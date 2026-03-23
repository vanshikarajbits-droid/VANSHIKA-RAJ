students = {
    "Vanshika": 85,
    "Rahul": 90,
    "Aman": 78
}

students["Riya"] = 88

students["Aman"] = 80

for name, marks in students.items():
    print(name, ":", marks)
