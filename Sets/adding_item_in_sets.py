# we can add item in set by the .add() function

Set1 = {1,3,4,5,6}
Set1.add(24)
print(Set1)

Set2 = {23,35,5,78,73}

# in the set we can marge two set with the update() function.
Set1.update(Set2)
print(Set1)

# in the we can add any iterable.
Set3 =[25,342,24,53]
Set1.update(Set3)
print(Set1)