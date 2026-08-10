def changecase(func):
    def my_inner():
       return func().upper()
    return my_inner

# Multiple Decorator Calls
# A decorator can be called multiple times. 
# Just place the decorator above the function you want to decorate.

@changecase
def my_function():
    return "Hello Master"
print(my_function())

@changecase
def Function2():
    return "Hellow !"
print(Function2())

@changecase
def func2():
    return "yooo Buddy!"
print(func2())


# passing argument 

def changecase(fun):
    def inner(x):
        return fun(x).upper()
    return inner

@changecase
def my_function(Name):
    return "Hellow !" + Name
print(my_function("Parth")) 

# Sometimes the decorator function has no control over the arguments passed from decorated function,
#  to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, 
# and any type of arguments, and pass them to the decorated function.

def change(fun):
    def my_function(*args,**kwargs):
        return fun(*args,**kwargs).upper()
    return my_function

@change
def fun(nam):
    return "HELLOW Mr." +nam
print(fun("Shubham"))