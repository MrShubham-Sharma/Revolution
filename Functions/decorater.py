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
