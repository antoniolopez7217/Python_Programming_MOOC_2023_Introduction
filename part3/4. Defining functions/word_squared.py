# Please write a function named squared, which takes a string argument and an integer argument, 
# and prints out a square of characters as specified by the examples below.

# squared("ab", 3)
# print()
# squared("aybabtu", 5)


# aba
# bab
# aba

# aybab
# tuayb
# abtua
# ybabt
# uayba

def squared(string, length):
	i = 0
	start = 0
	row = string * (length**2)

	while i < length:
		print(row[start:start + length])
		start += length
		i += 1
