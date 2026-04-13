#Simple map reduce program

from collections import defaultdict

documents = [
    "apple banana apple",
    "banana orange apple",
    "orange orange banana"
]

#map phase

def mapper(document):
    pairs = []
    for word in document.split():
        pairs.append((word, 1))
    return pairs

mapped = []
for doc in documents:
    mapped.extend(mapper(doc))

print("After Map: ", mapped)

# shuffle and sort phase

shuffled = defaultdict(list)
for key,value in mapped:
    shuffled[key].append(value)

print("After shuffle & sort: ", dict(shuffled))


#Reduce phase

def reducer(key,values):
    return (key, sum(value))

result = []
for key, value in shuffled.items():
    result.append(reducer(key,value))

print("FInal output: ",result)
