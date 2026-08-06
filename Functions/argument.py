def friends(buddy):#buddy is a parameter
    # th ebuddy will act as an placeholder any value will call it will be replaced.
    print("nigga " +buddy)
friends("Prath ")#"Parth is an argument"
friends("Rohit ")

def add(x,y):
    return x+y
addition =add(20,30)
print(addition)

# passing the list by the function
def my_list(friend):
    for X in friend:
        print(X)
My_friends=["Parth","Rohit","Shubh"]
my_list(My_friends)

# default paramerter 
def my_friends(name= friends):
    print("Hello " +name)
my_friends("Shubh")
my_friends("Parth")

def country(Country):
    print("I'm form " + Country)
country("india")

def My_function(Animal,name):
    print(f"I Have {Animal} ")
    print(f"His name is {name} ")
My_function(Animal="Cat",name="Sweety")

def friends(person):
    print("Name:", person["name"])
    print("Age:",person["age"])
my_person ={"name":"Shubh","age":21}
friends(my_person)