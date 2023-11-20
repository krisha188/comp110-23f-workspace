"""File to define Bear class."""
__author__ = "730656379"


class Bear:
    """Simulates a bear!"""
    age: int
    hunger_score: int
    
    def __init__(self, age=0, hunger_score=0):
        """My constructor!"""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Simulates on day."""
        self.age = self.age + 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Simulates a bear's decreasing hunger after eating."""
        self.hunger_score += num_fish
        return None
