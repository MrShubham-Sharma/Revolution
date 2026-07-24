#we want to create spacific list with new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
# only "a" letter word will be added in new list 
  if "a" in x:
    newlist.append(x)
print(newlist)

#with the single line syntax
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)