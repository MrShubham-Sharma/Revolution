
# The values in dictionary items can be of any data type:
Me= {
    "Name": "Shubh",
    "Age" : 21,
    "Profession" :"Software Engineer",
    "colors": ["red", "white", "blue"]
}
print(Me)
print(type(Me))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

Friends = dict(Shubh=21,Parth=21,Rohit=21)
print(Friends)

print(len(Me))
print(len(Friends))

x= Friends["Parth"]
print(x)

# There is also a method called get() that will give you the same result:

y= Friends.get("Rohit")
print(y)

# The keys() method will return a list of all the keys in the dictionary.
z=Friends.keys()
print(z)

# The list of the keys is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the keys list.
b=Friends.keys()
Friends["om"]= 21

print(b)
B=Friends.values()
print(B)

# The returned list is a view of the items of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the items list.
A=Friends.items()
print(A)
if "Shubh" in Friends:
    print("Yeahh !")