#Q1 --> Given a list of dictionaries, sort it based on a specific key.
people = [
    {"name": "Nitin", "age": 26},
    {"name": "Aman", "age": 22},
    {"name": "Rohit", "age": 24}
]
result = sorted(people,key = lambda x: x["age"])
print(result)


#Q2 --> sort by name 
people = [
    {"name": "Nitin", "age": 26},
    {"name": "Aman", "age": 22},
    {"name": "Rohit", "age": 24}
]
result = sorted(people,key=lambda x: x['name'])
print(result)

#Q3 --> Sort by multiple keys
data = [
    {"name": "Nitin", "age": 26},
    {"name": "Aman", "age": 26},
    {"name": "Riya", "age": 24}
]
result = sorted(people, key=lambda x: (x['age'], x['name']))
print(result)


#Q4 --> Handle missing keys
data = [
    {"name": "Nitin", "age": 26},
    {"name": "Aman"},
    {"name": "Riya", "age": 24}
]
sorted_data = sorted(data, key=lambda x: x.get("age", 0))
print(sorted_data)
