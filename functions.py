# organize, break up the code into chunks
# core concept

# FIRST STEP: i need a key word which is called def
# def = this person wants to use a function
# after def we need to give it a name
# all code after "def sayhi()": will be inside of the function
# we need to indent. the code inside of the function must be indented

def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

# i need to call the function. we must specify
# calling the function:
say_hi("Mike", 25)
say_hi("Steve", 44)

# we want functions to be named in lowercase
# we can give functions information
# PARAMETER is a piece of information that we give to the function
#"def sayhi(PARAMETER GOES HERE)"