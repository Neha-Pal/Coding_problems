# Grading Students
# Every student receives a grade in range from 0 to 100
# Any grade less than 40 is a failing grade

# input - 
# 73
# 67
# 38
# 33

# output - 
# 75
# 67
# 40
# 33

def output(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            diff = 5 - (grade % 5)
            if diff < 3:
                grade += diff
        rounded_grades.append(grade)
    return rounded_grades
grades = [73, 67, 38, 33]
print(output(grades))