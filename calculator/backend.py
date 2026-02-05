"""Calculator backend module with basic operations.

This module exposes basic arithmetic plus hooks for advanced operations
provided in `calculator.advanced`.
"""
from typing import Union

from . import advanced


Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def calculate(op: str, a: Number, b: Number) -> Number:
    """Calculate using an operation string.

    Supported ops:
      +, -, *, /           (basic)
      pow, ^              (power)
      mod, %              (modulus)
      percent             (percentage: a percent of b -> (a/100)*b )
      sqrt                (square root of a; b ignored)
    """
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "pow": advanced.power,
        "^": advanced.power,
        "mod": advanced.mod,
        "%": advanced.mod,
        "percent": advanced.percent_of,
        "sqrt": advanced.sqrt,
    }
    if op not in ops:
        raise ValueError(f"unsupported operation: {op}")
    func = ops[op]
    # sqrt expects one argument; keep signature stable by only passing a
    if op == "sqrt":
        return func(a)
    return func(a, b)
