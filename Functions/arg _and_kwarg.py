def my_function(*Friends):
    print(f"the youngest Kid is {Friends[2]}")
    print(f"the Smart One kid is {Friends[0]}")
    print(type(Friends))
    print(f"all friends are {Friends}")
my_function("Shubh","Rohit","parth")

def friends(greeting,*names):
    for name in names:
        print(greeting,name)
friends("Hello","Shubh","Parth","rohit")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))