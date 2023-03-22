# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. 
# The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# The following matrix

# 1 2 3
# 4 5 6
# 7 8 9

# transposed looks like this:

# 1 4 7
# 2 5 8
# 3 6 9

# The function should not have a return value. 
# The matrix should be modified directly through the reference.

def transpose(matrix: list):
	copy_matrix = []
	for row in matrix:
		copy_matrix.append(row[:])
	print(copy_matrix)
	for row in range(len(copy_matrix)):
		for col in range(len(copy_matrix[0])):
			matrix[col][row] = copy_matrix[row][col]
