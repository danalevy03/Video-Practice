#basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
#result = num1 + num2
#print(result)
# i need to convert the numbers from strings into numbers
#result = int (num1)  + int(num2)
#print(result)
# use integer to convert the values into integers (whole numbers)
# putting decimals will break the program
result = float(num1) + float(num2)
print(result)
# with FLOAT we can have our decimals!