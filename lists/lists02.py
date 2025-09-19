math_grades = [5,4,1,5,3,2,4,3,5,4,5,4,2,4,5,3,4,5,4]

print(f"you have {len(math_grades)} math grades")

sum = 0
average = 0,

for grade in math_grades:
    sum = sum +grade
    pass

print(f"your average grade is { (sum/len(math_grades))}")