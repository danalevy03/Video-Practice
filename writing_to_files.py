
employee_file = open("employees.txt", "a" )# Open the file in append mode
employee_file.write("\nToby - Human Resources") #append the file
employee_file.write("\nKelly - Customer Service") #append the file
employee_file.close() #close the file

employee_file = open("employees1.txt", "w" ) # Overwrite the file
employee_file.write("\nKelly - Customer Service") #append the file

# The code above will append the file with the new line "Toby - Human Resources" and then close the file.
# \n is used to create a new line in the file.
# Scape characters are used to create a new line in the file.




