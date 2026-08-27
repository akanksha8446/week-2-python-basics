students = [
    ("Akanksha", 85),
    ("Rahul", 72),
    ("Priya", 91),
    ("Sneha", 78),
    ("Amit", 88)
]
print("Original List:")
print(students)
students.sort(key=lambda student: student[1])
print("\nSorted by Marks:")
for student in students:
    print(student[0], "-", student[1])
