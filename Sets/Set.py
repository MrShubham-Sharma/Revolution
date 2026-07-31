Friends = {"Rohit","Parth","Shubh","Shubh"}

# in the set all items get sorted
# double items are not printed twice only single time 

print(Friends)

# set can be any data type
Set = {1,3,5,"Shubh",2.4}
print(Set)

# Create The Set By the set() finction
Set1=set((1,2,4,4,32,5,5,3,5,6,4))
print(Set1)

# for find the type of set 
print(type(Set1))

# acsess by loop
for x in Friends:
    print(x)

# check if item in set
print("Shubh"in Friends)

print("Parth"not in Friends)