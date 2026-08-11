# Preserving Function Metadata

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
def greeting():
    return "Hello Buddy"
print(greeting.__name__)

# when the function is decorated the original metadata was lost and for this function.wraps
# was used from the functools library 
 
import functools
def changecase(fun):
    @functools.wraps(fun)
    def inner():
        return fun().upper()
    return inner

@changecase
def my_function():
    return "Hello Buddy"
print(my_function.__name__)
print(my_function())
print(my_function.__doc__)