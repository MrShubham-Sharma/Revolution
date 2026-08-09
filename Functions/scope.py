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

x=300
def num():
    print(x)
num()
print(x)