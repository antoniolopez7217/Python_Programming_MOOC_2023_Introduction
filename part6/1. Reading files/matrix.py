# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...
# Please write two functions, named matrix_sum and matrix_max. 
# Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. 
# For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program. 
# It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. 
# Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. 
# The file you are working with is always named matrix.txt.

def open_matrix():
	with open("matrix.txt") as new_file:
		matrix = []
		for line in new_file:
			int_row = []
			line = line.replace("\n","")
			line = line.split(",")
			for value in line:
				int_row.append(int(value))
			matrix.append(int_row)
	return matrix

def row_sums():
	matrix = open_matrix()
	sum_rows = []
	for row in matrix:
		sum_rows.append(sum(row))
	return sum_rows

def matrix_sum():
	row_sum = row_sums()
	return sum(row_sum)	

def matrix_max():
	matrix = open_matrix()
	max_value = matrix[0][0]
	for row in matrix:
		if max(row) > max_value:
			max_value = max(row)
	return max_value
