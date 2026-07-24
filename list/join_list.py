#adding by the "+"
list1=[25,33,4,5,55,333]
list2=[29,35,556,35]
list3= list1 +list2
print(list3)

#join list by the append()
list3=[25,33,4,5,55,333]
list4=[234,54,56,33,5]
# in list4 the list3 will be added by for loop
for x in list4:
    # in list3 the list4 items will be added 
    list3.append(x)
print(list3)

list5 = [2,4,5,6]
list6 = [4,35,6,36,46]
list5.extend(list6)
print(list5)