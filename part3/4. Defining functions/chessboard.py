# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. 
# The function takes an integer argument, which specifies the length of the side of the board. 
# See the examples below for details:

# chessboard(3)
# print()
# chessboard(6)

# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101

def chessboard(length):
	row = 0
	initial = 1
	while row < length:
		column = 0
		val_col = initial
		while column < length:
			print(val_col, end="")
			if val_col == 1:
				val_col = 0
			else:
				val_col = 1
			column += 1
		if initial == 1:
			initial = 0
		else:
			initial = 1
		print()
		row += 1


			
