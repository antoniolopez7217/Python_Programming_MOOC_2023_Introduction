# Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. 
# Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main function which asks the user to type in words until they type in a palindrome:


# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!

# NB:, the main function should not be within an if __name__ == "__main__": block

def palindromes(string):
	return string == string[::-1]

def input_string():
	while True:
		string = input("Please type in a palindrome: ") 
		if palindromes(string):
			print(f"{string} is a palindrome!")
			break
		print("that wasn't a palindrome")

input_string()