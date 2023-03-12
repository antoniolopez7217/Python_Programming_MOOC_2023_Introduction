# Please write a program which asks the user to type in a string. 
# The program then prints out all the substrings which begin with the first character, 
# from the shortest to the longest. Have a look at the example below.


# Please type in a string: test
# t
# te
# tes
# test

string = input("Please type in a string: ")
index = 1

while index <= len(string):
    print(string[:index])
    index += 1


