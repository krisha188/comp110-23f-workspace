"""Summing the elements of a list using different loops."""

__author__ = "730656379"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of the list."""
    sum: float = 0
    x = 0
    while x < len(vals):
        sum += vals[x] 
        x += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of the list."""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of the list."""
    sum: float = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum