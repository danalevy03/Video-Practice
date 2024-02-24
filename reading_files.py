
#copen("employees.txt", "w" )# Open the file in write mode
#copen("employees.txt", "a" )# Open the file in append mode
# open("employees.txt", "r+" )# Open the file in read and write mode


employee_file = open("employees.txt", "r" )# Open the file in read mode

# print(employee_file.readable()) #check if the file is readable
# print(employee_file.read()) #read the file
# print(employee_file.readline()) #read the first line
# print(employee_file.readline()) #read the second line
# print(employee_file.readline()) #read the third line

for employee in employee_file.readlines(): #read all the lines and put them in a list
    print(employee)

# print(employee_file.readlines()[0]) #read all the lines and put them in a list
employee_file.close()