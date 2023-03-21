# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. 
# The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. 
# Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. 
# If all contain each of the numbers 1 to 9 at most once, the function returns True. 
# If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. 
# These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]

# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]

# print(sudoku_grid_correct(sudoku2))

# False
# True

def row_correct(sudoku: list, row_no: int):
	numbers = "123456789"
	for num in numbers:
		if sudoku[row_no].count(int(num)) > 1:
			return False
	return True

def column_correct(sudoku: list, column_no: int):
	numbers = []
	for row in sudoku:
		if row[column_no] == 0:
			continue
		if row[column_no] in numbers:
			return False
		numbers.append(row[column_no])
	return True

def block_correct(sudoku: list, row_no: int, column_no: int):
	numbers = []
	index_row = row_no
	while index_row < row_no + 3:
		index_col = column_no
		while index_col < column_no + 3:
			if sudoku[index_row][index_col] > 0 and sudoku[index_row][index_col] in numbers:
				return False
			numbers.append(sudoku[index_row][index_col])
			index_col += 1
		index_row += 1
	return True

def sudoku_grid_correct(sudoku: list):
	for i in range(9):
		if not row_correct(sudoku, i):
			return False
		if not column_correct(sudoku, i):
			return False
	for row in range(0, 9, 3):
		for col in range(0, 9, 3):
			if not block_correct(sudoku, row, col):
				return False
	return True

