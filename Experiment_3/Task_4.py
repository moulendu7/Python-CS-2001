def highest_grade(students):
    highest_student = ""
    highest_mark = -1
    for name in students:
        if students[name] > highest_mark:
            highest_mark = students[name]
            highest_student = name
    return highest_student

data = {
    "Amit": 85,
    "Riya": 92,
    "Kabir": 78,
    "Sneha": 95,
    "John": 88
}
print(highest_grade(data))