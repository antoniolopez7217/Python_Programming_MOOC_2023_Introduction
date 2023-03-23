# Please write an improved version of the phone book application. 
# Each entry should now accommodate multiple phone numbers. 
# The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.


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
# 040-5466745
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

def add(contacts):
	name = input("name: ")
	number = input("number: ")
	if not name in contacts:
		contacts[name] = []
	contacts[name].append(number)
	print("ok!")

def search(contacts):
	name_search = input("name: ")
	if name_search in contacts:
		for number in contacts[name_search]:
			print(number)
	else:
		print("no number")
	
def main():
	contacts = {}

	while True:
		command = int(input("command (1 search, 2 add, 3 quit): "))
		if command == 1:
			search(contacts)
		elif command == 2:
			add(contacts)
		else:
			print("quitting...")
			break

main()
