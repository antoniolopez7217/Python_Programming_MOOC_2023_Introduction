# Please write a function named sum_of_positives, which takes a list of integers as its argument. 
# The function returns the sum of the positive values in the list.

# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)

# The result is 9

def sum_of_positives(my_list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    return sum