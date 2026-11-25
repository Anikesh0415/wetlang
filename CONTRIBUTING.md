# Contributing to WetLang

Thank you for contributing to **WetLang**, an open-source domain-specific language, static safety analyzer, and C99 closed-loop simulation runtime for bio-electronic MEA and neuromorphic execution.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anikesh0415/wetlang.git
   cd wetlang
   ```

2. **Install dependencies and build the C99 runtime:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   python native/build.py
   ```

3. **Verify the test suite:**
   ```bash
   pytest tests/
   ```

## Development Guidelines

- **Dimensional Safety:** Always specify physical dimensions (`ms`, `V`, `mV`, `uA`, `nC`, `uL/min`, `um`, `kOhm`, `Hz`). Never introduce unitless electrical stimulation.
- **Biophysical & C99 Invariants:** Native runtime components (`native/src/*.c`) must compile cleanly with zero warnings under `clang -std=c99 -Wall -Wextra -Werror -pedantic` and preserve zero dynamic heap allocations (`malloc`/`calloc`/`realloc`/`free`) in deterministic stepping paths.

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`.
2. Commit your changes with descriptive commit messages.
3. Ensure the E2E, pytest, and C99 zero-malloc checks pass cleanly.
4. Submit a Pull Request targeting `main`.
