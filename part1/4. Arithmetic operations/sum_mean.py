# Please write a program which asks the user for four numbers. 
# The program then prints out the sum and the mean of the numbers.

# The program should function as follows:

# Number 1: 2
# Number 2: 1
# Number 3: 6
# Number 4: 7
# The sum of the numbers is 16 and the mean is 4.0

sum = 0

sum += int(input("Number 1: "))
sum += int(input("Number 2: "))
sum += int(input("Number 3: "))
sum += int(input("Number 4: "))

print(f"The sum of the numbers is {sum} and the mean is {sum/4}")
