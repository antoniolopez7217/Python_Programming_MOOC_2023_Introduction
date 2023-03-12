# Please write a program which asks the user for a year, and prints out the next leap year.

# Year: 2023
# The next leap year after 2023 is 2024

# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

# Year: 2024
# The next leap year after 2024 is 2028


year = int(input("Year: "))

year_leap = year + 1

while True:
	if year_leap % 4 != 0:
		year_leap += 1
	elif year_leap % 4 == 0 and year_leap % 100 == 0 and year_leap % 400 != 0:
		year_leap += 1
	else:
		break

print(f"The next leap year after {year} is {year_leap}")