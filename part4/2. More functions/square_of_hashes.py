# Please write a function named square_of_hashes, which draws a square of hash characters. 
# The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. 
# Please don't change anything in the line function.

# Some examples:

# square_of_hashes(5)
# print()
# square_of_hashes(3)

# #####
# #####
# #####
# #####
# #####

# ###
# ###
# ###

def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def square_of_hashes(size):
    index = 0
    while index < size:
        line(size, "#")
        index += 1
