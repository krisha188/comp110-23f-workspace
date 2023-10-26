"""Practice with Dictionary syntax."""
# Can't have multiple keys in the same dictionary, but you can have duplicate values

# Creating a new dictionary
ice_cream: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}
print(ice_cream)

# Never use append to add elements to a dictionary
# Will add a key-value pair to the dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary:")
print(ice_cream)

# Use .pop with the name of a key to remove a key-value pair from dictionary
ice_cream.pop("mint")
print("Removed mint")
print(ice_cream)

# Accessing a value
# Can't use a double quote with chocolate because the computer thinks we are exiting the f-string
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# Modifying a value
ice_cream["vanilla"] = 18
ice_cream["vanilla"] += 2
print("After updating vanilla:")
print(ice_cream)

# Print the length
print(f"There are {len(ice_cream)} key-value pairs.")

# Check if the key is in the dictionary
# This should return a boolean value
print("Is chocolate in ice_cream?")
print("chocolate" in ice_cream)
print("Is mint in ice_cream?")
print("mint" in ice_cream)

# Using "in" in a conditional 
if "mint" in ice_cream: 
    print(f"There are {ice_cream['mint']} mint orders")
else: 
    print(f"There are no orders of mint")

# Using for loops over dictionaries
# Will loop over the keys (chocolate, vanilla, strawberry), not the values

for key in ice_cream:
    print(key)

# Printing out dictionary keys using loops
for flavor in ice_cream:
    # Print out <flavor> has <num_orders> orders
    print(f"{flavor} has {ice_cream[flavor]} orders")