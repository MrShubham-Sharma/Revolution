car ={
    "Modle": "Supra",
    "Series": "MK4",
    "year" : 1993
}
for x in car:
    print(x)

print(car["Modle"])

# Return an object providing a view on the dict's values.

for x in car.values():
    print(x)

# Return a set-like object providing a view on the dict's keys.

for x in car.keys():
    print(x)

# Return a set-like object providing a view on the dict's items.

for x in car.items():
    print(x)