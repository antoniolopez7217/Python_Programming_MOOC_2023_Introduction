# Please write a function named most_common_character, which takes a string argument. 
# The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears first in the string should be returned.
# 
# An example of expected behaviour:
# 
# first_string = "abcdbde"
# print(most_common_character(first_string))
# 
# second_string = "exemplaryelementary"
# print(most_common_character(second_string))
# 
# b
# e

def most_common_character(my_string):
    number = 0
    char = ""
    for i in my_string:
        if my_string.count(i) > number:
            char = i
            number = my_string.count(i)
    return char