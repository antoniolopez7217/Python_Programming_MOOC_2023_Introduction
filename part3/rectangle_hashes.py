# Please modify the previous program so that it also asks for the height, 
# and prints out a rectangle of hash characters accordingly.


# Width: 10
# Height: 3
# ##########
# ##########
# ##########

width = int(input("Width: "))
height = int(input("Height: "))
index = 0

while index < height:
    print("#" * width)
    index += 1
