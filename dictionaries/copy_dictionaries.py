items ={
    "Grocery":"Oli,Rice",
    "Fule":"Gas",
    "Requirement":"Water,Food"
}
# to copy the all item to the diffrent list 
list1 = items.copy()
print(list1)

list2= dict(items)
print(list2)

# for only copy the particuler items use this syntax 
grocery={"Grocery":items["Grocery"]}
print(grocery)