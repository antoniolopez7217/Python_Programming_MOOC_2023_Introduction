# Please write a program which asks the user for a string and 
# then prints it out so that exactly 20 characters are displayed. 
# If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

# You may assume the input string is at most 20 characters long.


# Please type in a string: python

# **************python

# Please type in a string: alongerstring

# *******alongerstring

# Please type in a string: averyverylongstring

# *averyverylongstring

string = input("Please type in a string:")
chars = 20 - len(string)

print("*" * chars, end="")
print(string)