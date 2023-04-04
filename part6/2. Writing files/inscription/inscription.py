# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user. 
# Please see the example below.

# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txt would be

# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

name = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")