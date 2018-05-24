import string, random
print(string.ascii_letters)
print(string.ascii_lowercase)


print(random.choice('pull letter from here'))
print(random.choice('string.ascii_lowercase'))
print('-')

#function to create a name using 5 random letters and returns the concatonation of them
def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5

    return (name)

print(generator()) #creates a 'name' from randomly generated letters









