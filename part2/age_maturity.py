# Please write a program which asks the user for their age. 
# The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

# Some examples of expected behaviour:

# How old are you? 12
# You are not of age!

# How old are you? 32
# You are of age!

age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")