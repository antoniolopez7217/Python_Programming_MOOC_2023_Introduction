# The file solutions.csv contains some solutions to mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...
# As you can see above, on each line the format is name_of_student;problem;result. 
# All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.csv
# Using the example above, the file correct.csv would contain the lines

# Arto;2+5;7
# Pekka;3-2;1
# Pekka;5+5;10
# The other two would be in the file incorrect.csv.

# Please write the lines in the same order as they appear in the original file. Do not change the original file.

# NB: the function should have the exact same result, no matter how many times it is called. 
# That is, it shouldn't matter if the function is called once

# filter_solutions()
# or multiple times in a row

# filter_solutions()
# filter_solutions()
# filter_solutions()
# filter_solutions()
# After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.

def solution(operation, result):
	if "+" in operation:
		sol = operation.split("+")
		if int(sol[0]) + int(sol[1]) == int(result):
			return True
		return False
	else:
		sol = operation.split("-")
		if int(sol[0]) - int(sol[1]) == int(result):
			return True
		return False

def write_sol(filename, result :list):
	with open(filename, "w") as my_file:
		for item in result:
			my_file.write(item)

def filter_solutions():
	correct = []
	incorrect = []
	with open("solutions.csv") as my_file:
		for line in my_file:
			data = line.split(";")
			if solution(data[1], data[2]):
				correct.append(line)
			else:
				incorrect.append(line)
	write_sol("correct.csv", correct)
	write_sol("incorrect.csv", incorrect)

