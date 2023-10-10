"""Lists."""
__author__ = "730656379"

def all(x: list[int], y: int) -> bool:
    value = False
    counter: int = 0
    idx: int = 0
    if len(x) > 0:
        while idx < len(x):
            if x[idx] == y:
                counter += 1
            else:
                counter == counter 
            idx += 1
    if counter == len(x):
        value = True
    return value

def max(x: list[int]) -> int:
    if len(x) == 0:
        raise ValueError('max() arg is an empty List')
    max = x[0]
    idx = 1
    while idx < len(x):
        if x[idx] > max:
            max = x[idx]
        idx += 1
    return max 

def is_equal(x: list[int], y: list[int]) -> bool:
    counter: int = 0
    idx: int = 0
    while idx < len(x):
        if x[idx] == y[idx]:
            counter += 1
        idx += 1
    if counter == len(x):
        return True
    else: 
        return False
