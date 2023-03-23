# Please write a function named dict_of_numbers(), which returns a new dictionary. 
# The dictionary should have the numbers from 0 to 99 as its keys. 
# The value attached to each key should be the number spelled out in words. 
# Please have a look at the example below:

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])

# two
# eleven
# forty-five
# ninety-nine
# zero

# NB: Please don't formulate each spelled out number by hand. 
# Figure out how you can use loops and dictionaries in your solution.

def dict_of_numbers():
	numbers = {}
	first_19 = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
	for i in range(20):
		numbers[i] = first_19[i]
	dec = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
	index = -1
	dec_number = 10
	for i in range(20,100):
		if i % 10 == 0:
			index += 1
			dec_number += 10
			numbers[i] = dec[index]
		else:
			numbers[i] = f"{dec[index]}-{numbers[i % dec_number]}"

	return numbers

