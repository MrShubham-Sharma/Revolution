# ideal way to use the for loop on set 
item ={"Bricks","Cement","Sand","Labour"}
item.remove("Labour")
for x in item:
    print(x)

# we can not use the for loop on the set directly so we have to convert it into the list 
# and then we can use the while loop on the set

item_list =list(item)
i=0 
while i <len(item_list):
    print(item_list[i])
    i =i+1