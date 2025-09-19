age = int(input("enter your age: "))

for i in range(age + 1):
    calender_year = 2025 - age + i
    age_in_calender_year = i
    print(f"in year {calender_year} you where {age_in_calender_year} years old")