# Let's expand the program created in the previous exercise. 
# Now also the exam points awarded to each student are contained in a CSV file. 
# The contents of the file follow this format:

# id;e1;e2;e3
# 12345678;4;1;4
# 12345687;3;5;3
# 12345699;10;2;2

# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. 
# Then the program should process the files and print out a grade for each student.

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# pekka peloton 0
# jaana javanainen 1
# liisa virtanen 3

# Each completed exercise is counted towards exercise points, so that completing at least 10 % of the total exercices awards 1 point, 
# completing at least 20 % awards 2 points, etc. Completing all 40 exercises awards 10 points. The number of points awarded is always an integer number.

# The final grade for the course is determined based on the sum of exam and exercise points according to the following table:

# exam points + exercise points	grade
# 0-14	0 (fail)
# 15-17	1
# 18-20	2
# 21-23	3
# 24-27	4
# 28-	5


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")


def create_dict(file):
	new_dict = {}
	with open(file) as new_file:
		for line in new_file:
			line = line.strip()
			parts = line.split(";")
			if parts[0] == "id":
				continue
			new_dict[parts[0]] = []
			for item in parts[1:]:
				if item.isdigit():
					new_dict[parts[0]].append(int(item))
				else:
					new_dict[parts[0]].append(item)
	return new_dict

def comb_dict(student_names, student_exercises, student_exams):
	for id, name in student_names.items():
		if id in student_exercises:
			grade = calculate_grade(sum(student_exercises[id]), sum(student_exams[id]))
			print(f"{name[0]} {name[1]} {grade}")

def calculate_grade(exercises, exam_points):
	point_exerc = int((exercises/40) * 10)
	total_points = point_exerc + exam_points
	grade = 5
	if total_points <= 14:
		grade = 0
	elif total_points <= 17:
		grade = 1
	elif total_points <= 20:
		grade = 2
	elif total_points <= 23:
		grade = 3
	elif total_points <= 27:
		grade = 4
	return grade	

student_names = create_dict(student_info)
student_exercises = create_dict(exercise_data)
student_exams = create_dict(exam_points)
comb_dict(student_names, student_exercises, student_exams)
