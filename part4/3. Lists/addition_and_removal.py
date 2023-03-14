# Please write a program which asks the user to choose between addition and removal. 
# Depending on the choice, the program adds an item to or removes an item from the end of a list. 
# The item that is added must always be one greater than the last item in the list. 
# The first item to be added must be 1.

# The list is printed out in the beginning and after each operation. 
# Have a look at the example execution below:


# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!

# You may assume that, if the list is empty, there will not be an attempt to remove items.

my_list = []

while True:
    print(f"The list is now {my_list}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == "d":
        my_list.append(len(my_list) + 1)
    elif action == "r":
        my_list.remove(len(my_list))
    elif action == "x":
        print("Bye!")
        break