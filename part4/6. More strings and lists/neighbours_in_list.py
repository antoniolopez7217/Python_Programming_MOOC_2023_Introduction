# Given a list of integers, let's decide that two consecutive items in the list are neighbours 
# if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

# An example function call:

# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))

# 4

def longest_series_of_neighbours(my_list):
    max_length = 0
    length = 1
    last_item = my_list[0]
    for item in my_list:
        if (item - last_item) == 1 or (item - last_item) == -1:
            length += 1
            if length > max_length:
                max_length = length
        else:
            length = 1
        last_item = item
    return max_length

