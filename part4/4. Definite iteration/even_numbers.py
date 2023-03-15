# Please write a function named even_numbers, which takes a list of integers as an argument. 
# The function returns a new list containing the even numbers from the original list.

# my_list = [1, 2, 3, 4, 5]
# new_list = even_numbers(my_list)
# print("original", my_list)
# print("new", new_list)

# original [1, 2, 3, 4, 5]
# new [2, 4]

def even_numbers(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list