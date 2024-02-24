
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #catches all division by zero errors
    print(err)
except ValueError: #catches all invalid inputs
    print("Invalid input")