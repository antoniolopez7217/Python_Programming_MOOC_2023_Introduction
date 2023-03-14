# Please write a program which asks the user for words. 
# If the user types in a word for the second time, the program should print out the number of different words typed in, and exit.


# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

my_list = []

while True:
    word = input("Word: ")
    if word in my_list:
        break
    my_list.append(word)

print(f"You typed in {len(my_list)} different words")