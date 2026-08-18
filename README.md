# Basic Python Calculator

A simple command-line calculator supporting addition, subtraction,
multiplication, division, powers, and modulo.

## Requirements

- Python 3.9 or newer

No third-party packages are required.

## Run the calculator

Pass an operation followed by two numbers:

```powershell
python calculator.py add 2 3
python calculator.py subtract 10 4
python calculator.py multiply 6 7
python calculator.py divide 20 5
python calculator.py power 2 8
python calculator.py modulo 10 3
```

The available operations are `add`, `subtract`, `multiply`, `divide`, `power`,
and `modulo`.

## Run the tests

From the project directory, run:

```powershell
python -m unittest discover
```
