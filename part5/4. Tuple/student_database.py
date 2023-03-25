# In this series of exercises you will create a simple student database. 
# Before diving in, please spend a moment reading through the instructions and thinking about what 
# sort of data structures are necessary for organising the data stored by your program.

# Part 1: adding students
# First write a function named add_student, which adds a new student to the database. 
# Also write a preliminary version of the function print_student, which prints out the information of a single student.

# These function are used as follows:

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")

# Your program should now print out

# Peter:
#  no completed courses
# Eliza:
#  no completed courses
# Jack: no such person in the database

# Part 2: adding completed courses
# Please write a function named add_course, which adds a completed course to the information of a specific student in the database. 
# The course data is a tuple consisting of the name of the course and the grade:

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")

# When some courses have been added, the information printed out changes:

# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

# Part 3:brepeating courses
# Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific 
# student's information, the grade recorded in the database should never be lowered if the course is repeated.

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")

# Peter:
#  2 completed courses:
#   Introduction to Programming 3
#   Advanced Course in Programming 2
#  average grade 2.5

# Part 4: summary of database
# Please write a function named summary, which prints out a summary based on all the information stored in the database.

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# This should print out

# students 2
# most courses completed 3 Peter
# best average grade 4.5 Eliza

def add_student(students, name):
	students[name] = {}

def add_course(students, name, course):
	if course[1] == 0:
		return
	if course[0] in students[name]:
		if course[1] > students[name][course[0]]:
			students[name][course[0]] = course[1]
	else:	
		students[name].update({course[0]:course[1]})

def summary(students):
	print(f"students {len(students)}")
	most_courses = ["", 0]
	best_average = ["", 0]
	for key, value in students.items():
		if len(value) > most_courses[1]:
			most_courses = [key, len(value)]
		avg = sum(value.values())/len(value)
		if avg > best_average[1]:
			best_average = [key, avg]
	print(f"most courses completed {most_courses[1]} {most_courses[0]} ")
	print(f"best average grade {best_average[1]} {best_average[0]} ")


def print_student(students, name):
	if name not in students:
		print(f"{name}: no such person in the database")
		return
	print(f"{name}:")
	if students[name] == {}:
		print(" no completed courses")
	else:
		print(f" {len(students[name])} completed courses:")
		values_sum = 0
		for key, value in students[name].items():
			print(f"  {key} {value}")
			values_sum += value
		print(f" average grade {values_sum / len(students[name])}")
