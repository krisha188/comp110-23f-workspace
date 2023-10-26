"""Combiing two lists into a dictionaries."""
__author__ = "730656379"


def zip(x: list[str], y: list[int]) -> dict[str, int]:
    """Returns a dictionary where x is the key and y is the value."""
    dictionary: dict[str, int] = {}
    i = 0
    assert len(x) == len(y)
    while i < len(x):
        dictionary[x[i]] = y[i]
        i += 1
    return dictionary

print(zip(['a', 'b'], [1, 2, 3]))