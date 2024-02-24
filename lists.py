#give it a name
# [] to store values inside
friends = ["Kevin", "Karen", "Jim"]
#             0        1       2     #we start indexing like this
print(friends)
#to access a specific element:
print(friends[0])
print(friends[-3]) #negatives to start indexing from the back of the list (the first one is -1)
#to select the last two elements
print(friends[1:])
print(friends[0:2]) #it does not include number 2

friends[1] = "Mike"
print(friends)