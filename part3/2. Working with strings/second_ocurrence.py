# Please write a program which finds the second occurrence of a substring. 
# If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap. 
# For example, in the string aaaa the second occurrence of the substring aa is at index 2.

# Some examples of expected behaviour:


# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.


# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.


# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.

word = input("Please type in a word: ")
substr = input("Please type in a substring: ")
index = word.find(substr)
substr_index = index

if index >= 0:
	word = word[index + len(substr):]
	index = word.find(substr)
	if index > 0:
		substr_index += index + len(substr)
		print(f"The second occurrence of the substring is at index {substr_index}.")
	else:
		print("The substring does not occur twice in the string.")
else:
	print("The substring does not occur twice in the string.")
		