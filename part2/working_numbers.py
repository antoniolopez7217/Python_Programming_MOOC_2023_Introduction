# Pre-task
# Please write a program which asks the user for integer numbers. 
# The program should keep asking for numbers until the user types in zero.

# Please type in integer numbers. Type in 0 to finish.
# Number: 5
# Number: 22
# Number: 9
# Number: -2
# Number: 0

# Part 1: Count
# After reading in the numbers the program should print out how many numbers were typed in. 
# The zero at the end should not be included in the count.

# You will need a new variable here to keep track of the numbers typed in.

# ... the program asks for numbers
# Numbers typed in 4

# Part 2: Sum
# The program should also print out the sum of all the numbers typed in. 
# The zero at the end should not be included in the calculation.

# The program should now print out the following:

# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34

# Part 3: Mean
# The program should also print out the mean of the numbers. 
# The zero at the end should not be included in the calculation. 
# You may assume the user will always type in at least one valid non-zero number.

# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5

# Part 4: Positives and negatives
# The program should also print out statistics on how many of the numbers were positive and how many were negative. 
# The zero at the end should not be included in the calculation.

# ... the program asks for numbers
# Numbers typed in 4
# The sum of the numbers is 34
# The mean of the numbers is 8.5
# Positive numbers 3
# Negative numbers 1

print("Please type in integer numbers. Type in 0 to finish.")

count = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    sum += number
    if number == 0:
        break
    if number > 0:
        positive += 1
    else:
        negative += 1
    count += 1

print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

