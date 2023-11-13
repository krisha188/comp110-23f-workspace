"""Defining a Class!"""
from __future__ import annotations

"""
Think of a class definition as a "roadmap" 
for objects that belong to the class. 
You are defining the underlying structure every 
instance of this class will have
"""

class Pizza:

    # attributes
    # Think of these as the variables each 
    # instance of my class will have
    # <name> : <type> 
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf: bool):
        "My constructor"
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf
        # returns a Pizza object, but we don't have to declare return
    
    # Methods can only be used in there specific class
    def price(self) -> float:
        """Calculate the price of a pizza"""
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
        price += 0.75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    # method to update attribute
    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to existing pizza"""
        self.toppings += num_toppings

    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """Make a new pizza with existing pizza's propoerties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza