#Q sort the list based on specific key in dictionary
# list of dictionaries
students = [
    {"name": "Rahul", "age": 21},
    {"name": "Amit", "age": 19},
    {"name": "Neha", "age": 22}
]

# sorting list based on 'age' key
sorted_students = sorted(students, key=lambda x: x["age"])

print(sorted_students)
