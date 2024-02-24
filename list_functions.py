# list allows to organize and store values inside their list structure

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends)

friends.extend(lucky_numbers) #add two lists
print(friends)

# append another item to the end of the list
friends.append("Creed")
print(friends)

# add an item into the middle of the list
friends.insert(1, "Kelly")
print(friends)

#remove elements
friends.remove("Karen")
print(friends)

# reset the list
# friends.clear()
# print(friends)

# pop will pop an item off of the list --> the last one
friends.pop()
print(friends)

print(friends.index("Kevin")) #will tell me the index of Kevin

print(friends.count("Jim")) #count how many times

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.sort() # alphabetical order
print(friends)

lucky_numbers.sort() # ascending order
print(lucky_numbers)

lucky_numbers.reverse() # descending order
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)