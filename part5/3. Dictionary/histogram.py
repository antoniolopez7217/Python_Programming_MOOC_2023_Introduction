# Please write a function named histogram, which takes a string as its argument. 
# The function should print out a histogram representing the number of times each letter occurs in the string. 
# Each occurrence of a letter should be represented by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out


# a **
# b **

# while histogram("statistically") should print out


# s **
# t ***
# a **
# i **
# c *
# l **
# y *

def histogram(my_string):
    dictionary = {}
    for word in my_string:
        if word not in dictionary:
            dictionary[word] = 0
        dictionary[word] += 1
    for key, value in dictionary.items():
        print(f"{key} {value * '*'}")
