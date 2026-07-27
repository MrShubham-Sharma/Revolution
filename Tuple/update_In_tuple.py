# note - Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
num =(2,4,5,3,3,4)

# convert in to list for update the index
x=list(num)

# after conversion change whatever index want o change
x[4]=6666

# now convert the list into tuple 
num= tuple(x)

print(num)

# adding the item in the tuple 

# same work as the update 
y = list(num)
y.append("orange")
num = tuple(y)
print(num)

# remove the item from the tuple 

z = list(num)
z.remove(3)

# 1 including and 3 where to stop
z[1:3]=["ninja","Jack"]
num= tuple(z)
print(num)