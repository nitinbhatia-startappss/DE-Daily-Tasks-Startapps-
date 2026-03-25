import csv
import json

# -------- Create CSV file --------
csv_data = [
    ["name", "age", "city"],
    ["Akash", 22, "Bhopal"],
    ["Rahul", 23, "Indore"],
    ["Aman", 24, "Delhi"]
]

# write CSV file
with open("sample.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("sample.csv created successfully")


# -------- Create JSON file --------
json_data = [
    {"name": "Akash", "age": 22, "city": "Bhopal"},
    {"name": "Rahul", "age": 23, "city": "Indore"},
    {"name": "Aman", "age": 24, "city": "Delhi"}
]

# write JSON file
with open("sample.json", "w") as file:
    json.dump(json_data, file, indent=4)

print("sample.json created successfully")