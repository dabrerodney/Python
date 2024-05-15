d1 = {1: "Hello", 2: "World", 3: "Python", 4: "Java", 5: "C++"}

print(d1.pop(2))
print(d1)

print(d1.popitem())
print(d1)


del d1[4]
print(d1)

d1.clear()
print(d1)
