# Please write a program which asks the user to type in a sentence. 
# The program then prints out the first letter of each word in the sentence, each letter on a separate line.

# An example of expected behaviour:


# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w

sentence = input("Please type in a sentence: ")
index = 0

while index < len(sentence):
    if index == 0:
        print(sentence[index])
        index += 1
        continue
    if sentence[index - 1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1