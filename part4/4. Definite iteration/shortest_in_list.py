# Please write a function named shortest, which takes a list of strings as its argument. 
# The function returns whichever of the strings is the shortest. If more than one are equally short, 
# the function can return any of the shortest strings (there will be no such situation in the tests). 
# You may assume there will be no empty strings in the list.

# my_list = ["first", "second", "fourth", "eleventh"]

# result = shortest(my_list)
# print(result)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = shortest(my_list)
# print(result)

# first
# tim

def shortest(my_list):
    length = len(my_list[0])
    short = ""
    for i in my_list:
        if len(i) < length:
            short = i
            length = len(i)
    return short

