# Please write a function named same_chars, which takes one string and two integers as arguments. 
# The integers refer to indexes within the string. The function should return True if the two characters 
# at the indexes specified are the same. 
# Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

# Some examples of how the function is used:

# # same characters m and m
# print(same_chars("programmer", 6, 7)) # True

# # different characters p and r
# print(same_chars("programmer", 0, 4)) # False

# # the second index is not within the string
# print(same_chars("programmer", 0, 12)) # False

def same_chars(string, index1, index2):
    if index1 >= len(string) or index2 >= len(string):
        return False
    if string[index1] == string[index2]:
        return True
    return False
