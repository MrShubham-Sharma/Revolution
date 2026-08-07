def my_function(*Friends):
    print(f"the youngest Kid is {Friends[2]}")
    print(f"the Smart One kid is {Friends[0]}")
    print(type(Friends))
    print(f"all friends are {Friends}")
my_function("Shubh","Rohit","parth")

def friends(greeting,*names):
    for name in names:
        print(greeting,name)
        # "Hello" is assigned to greeting, and the rest are collected in names.
friends("Hello","Shubh","Parth","rohit")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num 

print(my_function(5, 3, 6, 7, 8, 3))

# Arbitrary Keyword Arguments - **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**name):
   print(f"He Is my Friend is {name["sname"]}")
my_function(sname="Shubh",yname="parth")