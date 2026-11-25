import * as vscode from 'vscode';
import * as cp from 'child_process';
import * as path from 'path';

let diagnosticCollection: vscode.DiagnosticCollection;
const debounceTimers = new Map<string, NodeJS.Timeout>();

interface LinterDiagnostic {
    file: string;
    line: number;
    column: number;
    severity: string;
    code: string;
    message: string;
}

export function activate(context: vscode.ExtensionContext) {
    diagnosticCollection = vscode.languages.createDiagnosticCollection('wetlang');
    context.subscriptions.push(diagnosticCollection);

    context.subscriptions.push(
        vscode.workspace.onDidOpenTextDocument((doc) => {
            if (doc.languageId === 'wetlang') {
                runLinter(doc);
            }
        })
    );

    context.subscriptions.push(
        vscode.workspace.onDidChangeTextDocument((event) => {
            if (event.document.languageId === 'wetlang') {
                scheduleLinter(event.document);
            }
        })
    );

    context.subscriptions.push(
        vscode.workspace.onDidSaveTextDocument((doc) => {
            if (doc.languageId === 'wetlang') {
                runLinter(doc);
            }
        })
    );

    context.subscriptions.push(
        vscode.workspace.onDidCloseTextDocument((doc) => {
            diagnosticCollection.delete(doc.uri);
            const key = doc.uri.toString();
            const timer = debounceTimers.get(key);
            if (timer) {
                clearTimeout(timer);
                debounceTimers.delete(key);
            }
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('wetlang.check', () => {
            const activeEditor = vscode.window.activeTextEditor;
            if (activeEditor && activeEditor.document.languageId === 'wetlang') {
                runLinter(activeEditor.document);
            }
        })
    );

    vscode.workspace.textDocuments.forEach((doc) => {
        if (doc.languageId === 'wetlang') {
            runLinter(doc);
        }
    });
}

export function deactivate() {
    if (diagnosticCollection) {
        diagnosticCollection.clear();
        diagnosticCollection.dispose();
    }
    debounceTimers.forEach((timer) => clearTimeout(timer));
    debounceTimers.clear();
}

function scheduleLinter(document: vscode.TextDocument) {
    const key = document.uri.toString();
    const existing = debounceTimers.get(key);
    if (existing) {
        clearTimeout(existing);
    }

    const timer = setTimeout(() => {
        debounceTimers.delete(key);
        runLinter(document);
    }, 300);
    debounceTimers.set(key, timer);
}

function runLinter(document: vscode.TextDocument) {
    const config = vscode.workspace.getConfiguration('wetlang');
    const enabled = config.get<boolean>('linter.enable', true);
    if (!enabled) {
        diagnosticCollection.delete(document.uri);
        return;
    }

    const maxTicks = config.get<number>('linter.maxUnsyncedTicks', 1000);
    const executable = config.get<string>('linter.executablePath', 'wetlang');
    const filePath = document.uri.scheme === 'file' ? document.uri.fsPath : (document.fileName || '<untitled>');
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    const cwd = (document.uri.scheme === 'file' && filePath)
        ? path.dirname(filePath)
        : (workspaceRoot || process.cwd());

    const checkArgs = [
        'check',
        '--format=json',
        '--max-unsynced-ticks',
        String(maxTicks),
        '--stdin',
        '--filename',
        filePath
    ];
    const sourceText = document.getText();

    const invokeLinter = (
        bin: string,
        args: string[],
        onFallback?: () => void
    ) => {
        const child = cp.execFile(bin, args, { cwd, shell: false }, (error, stdout, _stderr) => {
            const errCode = (error as NodeJS.ErrnoException | null)?.code;
            const jsonStr = stdout ? stdout.trim() : '';
            if (!jsonStr && error && (errCode === 'ENOENT' || executable === 'wetlang') && onFallback) {
                onFallback();
                return;
            }
            parseAndPublishDiagnostics(document, jsonStr);
        });
        if (child.stdin) {
            child.stdin.on('error', () => { /* ignore EPIPE if child exits early */ });
            child.stdin.end(sourceText, 'utf8');
        }
    };

    const pythonCandidates = process.platform === 'win32'
        ? ['python', 'py', 'python3']
        : ['python3', 'python'];

    const tryPythonFallback = (idx: number) => {
        if (idx >= pythonCandidates.length) {
            return;
        }
        const pyBin = pythonCandidates[idx];
        invokeLinter(
            pyBin,
            ['-m', 'wetlang.cli', ...checkArgs],
            () => tryPythonFallback(idx + 1)
        );
    };

    if (executable === 'wetlang') {
        invokeLinter(executable, checkArgs, () => tryPythonFallback(0));
    } else {
        invokeLinter(executable, checkArgs);
    }
}

function parseAndPublishDiagnostics(document: vscode.TextDocument, jsonStr: string) {
    if (!jsonStr) {
        diagnosticCollection.set(document.uri, []);
        return;
    }

    try {
        const rawDiags: LinterDiagnostic[] = JSON.parse(jsonStr);
        const vsDiags: vscode.Diagnostic[] = rawDiags.map((d) => {
            const line = Math.max(0, (d.line || 1) - 1);
            const col = Math.max(0, (d.column || 1) - 1);
            const range = new vscode.Range(line, col, line, col + 1);

            const severity = d.severity && d.severity.toLowerCase() === 'warning'
                ? vscode.DiagnosticSeverity.Warning
                : vscode.DiagnosticSeverity.Error;

            const diagnostic = new vscode.Diagnostic(range, d.message, severity);
            diagnostic.code = d.code;
            diagnostic.source = 'wetlang';
            return diagnostic;
        });

        diagnosticCollection.set(document.uri, vsDiags);
    } catch (_e) {
        // Safe ignore
    }
}
