# Please write a program which asks the user for a temperature in degrees Fahrenheit, 
# and then prints out the same in degrees Celsius. 
# If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Two examples of expected behaviour:

# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!

temp_f = int(input("Please type in a temperature (F): "))
temp_g = (temp_f - 32)/1.8

print(f"{temp_f} degrees Fahrenheit equals {temp_g} degrees Celsius")
if temp_g < 0:
    print("Brr! It's cold in here!")

