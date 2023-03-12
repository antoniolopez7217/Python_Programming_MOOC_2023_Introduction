# Please write a program which asks for the user's age. 
# If the age is not plausible, that is, it is under 5 or something that can't be an actual human age, the program should print out a comment.

# Have a look at the examples of expected behaviour below to figure out which comment is applicable in each case.

# What is your age? 13
# Ok, you're 13 years old

# What is your age? 2
# I suspect you can't write quite yet...

# What is your age? -4
# That must be a mistake

age = int(input("What is your age? "))

if age >= 5:
	print(f"Ok, you're {age} years old")
elif 0 <= age < 5:
    print("I suspect you can't write quite yet...") 
else:
    print("That must be a mistake")

     


