#\n inserts another line

phrase = "Giraffe Academy"
print(phrase + " is cool") #concatenation

# a function is a block of code and will perform a specific operation
# use them to modify and get information about our strings

print(phrase.lower()) #lower case
print(phrase.upper()) #upper case
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[3])
# a string gets indexed starting from 0.
# if python is counting characters, it will start with 0
print(phrase.index("Acad")) #index where is it located --> 0,1,2.. (starts)
print(phrase.replace("Giraffe", "Elephant"))
