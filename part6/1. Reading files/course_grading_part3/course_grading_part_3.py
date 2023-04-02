# This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3

# Each row contains the information for a single student. 
# The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, 
# and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

# You might find the f-strings covered in part 4 useful here.

# F-strings differentiate between strings and numbers when it comes to justifying columns:

# word = "python"
# print(f"{word:10}continues")
# print(f"{word:>10}continues")

# python    continues
#     pythoncontinues

# As you can see above, by default strings are justified to the left edge of the area specified for them. The > symbol can be used to justify to the right edge.

# With number values the logic is reversed:

# number = 42
# print(f"{number:10}continues")
# print(f"{number:<10}continues")

#         42continues
# 42        continues

# With numbers the default behaviour is to justify to the right edge. The symbol < can be used to justify to the left edge.

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
	print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
	for id, name in student_names.items():
		if id in student_exercises:
			grade = calculate_grade(sum(student_exercises[id]), sum(student_exams[id]))
			full_name = f"{name[0]} {name[1]}"
			print(f"{full_name:30}{grade[0]:<10}{grade[1]:<10}{grade[2]:<10}{grade[3]:<10}{grade[4]:<10}")

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
	return [exercises, point_exerc, exam_points, total_points, grade]	

student_names = create_dict(student_info)
student_exercises = create_dict(exercise_data)
student_exams = create_dict(exam_points)
comb_dict(student_names, student_exercises, student_exams)
