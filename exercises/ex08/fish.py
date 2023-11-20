"""File to define Fish class."""
__author__ = "730656379"


class Fish:
    """Simulates fish in river!"""
    age: int

    def __init__(self, age=0):
        """My constructor!"""
        self.age = age
        return None
    
    def one_day(self):
        """Simulates one day in the river."""
        self.age += 1
        return None