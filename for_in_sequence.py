for number in[1,5,7,4,5,6,9,8,7,5,4,4]:
    print(number)

    pass


for name in ["Drazen", "harvey","john"]:
    print(name)


teacher = {
    "name":"Drazen",
    "age": 38,
    "height": 1.83
}

student = {
    "name":"harvey",
    "age": 10,
    "height": 1.5 
}

for key, value in student.items():
    print(f"student {key} => {value}")
    pass


subjects = {
    "math" : 10,
    "biology":0,
    "technology":10,
    "chinese":0,

}
for key, value in subjects.items():
    print(f"grade {key} : {value}")
    pass