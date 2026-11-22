import sys
from pathlib import Path

tests_dir = Path(__file__).resolve().parent
repo_root = tests_dir.parent
wetlang_pkg = repo_root / "wetlang"

for p in [str(repo_root), str(wetlang_pkg)]:
    if p not in sys.path:
        sys.path.insert(0, p)
