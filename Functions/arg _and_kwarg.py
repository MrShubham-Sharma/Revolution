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
# The double star ** tells Python: "Take all labeled key-value pairs passed here and pack them into a dictionary called kwargs."
#  Use this when your inputs have names (like profile details or settings).

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**name):
   print(f"He Is my Friend is {name["sname"]}")
my_function(sname="Shubh",yname="parth")

def my_function(**myvar):
   print("type is ", type(myvar))
   print("Name" ,myvar["name"])
   print("Age" ,myvar["age"] )
   print("all Data ",myvar)
my_function(name= "Shubh" ,age=21)

def my_function(Collage_Name,*Fees,**Student):
   print(f"Welcome TO The {Collage_Name}")
   total_fees =sum(Fees)
   print(f"total fess is {total_fees}")
   print(f"Student Data :{Student}")
my_function("Slrtce",12000,4000,43000,name="Shubham",age=21) 

def Data(**Hey):
   User_name =Hey.get("Name")
   User_age =Hey["age"]
   for x,v in Hey.items():
      print(f"{x} > {v}")
Data(Name="Shubham",age=21,goal="SDE")

def Laptop(Brand,**Specs):
   print(f"The Laptop Brand is {Brand}")
   print(f"Ram: is {Specs.get("ram")}")
   print(f"The Price is {Specs.get("Price")}")
   print("Remaning Specs are")
   for x,v in Specs.items():
      if x not in ["ram","Price"]:
         print(f"{x} -> {v}")
Laptop(Brand='lenovo',ram="16Gb",Price=74000,Storage="1TB SSD",GPU="RTX2050")

Employee_data={"name":"Shubh","age":21,"job":"SDE"}
def Employee(name,age,job):
   print(f"Employee: {name}, he's Age is {age} and He's an {job}")
Employee(**Employee_data)

def passenger(*passengers):
   for p in passengers:
      print(f"passengers Name is {p.get("name")} and he's seat is {p.get("Seat")}")
p1={"name" : "SHUBHAM" ,"Seat":"B3"}
p2={"name" : "PARTH" ,"Seat":"B6"}
passenger(p1,p2)