# Please write a program which first asks the user for the number of items to be added. 
# Then the program should ask for the given number of values, one by one, and add them 
# to a list in the order they were typed in. Finally, the list is printed out.

# An example of expected behaviour:

# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]

items = int(input("How many items: "))
my_list = []
index = 1
while index <= items:
    value = int(input(f"Item {index}: "))
    my_list.append(value)
    index += 1

print(my_list)
    