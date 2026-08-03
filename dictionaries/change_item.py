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

nigga.popitem()
print(nigga)