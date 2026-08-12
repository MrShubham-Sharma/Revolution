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