# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.
def my_function():
    print(f"Hello Master")
# To call a function, write its name followed by parentheses:
my_function()
# we can call multiple time functions
my_function()
my_function()
my_function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# return fucntion 
def Greeting():
   return "Hello Master"
To_Master = Greeting()
print(To_Master)

# If a function doesn't have a return statement, it returns None by default

print(Greeting())

def Hello():
   pass
# pass act as the placeholder it allowing you to define the structure first and implement details later.

