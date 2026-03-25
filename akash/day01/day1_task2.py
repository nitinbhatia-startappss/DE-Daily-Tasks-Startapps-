arr = [1,2,2,3,4,4]

result = []

for num in arr:
    if num not in result:
        result.append(num)

print(result)