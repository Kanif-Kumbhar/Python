#5.	Write a program to input percentage marks of a student and find the grade as per following criterion:
# Marks           Grade
# >=90             A
# 75-90            B 
# 60-75            C     
# Below 60         D

def calculate_grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid marks"
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'D'

marks = float(input("Enter the percentage marks: "))

if 0 <= marks <= 100:
    grade = calculate_grade(marks)
    print(f"Your grade is: {grade}")
else:
    print("Please enter a valid percentage between 0 and 100.")

    
