shoes = ("nike","Asian","puma","jorden","bata")

# it will only print nike and puma
print(shoes[0:2])

# chose an perticuler index
print(shoes[2])

# the items from the beginning to, but NOT included "puma"
print(shoes[:2])

# By leaving out the end value, the range will go on to the end of the tuple
print(shoes[1:])


# negetive indexing

# -4 including and -1 excluding 
print(shoes[-4:-1])

# it will print -3 index item
print(shoes[-3])

if "puma" in shoes:
    print("yes! it's there")