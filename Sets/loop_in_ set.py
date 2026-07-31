item ={"Bricks","Cement","Sand","Labour"}
item.remove("Labour")
for x in item:
    print(x)

item_list =list(item)
i=0 
while i <len(item_list):
    print(item_list[i])
    i =i+1