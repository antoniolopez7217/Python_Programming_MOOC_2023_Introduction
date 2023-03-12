# Please write a function named spruce, which takes one argument. 
# The function prints out the text a spruce!, and the a spruce tree, 
# the size of which is specified by the argument.

# Calling spruce(3) should print out


# a spruce!
#   *
#  ***
# *****
#   *
# Calling spruce(5) should print out


# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *

# NB: to the left of the spruce there should be exactly the right amount of whitespace. 
# If the shape of the spruce looks correct, but the left edge of the tree is not touching 
# the left edge of the text area in the terminal, the tests will not accept the solution.

def spruce(size):
    print("a spruce!")
    blank_spaces = size - 1
    stars = 1
    while blank_spaces >= 0:
        print(" " * blank_spaces, end="")
        print("*" * stars)
        blank_spaces -= 1
        stars += 2
    print(" " * (size - 1), end="")
    print("*")
