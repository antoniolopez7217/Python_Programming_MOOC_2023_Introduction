# Please write a function named triangle, which draws a triangle of hashes, and takes one argument. 
# The triangle should be as tall and as wide as the value of the argument.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. 
# Please don't change anything in the line function.

# Some examples:

# triangle(6)
# print()
# triangle(3)

# #
# ##
# ###
# ####
# #####
# ######

# #
# ##
# ###

def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def triangle(size):
    index = 1
    while index <= size:
        line(index, "#")
        index += 1
