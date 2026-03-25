#to find / print / remove duplicate elements
arr = [1, 2, 2, 3, 4, 4, 5]

unique = []
duplicates = []

for num in arr:
    if num not in unique:
        unique.append(num)
    else:
        duplicates.append(num)

print("Duplicates:", duplicates)
print("After removing duplicates:", unique)