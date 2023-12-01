"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730656379"


class Simpy:
    """Class Simpy!"""
    values: list[float]

    def __init__(self, values: list[float] = []) -> None:
        """My constructor!"""
        self.values = values
    
    def __str__(self) -> str:
        """Overloads str operator."""
        lst = f"Simpy({self.values})"
        return lst
    
    def fill(self, value: float, number: int) -> None:
        """Fills in values list in a simpy with value for a number of times."""
        self.values = [value] * number 
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Will fill in a list with values from start to stop."""
        assert step != 0.0
        if start >= 0:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Gives the sum of a the numbers in the value attribute."""
        i = 0
        sum = 0
        while i < len(self.values):
            sum += self.values[i]
            i += 1
        return sum
    
    def __add__(self, right: Union[Simpy, float]) -> Simpy:
        """Will add the simpy values together or a simpy and a float."""
        new: Simpy = Simpy([])
        if type(right) is float:
            for i in range(0, len(self.values)):
                elements = self.values[i] + right
                new.values.append(elements)
        else:
            assert len(self.values) == len(right.values)
            for i in range(0, len(self.values)):
                elements = self.values[i] + right.values[i]
                new.values.append(elements)
        return new

    def __pow__(self, right: Union[Simpy, float]) -> Simpy:
        """Will do the same as add, but now with exponents."""
        new: Simpy = Simpy([])
        if type(right) is float:
            for i in range(0, len(self.values)):
                elements = self.values[i] ** right
                new.values.append(elements)
        else:
            assert len(self.values) == len(right.values)
            for i in range(0, len(self.values)):
                elements = self.values[i] ** right.values[i]
                new.values.append(elements)
        return new

    def __eq__(self, right: Union[Simpy, float]) -> list[bool]:
        """Overwrites the equal sign to return a list of true of false if the values are the same."""
        new = []
        if type(right) is float:
            for i in range(0, len(self.values)):
                if self.values[i] == right:
                    new.append(True)
                else:
                    new.append(False)
        else:
            assert len(self.values) == len(right.values)
            for i in range(0, len(self.values)):
                if self.values[i] == right.values[i]:
                    new.append(True)
                else:
                    new.append(False)
        return new
    
    def __gt__(self, right: Union[Simpy, float]) -> list[bool]:
        """Overloads the greater than operator to see if the values are greater and returns an array of bools."""
        new = []
        if type(right) is float:
            for i in range(0, len(self.values)):
                if self.values[i] > right:
                    new.append(True)
                else:
                    new.append(False)
        else:
            assert len(self.values) == len(right.values)
            for i in range(0, len(self.values)):
                if self.values[i] > right.values[i]:
                    new.append(True)
                else:
                    new.append(False)
        return new
    
    def __getitem__(self, mask: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Will return the index value of to values list or return a simpy values list of the numbers that fit the expectation."""
        new = Simpy([])
        if type(mask) is int:
            return self.values[mask]
        else:
            for i in range(0, len(self.values)):
                if mask[i] is True:
                    new.values.append(self.values[i])
            return new