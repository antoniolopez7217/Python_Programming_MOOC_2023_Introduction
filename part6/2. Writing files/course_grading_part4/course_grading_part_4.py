# Let's revisit the course grading project from the previous section.

# As we left if last time, the program read and processed files containing student information, completed exercises and exam results. 
# We'll add a file containing information about the course. An example of the format of the file:

# Sample data

# name: Introduction to Programming
# study credits: 5
# The program should then create two files. There should be a file called results.txt with the following contents:

# Sample data
# Introduction to Programming, 5 credits
# ======================================
# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3
# The statistics section is identical to the results printed out in part 3 of the project. 
# The only addition here is the header section.

# Additionally, there should be a file called results.csv with the following format:

# Sample data
# 12345678;pekka peloton;0
# 12345687;jaana javanainen;1
# 12345699;liisa virtanen;3
# When the program is executed, it should look like this:

# Sample output
# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# Course information: course1.txt
# Results written to files results.txt and results.csv

# That is, the program only asks for the names of the input files. All output should be written to the files. The user will only see a message confirming this.

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")

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


def results_txt(student_names, student_exercises, student_exams, course_info):
	with open(course_info) as new_file:
		info = []
		for line in new_file:
			line = line.replace("\n", "")
			parts = line.split(": ")
			info.append(parts[1])
	content = []
	content.append(f"{info[0]}, {info[1]} credits\n")			
	content.append("======================================\n")
	content.append(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
	for id, name in student_names.items():
		if id in student_exercises:
			grade = calculate_grade(sum(student_exercises[id]), sum(student_exams[id]))
			full_name = f"{name[0]} {name[1]}"
			content.append(f"{full_name:30}{grade[0]:<10}{grade[1]:<10}{grade[2]:<10}{grade[3]:<10}{grade[4]:<10}\n")
	with open("results.txt", "w") as my_file:
		for item in content:
			my_file.write(item)

def results_csv(student_names, student_exercises, student_exams):
	content = []
	for id, name in student_names.items():
		if id in student_exercises:
			grade = calculate_grade(sum(student_exercises[id]), sum(student_exams[id]))
			full_name = f"{name[0]} {name[1]}"
			content.append(f"{id};{full_name};{grade[4]}\n")
	with open("results.csv", "w") as my_file:
		for item in content:
			my_file.write(item)


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
results_txt(student_names, student_exercises, student_exams, course_info)
results_csv(student_names, student_exercises, student_exams)
