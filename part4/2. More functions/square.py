# Please write a function named square, which prints out a square of characters, and takes two arguments. 
# The first parameter specifies the length of the side of the square. 
# The second parameter specifies the character used to draw the square.

# The function should call the function line from the exercise above for the actual printing out. 
# Copy your solution to that exercise above the code for this exercise. 
# Please don't change anything in the line function.

# Some examples:

# square(5, "*")
# print()
# square(3, "o")

# *****
# *****
# *****
# *****
# *****

# ooo
# ooo
# ooo

def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)

def square(size, character):
    index = 0
    while index < size:
        line(size, character)
        index += 1
