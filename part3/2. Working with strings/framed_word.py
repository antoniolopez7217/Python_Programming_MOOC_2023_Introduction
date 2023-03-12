# Please write a program which asks the user for a string and then prints out a 
# frame of * characters with the word in the centre. The width of the frame should 
# be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in 
# either of the two possible centre locations.


# Word: testing

# ******************************
# *          testing           *
# ******************************

# Word:python

# ******************************
# *           python           *
# ******************************

word = input("Word: ")
spaces = 28 - len(word)

print("*" * 30)
print("*", end="")
print(" " * int((spaces/2)), end="")
print(word, end="")
if len(word) % 2 == 0:
	print(" " * int((spaces/2)), end="")
else:
	print(" " * int((spaces/2 + 1)), end="")
print("*")
print("*" * 30)
