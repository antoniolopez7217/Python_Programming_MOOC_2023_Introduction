# Please write a program which asks the user for two numbers and an operation. 
# If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 
# If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

number1 = int(input("NUmber 1: "))
number2 = int(input("NUmber 2: "))
operation = input("Operation: ")

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2 }")
elif operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2 }")
elif operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2 }")