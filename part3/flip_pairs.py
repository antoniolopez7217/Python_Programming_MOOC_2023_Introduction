# Please write a program which asks the user to type in a number. 
# The program then prints out all the positive integer values from 1 up to the number. 
# However, the order of the numbers is changed so that each pair or numbers is flipped. 
# That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.


# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5


# Please type in a number: 6
# 2
# 1
# 4
# 3
# 6
# 5

number = int(input("Please type in a number: "))

even = 2
odd = 1

while even <= number or odd <= number:
    if even <= number:
        print(even)
    if odd <= number:
        print(odd)
    even += 2
    odd += 2