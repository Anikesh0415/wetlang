"""
Test Suite: Official VS Code Extension & Token Parity Verification (Milestone 3)
Verifies:
1. VS Code extension manifest, configuration, and syntax grammar existence and schema validity.
2. 100% token coverage parity between compiler/token.py (73 canonical tokens) and syntaxes/wet.tmLanguage.json.
3. Physical unit literal coverage across all supported biophysical dimensions.
"""

import json
import re
from pathlib import Path
import pytest

from compiler.token import KEYWORDS, UNIT_SUFFIXES, SORTED_UNIT_SUFFIXES

REPO_ROOT = Path(__file__).resolve().parent.parent
VSCODE_DIR = REPO_ROOT / "vscode-wetlang"
SYNTAX_PATH = VSCODE_DIR / "syntaxes" / "wet.tmLanguage.json"
PKG_PATH = VSCODE_DIR / "package.json"
LANG_CFG_PATH = VSCODE_DIR / "language-configuration.json"
TSCONFIG_PATH = VSCODE_DIR / "tsconfig.json"
EXTENSION_TS_PATH = VSCODE_DIR / "src" / "extension.ts"
ICON_PATH = VSCODE_DIR / "icons" / "wetlang.png"

CANONICAL_OPERATORS = [
    "+", "-", "*", "/", "%",
    "==", "!=", "<", "<=", ">", ">=",
    "&&", "||", "!",
    "=", "->"
]


def test_vscode_extension_files_exist():
    """Verify that all mandatory extension assets are present."""
    assert VSCODE_DIR.is_dir(), "vscode-wetlang directory missing"
    assert PKG_PATH.is_file(), "package.json missing"
    assert LANG_CFG_PATH.is_file(), "language-configuration.json missing"
    assert TSCONFIG_PATH.is_file(), "tsconfig.json missing"
    assert SYNTAX_PATH.is_file(), "wet.tmLanguage.json missing"
    assert EXTENSION_TS_PATH.is_file(), "src/extension.ts missing"
    assert ICON_PATH.is_file(), "icons/wetlang.png missing"
    assert ICON_PATH.stat().st_size > 0, "Icon file is empty"


def test_package_json_manifest_schema():
    """Verify package.json contributes proper language, grammars, and config."""
    with open(PKG_PATH, "r", encoding="utf-8") as f:
        pkg = json.load(f)

    assert pkg.get("name") == "wetlang"
    assert pkg.get("displayName") == "WetLang"
    assert pkg.get("publisher") == "finalspark"
    assert pkg.get("version") == "2.1.2"
    assert "onLanguage:wetlang" in pkg.get("activationEvents", [])

    contrib = pkg.get("contributes", {})
    assert "languages" in contrib
    langs = contrib["languages"]
    assert any(l.get("id") == "wetlang" and ".wet" in l.get("extensions", []) for l in langs)

    assert "grammars" in contrib
    grammars = contrib["grammars"]
    assert any(g.get("language") == "wetlang" and g.get("scopeName") == "source.wet" for g in grammars)

    assert "configuration" in contrib
    props = contrib["configuration"].get("properties", {})
    assert "wetlang.linter.executablePath" in props
    assert "wetlang.linter.enable" in props
    assert "wetlang.linter.maxUnsyncedTicks" in props


def test_language_configuration_json():
    """Verify language comment rules, brackets, and auto-closing pairs."""
    with open(LANG_CFG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    assert "comments" in cfg
    assert cfg["comments"].get("lineComment") == "//"
    assert cfg["comments"].get("blockComment") == ["/*", "*/"]

    assert "brackets" in cfg
    brackets = cfg["brackets"]
    assert ["{", "}"] in brackets
    assert ["[", "]"] in brackets
    assert ["(", ")"] in brackets

    assert "autoClosingPairs" in cfg
    pairs = cfg["autoClosingPairs"]
    open_pairs = {p["open"]: p["close"] for p in pairs}
    assert open_pairs.get("{") == "}"
    assert open_pairs.get("[") == "]"
    assert open_pairs.get("(") == ")"


def _extract_patterns(grammar_dict):
    """Extract all regex pattern strings from a TextMate grammar."""
    patterns = []
    for item in grammar_dict.get("patterns", []):
        if "match" in item:
            patterns.append(item["match"])
    for _, repo_entry in grammar_dict.get("repository", {}).items():
        for item in repo_entry.get("patterns", []):
            if "match" in item:
                patterns.append(item["match"])
    return patterns


def test_token_parity_73_canonical_tokens():
    """
    Verify 100% token coverage parity:
    57 keywords + 16 operators = 73 canonical tokens.
    """
    with open(SYNTAX_PATH, "r", encoding="utf-8") as f:
        grammar = json.load(f)

    patterns = _extract_patterns(grammar)
    assert len(patterns) > 0, "No regex patterns found in grammar"

    # 1. Verify all 57 keywords
    assert len(KEYWORDS) == 57, f"Expected 57 keywords in token.py, found {len(KEYWORDS)}"
    unmatched_keywords = []
    for kw in KEYWORDS:
        matched = any(re.search(pat, kw) for pat in patterns)
        if not matched:
            unmatched_keywords.append(kw)

    assert not unmatched_keywords, f"Unmatched keywords in TextMate grammar: {unmatched_keywords}"

    # 2. Verify all 16 canonical operators
    assert len(CANONICAL_OPERATORS) == 16, f"Expected 16 canonical operators, found {len(CANONICAL_OPERATORS)}"
    unmatched_operators = []
    for op in CANONICAL_OPERATORS:
        matched = any(re.search(pat, op) for pat in patterns)
        if not matched:
            unmatched_operators.append(op)

    assert not unmatched_operators, f"Unmatched operators in TextMate grammar: {unmatched_operators}"

    # Total check
    total_tokens = len(KEYWORDS) + len(CANONICAL_OPERATORS)
    assert total_tokens == 73, f"Expected 73 total canonical tokens, got {total_tokens}"


def test_physical_unit_literals_highlighted():
    """Verify that physical unit literals with SI suffixes are matched by grammar."""
    with open(SYNTAX_PATH, "r", encoding="utf-8") as f:
        grammar = json.load(f)

    patterns = _extract_patterns(grammar)

    test_units = ["100mV", "20ms", "500us", "1.5uL/min", "30uA", "0.5nC", "10kOhm", "50Hz", "37degC", "100kPa"]
    for sample in test_units:
        matched = any(re.search(pat, sample) for pat in patterns)
        assert matched, f"Physical literal sample '{sample}' was not matched by any grammar pattern"
