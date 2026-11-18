# Contributing to WetLang

Thank you for your interest in contributing to **WetLang**! WetLang is an open-source domain-specific language for neural organoid wetware computing and cyber-physical life-support actuation.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wetworld/wetlang.git
   cd wetlang
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Verify the test suite:**
   ```bash
   pytest tests/
   ```

## Development Guidelines

- **Dimensional Safety:** Always specify physical dimensions where applicable (`ms`, `V`, `uL/min`, `mmHg`). Never introduce unitless electrical stimulation.
- **Biophysical Integrity:** The native C99 execution engine enforces strict Krogh cylinder diffusion checks ($r \le 200\,\mu\text{m}$), water-window electrochemical limits ($\pm 1.2\text{ V}$), and maximum firing refractory bounds ($500\text{ Hz}$).
- **Zero-Dependency Core:** The compiler and core VM runtime must maintain zero third-party dependencies outside the C standard library and Python standard library.

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-feature`.
2. Commit your changes with descriptive commit messages.
3. Ensure all tests pass: `pytest tests/`.
4. Submit a Pull Request targeting the `main` branch.
