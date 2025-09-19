# START

# DISPLAY "Enter grades for the following subjects:"

# ASK user for Maths grade → store in maths_grade
# ASK user for History grade → store in history_grade
# ASK user for Physics grade → store in physics_grade
# ASK user for Biology grade → store in biology_grade
# ASK user for Physical Education grade → store in pe_grade

# CALCULATE grade_sum = maths_grade + history_grade + physics_grade + biology_grade + pe_grade
# CALCULATE average = grade_sum / 5

# IF average >= 4.75 THEN
#     DISPLAY "Congratulations, you’ll get a reward for great grades!"
# ELSE
#     DISPLAY "Unfortunately your grades are too low. Good luck next year!"
# END IF

# STOP


maths_grade = input("input your maths grade: ")
history_grade = input("input your history grade")
physics_grade = input("input your physics grade")
biology_grade = input("input your biology grade")
PE_grade = input("input your PE grade")
grade_sum = maths_grade + history_grade + physics_grade + biology_grade + PE_grade
average = grade_sum / 5
if average >= 4.75:
    print("you passed")
else:
    print("you failed")