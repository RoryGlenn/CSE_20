"""
dictionary methods

.clear() - empties the dictionary
.update() - adds a new dictionary to the dictionary
.pop() - removes a key and returns its value
.get() - return the value of a key
.keys() - returns a list of keys
.items() - returnsd a list of items
"""

# Q1
list1 = [["alice", 20, "math"]]
d1 = {}

for item in list1:
    key = item[0].lower()
    d1[key] = item

print(d1)

# Q2
d2 = {"forest": ["Forest", 21, "psychology"]}
print(d2.values())

# Q3
d1.update(d2)
print(d1)

# Q4
for item in d1.items():
    print(item, end=" ")

# Q5
for key in d1.keys():
    print(key, end=" ")
    print(d1.get(key), end=" ")

# Q6
sorted_keys = sorted(d1.keys())
print(sorted_keys)

# Q7
for key in sorted_keys:
    value = d1.pop(key)
    print(key, end=" ")  # " " is a space
    print(value, end=" ")  # " " is a space

# Q8
print(d1)

# Q9
print(d2)

# Q10
d2.clear()
print(d2)

# Q11
d = {}
print("Enter a name and a major one at a time")
name = input()
major = input()

d.update({name: major})

name = input()
major = input()

d.update({name: major})

# Q12
print(d)

# LISTS

# Q13
A = set()
for i in range(10):
    A.add(i)
print(A)

# Q14
B = {1, 2, 3}
print(B)

# Q15
print(A.difference(B))

# Q16
print(A - B)

# Q17
print(A.intersection(B))

# Q18
print(A & B)

# Q19
print(A.union(B))

# Q20
print(A | B)

# Q21
print(A.symmetric_difference(B))

# Q22
print(A.issuperset(B))

# Q23
item = B.pop()
print(item)

# Q24
item = B.remove(2)
print(item)

# Q25
print(B)

# Q26
item = B.discard(3)
print(item)

# Q27
print(B)

# Q28
print(A.isdisjoint(B))

# Q29
B.update(A)
print(B)

# Q30
B.pop()
print(A.isdisjoint(B))

# Q31
B.clear()
print(B)

# frozen sets


# Q32
fset1 = frozenset([1, 2, 3, 4, 5, 5, 5])
print(fset1)

# Q33
for item in fset1:
    print(item, end=" ")

# Q34
fset2 = frozenset([1, 10])

for item in fset2:
    if item in fset1:
        print(f"{item} is in both sets.", end=" ")  # " " is a space
    else:
        print(f"{item} is only in set 2.", end=" ")  # " " is a space

# Q35
students = ["alice", "bob", "carol"]
ids = frozenset([123, 124, 125])
records = {}
j = 0

for i in ids:
    records.update({i: students[j]})
    j += 1

# Q36
print(records)
