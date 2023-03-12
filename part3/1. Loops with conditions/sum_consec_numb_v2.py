# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation performed:

# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# You may assume the number typed in by the user is always equal to 2 or higher.


limit = int(input("Limit: "))
sum = 1
number = 1
result = f"The consecutive sum: {number}"

while sum < limit:
    number += 1
    result += f" + {number}"
    sum += number

result += f" = {sum}" 
print(result)