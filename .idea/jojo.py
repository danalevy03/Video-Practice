 # Write a function that takes an integer as parameter and returns a list of all thedivisors of that number

def divisors(num):
     divisors = []
     for i in range(1, num + 1):
         if num % i == 0:
             divisors.append(i)
     return divisors

#print(divisors(10))



# Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with “b”
def three_letter_words(file):
    with open(file, "r") as f:
        text = f.read()
        words = text.split()
        for word in words:
            if len(word) == 3 and word[0] == "b":
                print(word)
print(three_letter_words("text.txt"))
