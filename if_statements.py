# if statement: run one code when certain conditions are true
# run another code when other conditions are true
# if statements allow programs to respond to the input given

# create a boolean variable
is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall): #else if
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")