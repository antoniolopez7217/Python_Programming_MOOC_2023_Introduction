# This final exercise in this part is a relatively demanding problem solving task. 
# It can be solved in many different ways. 
# Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples below. 
# You may assume there will be at most 26 layers.

# Layers: 3

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

# Layers: 4

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))

left = ""
right = ""
next_char = layers - 1
chars_between = 2 * layers - 1
while next_char >= 1:
    left = left + alphabet[next_char]
    right = alphabet[next_char] + right
    chars_between -= 2
    print(left + alphabet[next_char] * chars_between + right)
    next_char -= 1
while next_char <= layers - 1:
    print(left + alphabet[next_char] * chars_between + right)
    left = left[:-1]
    right = right[1:]
    chars_between += 2
    next_char += 1