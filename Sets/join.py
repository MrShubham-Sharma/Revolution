# .union() commbines the two item sets
set1 ={1,3,5,6,7,8}
set2 ={"a","b","c","d","e","f"}
set3 =set1.union(set2)
print(set3)

# | gives the same output as union but only works set to set
set1 = set3 | set2 
print(set1)

set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set6 = {"John", "Elena"}
set7 = {"apple", "bananas", "cherry"}

set8= set4|set5|set6|set7
print(set8)

# Note: The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Note: Both union() and update() will exclude any duplicate items.
set7.update(set6)
print(set7)

# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set9={2,4,5,6,4,3,4,3,4,5}
set10={2,4,5,6,5,4,6,4,7}
set11=set9.intersection(set10)
print(set9)

# You can use the & operator instead of the intersection() method, and you will get the same result.
set11=set9 &set10
print(set11)

# Note: The & operator only allows you to join sets with sets, 
# and not with other data types like you can with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set9.intersection_update(set10)
print(set9)

# The difference() method will return a new set that will contain only the items 
# from the first set that are not present in the other set.

set13={"apple", "banana", "cherry"}
set12 = {"google", "microsoft", "apple"}
set14 = set13.difference(set12)

print(set14)

# Note: The - operator only allows you to join sets with sets,
# and not with other data types like you can with the difference() method.

set15=set12-set11
print(set15)

# The difference_update() method will keep the items from the first set that are not in the other set,
#  but it will change the original set instead of returning a new set.
data ={2,2,4,2,53,5,3,5}
data2 ={2,44,4,52,5,2,246,5}
data.difference_update(data2)
print(data)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
data.symmetric_difference(data2)
print(data2)

data3 = data^data2
print(data3)

# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
data.symmetric_difference_update(data3)
print(data)