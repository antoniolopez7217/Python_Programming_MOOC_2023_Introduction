# Please write a function named distinct_numbers, which takes a list of integers as its argument. 
# The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]

def distinct_numbers(my_list):
    dist_list = []
    for i in sorted(my_list):
        if i not in dist_list:
            dist_list.append(i)
    return dist_list