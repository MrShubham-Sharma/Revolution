# local function

# A variable created inside a function belongs to the local scope of that function,
#  and can only be used inside that function.
def my_function():
    x=10
    print(x)
my_function()

def Hello():
    greeting = "hello"
    def hello():
        print(greeting)
    hello()
Hello()