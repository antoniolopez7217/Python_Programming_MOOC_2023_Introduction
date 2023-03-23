# Please write a phone book application. It should work as follows:


# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

# As you can see above, each name can be attached to a single number only. 
# If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

contacts = {}

while True:
	command = int(input("command (1 search, 2 add, 3 quit): "))
	if command == 1:
		name_search = input("name: ")
		number = ""
		for key, value in contacts.items():
			if key == name_search:
				number += value
				print(number)
		if not number:
			print("no number")
	elif command == 2:
		name = input("name: ")
		number = input("number: ")
		contacts[name] = number
		print("ok!")
	else:
		print("quitting...")
		break
	