# Recursion

# Recursion is when a function calls itself.
def coundown(n):
    if n<=0:
        print("Boooooooom!")
    else:
        print(n)
        coundown(n-1)
coundown(10)

# Base Case and Recursive Case

# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
    # base case 
    if n==0 or n==1:
        return 1 

    else:
        return n*factorial(n-1)
print(factorial(5))

# fibonacci series for base case and recursive case
def fibonacci(n):
    if n<=1 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))