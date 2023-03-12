# Please write a function named greatest_number, which takes three arguments. 
# The function returns the greatest in value of the three.

# An example of how the function is used:

# print(greatest_number(3, 4, 1)) # 4
# print(greatest_number(99, -4, 7)) # 99
# print(greatest_number(0, 0, 0)) # 0

def greatest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z
