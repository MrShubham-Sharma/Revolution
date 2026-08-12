# Lambda Functions

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

#  it's an reguler expression like wise normal a+b
x = lambda a :a+ 100
print(x(400))

# addition argument
x = lambda a,b,c: a+b+c
print(x(2,3,4))

# multiply argument 
x = lambda a,b: a*b
print(x(34,36))

def my_function(n):
    return lambda a: a*n
triple = my_function(3)
double =my_function(2)
print(triple(22))
print(double(220))

# Use lambda functions when an anonymous function is required for a short period of time.

# Lambda with Built-in Functions

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
# Using Lambda with map()
# The map() function applies a function to every item in an iterable:

list1 = [1,2,4,4,64,3]
triple = list(map(lambda a:a *3, list1))
print(triple)

list2 =[1,4,56,6,3,5]
double= list(map(lambda a,b :a*b , list1 ,list2))
print(double)