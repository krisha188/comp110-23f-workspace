"""Things I'll be importing"""

def addition(x: int, y: int):
    return x + y

my_variable: str = "Hello!"

if __name__ == "__main__": #prints this string only when running my_functions
    print("This should only print when running my_functions")
else:  # prints this string when running my_functions in another file
    print("my_functions is being imported")