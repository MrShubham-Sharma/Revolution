Friends ={"Parth","Rohit","Shubh","Prashant"}

# .remove() removes the Item from list, if item in not list it will cause error
Friends.remove("Prashant")
print(Friends)

Friends.add("Omkar")

# .pop() removes the random item 
x = Friends.pop()

# .discard() removes the Item from list, if item in not list it will NOT cause error
Friends.discard("Omkar")
print(Friends)

# .clear() remove items from sets and gives the null set
Friends.clear()
print(Friends)

# del Delete the whole set from existance
del Friends
