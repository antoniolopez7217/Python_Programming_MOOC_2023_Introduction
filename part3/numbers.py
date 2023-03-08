# Please write a program which asks the user for a number. 
# The program then prints out all integer numbers greater than zero but smaller than the input.

# Upper limit: 5
# 1
# 2
# 3
# 4

# Please don't use the value True as the condition of your while loop in this exercise!

limit = int(input("Upper limit: "))
number = 1

while number < limit:
    print(number)
    number += 1