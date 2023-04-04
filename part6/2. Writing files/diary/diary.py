# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. 
# When the program is executed, it should first read any entries already in the file.

# NB: the automatic tests for this exercise will change the contents of the file. 
# If you want to keep its contents, first make a copy of the file under a different name.

# The program should work as follows:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# When the program is executed for the second time, this should happen:

# Sample output
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

def add(filename):
	entry = input("Diary entry: ")
	with open(filename, "a") as my_file:
		my_file.write(f"{entry}\n")
		print("Diary saved")

def read_diary(filename):
	print("Entries:")
	with open(filename) as my_file:
		for line in my_file:
			line = line.replace("\n", "")
			print(line)

def main():
	filename = "diary.txt"
	while True:
		print("1 - add an entry, 2 - read entries, 0 - quit")
		action = int(input("Function: "))
		if action == 1:
			add(filename)
		elif action == 2:
			read_diary(filename)
		else:
			print("Bye now!")
			break

main()