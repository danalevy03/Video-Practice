# take a number and raise it to a specific power

# print(2**3) #2^3

#create an exponent function

def raise_to_power(base_num, pow_num):
    result = 1 #defining the variable
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))


