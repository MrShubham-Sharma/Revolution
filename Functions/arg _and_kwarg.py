def my_function(*Friends):
    print(f"the youngest Kid is {Friends[2]}")
    print(f"the Smart One kid is {Friends[0]}")
    print(type(Friends))
    print(f"all friends are {Friends}")
my_function("Shubh","Rohit","parth")