car ={
    "Modle": "Supra",
    "Series": "MK4",
    "year" : 1993
}
for x in car:
    print(x)

print(car["Modle"])

for x in car.values():
    print(x)

for x in car.keys():
    print(x)

for x in car.items():
    print(x)