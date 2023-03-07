# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.

# Some examples of expected behaviour:

# Please type in the first number: 5
# Please type in another number: 3
# The greater number was: 5

# Please type in the first number:: 5
# Please type in another number: 8
# The greater number was: 8

# Please type in the first number: 5
# Please type in another number: 5
# The numbers are equal!

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in another number: "))

if number1 > number2:
    print(f"The greater number was: {number1}")
elif number1 < number2:
    print(f"The greater number was: {number2}")
else:
    print("The numbers are equal!")

