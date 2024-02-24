
# for loop allows us to loop over collection of items
# loop through arrays, letters inside a string, etc

friends = ["Jim", "Karen", "Kevin"]

for friend in friends:
    print(friend)

for index in range(3, 10): #not including 10
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")