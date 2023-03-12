# Please write a program which asks the user to type in a number. 
# The program then prints out the positive integers between 1 and the number itself, 
# alternating between the two ends of the range as in the examples below.


# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3


# Please type in a number: 6
# 1
# 6
# 2
# 5
# 3
# 4

number = int(input("Please type in a number: "))

index = 1

while index <= number:
    if index == number:
        print(number)
        break
    print(index)
    print(number)
    index += 1
    number -= 1
