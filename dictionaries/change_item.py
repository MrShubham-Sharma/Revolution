nigga ={
    "1st":"Parth","2nd":"Shubh","3rd":"Rohit"
}
# syntax for add the item in dictionaries
nigga["4th"]="Pratik"
print(nigga)

# .update() used for the update dictinaries
nigga.update({"all":"nigga"})
print(nigga)

nigga.pop("4th")
print(nigga)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
nigga.popitem()
print(nigga)