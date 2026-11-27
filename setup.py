from setuptools import setup, find_packages

setup(
    name="wetlang",
    version="2.2.0",
    description="Domain-Specific Programming Language & Cyber-Physical Engine for Neural Organoid Computing",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "wetlang=wetlang.cli:main",
            "wetc=compiler.compiler_cli:main",
        ],
    },
)
