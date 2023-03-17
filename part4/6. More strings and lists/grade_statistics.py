# In this exercise you will write a program for printing out grade statistics for a university course.

# The program asks the user for results from different students on the course. 
# These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.

# Exam points are integers between 0 and 20. 
# The number of exercises completed is an integer between 0 and 100.

# The program kees asking for input until the user types in an empty line. You may assume all lines contain valid input, 
# which means that there are two integers on each line, or the line is empty.

# And example of how the data is typed in:

# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:

# When the user types in an empty line, the program prints out statistics. 
# They are formulated as follows:

# The exercises completed are converted into exercise points, so that completing at least 
# 10% of the exercises grants one point, 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. 
# The number of exercise points granted is an integer value, rounded down.

# The grade for the course is determined based on the following table:

# exam points + exercise points	grade
# 0–14	0 (i.e. fail)
# 15–17	1
# 18–20	2
# 21–23	3
# 24–27	4
# 28–30	5

# There is also an exam cutoff threshold. 
# If a student received less than 10 points from the exam, they automatically fail the course, regardless of their total number of points.

# With the example input from above the program would print out the following statistics:

# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *

# Floating point numbers should be printed out with one decimal precision.

# NB: this exercise doesn't ask you to write any specific functions, so you should not place any code within an 
# if __name__ == "__main__" block. If any functionality in your program is e.g. in the main function, 
# you should include the code calling this function normally, and not contain it in an if block like in the exercises which specify certain functions.

# Hint:

# The user input in this program consists of lines with two integer values:

# Exam points and exercises completed: 15 87

# You have to first split the input line in two and then convert the sections into integers with the int function.
# Splitting the input can be achieved in the same way as in the exercise First, second and last words, but there is a simpler way as well. 
# The string method split will chop the input up nicely. You will find more information by searching for python string split online.


def input_user():
    results = []
    while True:
        ex_points = input("Exam points and exercises completed: ")
        if ex_points == "":
            break
        results.append(ex_points)
    return results

def convert_res(results):
    ex_points = []
    exercises = []
    for item in results:
        item = item.split()
        ex_points.append(int(item[0]))
        exercises.append(int(item[1]))
    return [ex_points, exercises]

def statistics(ex_points, exercises):
    points = []
    grade = []
    index = 0
    for i in exercises:
        points.append(i//10 + ex_points[index])
        if ex_points[index] < 10:
            grade.append(0)
        else:
            grade.append(calculate_grade(points[index]))
        index += 1
    return [points, grade]
            
def calculate_grade(points):
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    return 5

def print_results(points, grades):
    print("Statistics:")
    print(f"Points average: {sum(points)/len(points):.1f}")
    pass_perc = ((len(grades) - grades.count(0))/len(grades)) * 100
    print(f"Pass percentage: {pass_perc:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {(grades.count(i)) * '*'}")

def main():
    results = input_user()
    int_results = convert_res(results)
    point_grade = statistics(int_results[0], int_results[1])
    print_results(point_grade[0], point_grade[1])
    
main()














