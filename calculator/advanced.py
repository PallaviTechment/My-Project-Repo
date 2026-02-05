"""Advanced calculator operations kept separate from core backend.

Includes unary and non-basic binary operations used by the UI/API.
"""
from typing import Union

Number = Union[int, float]


def power(a: Number, b: Number) -> float:
    a = float(a)
    b = float(b)
    return a ** b


def mod(a: Number, b: Number) -> float:
    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a % b


def sqrt(a: Number) -> float:
    a = float(a)
    if a < 0:
        raise ValueError("sqrt of negative")
    return a ** 0.5


def negate(a: Number) -> float:
    return -float(a)


def percent_of(a: Number, b: Number) -> float:
    """Return a percent of b: (a / 100) * b

    Example: a=10, b=200 -> 10% of 200 -> 20
    """
    a = float(a)
    b = float(b)
    return (a / 100.0) * b
