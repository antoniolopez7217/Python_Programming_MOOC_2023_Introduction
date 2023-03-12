# Please change the program from the previous exercise so that the user gets to input also the base which is multiplied.

# Upper limit: 27
# Base: 3
# 1
# 3
# 9
# 27

# Upper limit: 1234567
# Base: 10
# 1
# 10
# 100
# 1000
# 10000
# 100000
# 1000000

# Please don't use the value True as the condition of your while loop in this exercise!

limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1

while number <= limit:
    print(number)
    number *= base
