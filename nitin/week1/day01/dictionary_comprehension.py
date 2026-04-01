# Q1 --> Squares dictionary
#ans -->

x = {x: x**2 for x in range(1,11)}
print(x)

#Q2 --> Even numbers only
even  = {x: x**2 for x in range(1,11) if x%2==0}
print(even)

#Q3 --> Convert list to dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]

dict = list(zip(keys,values))
print(dict)


#Q4 --> String length mapping
words = ["apple", "banana", "kiwi"]
result = {word: len(word) for word in words }
print(result)


#Q5 --> Swap keys and values
d = {"a":1, "b":2, "c":3}
swapped = {v: k for k, v in d.items()}
print(swapped)


#Q6 --> Conditional Transformation
nums = [1,2,3,4,5]
result = {x: (x**2 if x % 2 == 0 else x**3) for x in nums}
print(result)


#Q7 --> Filter dictionary
d = {"a":10, "b":5, "c":20}
result = {k: v for k, v in d.items() if v > 10}
print(result )


#Q9 --> Count characters in string
s = "aabbccc"
result = {ch: s.count(ch) for ch in set(s)}
print(result)
