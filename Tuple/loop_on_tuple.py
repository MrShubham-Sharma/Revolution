thistuple = ("apple", "banana", "cherry")
count=0
for x in thistuple:
  print(x)

# Print all items by referring to their index number:
for i in range(len(thistuple)):
  count+=1
  print(f"items in the Tuple {count} Item's are {thistuple[i]} ")

# Print all items, using a while loop to go through all the index numbers:
Material = ("Stick","Wood","cement","Bricks")
i=0
while i < len(Material):
  print(Material[i])
  i = i+1
  i=+1