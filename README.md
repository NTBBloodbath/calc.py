# Calc - A powerful Python REPL calculator

This is a calculator with a complex source that includes a small AST, a parser
and a tokenizer. This is a personal project _done in 2 days_ to understand how
operator precedence works and to practice my rusty skills of making interpreters.

This project has no external dependencies and should work with minimum
Python `3.8` and newer versions of the Python interpreter. 

## Features

- Complex but small and understandable source code. Implemented in less than 450LoC
- Supports all basic operations (sum, substraction, multiplication, division)
- Supports use of parentheses
- Proper precedence order of operations
- Rich errors handling (human-readable exceptions and hints to fix them)

## Usage

Just start `main.py` with Python, this will create a REPL in your terminal which
you can close by typing `exit`.

## Modules explanation

- `ast`
  - Contains all Tree classes
- `evaluator`
  - Evaluates our generated AST
- `exception`
  - Error handling, custom Exception class
- `parser`
  - Parses our generated tokens and makes an AST
- `scanner`
  - Scans our expressions and makes tokens
- `token`
  - Tokenizer classes, debugging function to print tokens

## License

This calculator is licensed under [GPLv3](./LICENSE).
