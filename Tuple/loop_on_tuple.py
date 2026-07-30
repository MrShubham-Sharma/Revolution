thistuple = ("apple", "banana", "cherry")
count=0
for x in thistuple:
  print(x)

# Print all items by referring to their index number:
for i in range(len(thistuple)):
  count+=1
  print(f"items in the Tuple {count} Item's are {thistuple[i]} ")