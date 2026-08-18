"""A small calculator with a command-line interface."""

import argparse


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return the difference between two numbers."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right


def divide(left: float, right: float) -> float:
    """Return the quotient of two numbers."""
    if right == 0:
        raise ValueError("Cannot divide by zero")
    return left / right


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Perform a basic calculation.")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()

    try:
        result = OPERATIONS[args.operation](args.left, args.right)
    except ValueError as error:
        parser.error(str(error))

    print(result)


if __name__ == "__main__":
    main()
