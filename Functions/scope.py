# local function

# A variable created inside a function belongs to the local scope of that function,
#  and can only be used inside that function.
def my_function():
    x=10
    print(x)
my_function()

# Function Inside Function

# As explained in the example above, 
# the variable x is not available outside the function, but it is available for any function inside the function:
def Hello():
    greeting = "hello"
    def hello():
        print(greeting)
    hello()
Hello()

# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

x=300
def num():
    print(x)
num()
print(x)

# Naming Variables

# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
# one available in the global scope (outside the function) and one available in the local scope (inside the function):

x = "Shubh"
def hi():
    x="Parth"
    print(x)
hi()
print(x)

# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

x=200
# we can use the global keyword for change global variable in the function.
def yo():
    global x
    x=3000
    print(x)
yo()
print(x)