"""Practice with classes."""
from __future__ import annotations
__author__ = "730656379"


class Point:
    """Create a new class that makes a point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor!"""
        self.x = x_init
        self.y = y_init
    
    """def scale_by(self, factor: int) -> None:
        Modifies existing point.
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        Makes a new point that increases by the factor.
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point"""
    
    def __str__(self) -> str:
        """Returns a string of x and y attributes."""
        string = (f"x: {self.x}; y: {self.y}")
        return string

    def __mul__(self, factor: int | float) -> Point:
        """Tells the * what to do."""
        point = Point(self.x * factor, self.y * factor)
        return point 

    def __add__(self, factor: int | float) -> Point:
        """Tells the + what to do."""
        new_point = Point(self.x + factor, self.y + factor)
        return new_point
    