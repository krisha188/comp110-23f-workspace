"""Instantiating a Class, creating instances of the class."""

"""
This is where we instantiate the class 
we defined in classes.py.
In other words, we're creating objects 
that belong to that class.
"""

# import the class
# from <file_name>.module_name import <class_type>
from lessons.classes.pizza import Pizza

# instantiating pizza
# Pizza is the class like int or str
my_pizza: Pizza = Pizza("large", 10, True) # CONSTRUCTOR (Pizza())

# accessing/setting attributes
#my_pizza.size = "medium" # updates value from large to medium
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

# printing out some values
#print("my_pizza: ")
#print(my_pizza)

#print("Pizza")
#print(Pizza)

print("Size Attribute")
print(my_pizza.size)

print("Toppings:")
print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(inp_pizza: Pizza) -> float:
    """Calculate price of pizza"""
    if inp_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += 0.75 * inp_pizza.toppings
    if inp_pizza.gluten_free:
        price += 1.00
    return price

# Calling price funciton
print(price(sals_pizza))
print(price(my_pizza))

# Calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)