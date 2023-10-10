"""Practice importing from other modules"""

# from <package name/directory/file> import <module name>
# imports the whole module, and runs the whole program
from lessons import my_functions

# <module name>, <function name>(arguments)
print(my_functions.addition(1, 2))

# <module name>, <variable name>
print(my_functions.my_variable)

if __name__ == "__main__":
    print("Howdy!")