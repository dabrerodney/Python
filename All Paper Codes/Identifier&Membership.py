color = ["red", "yellow", "green"]

t1 = (10, 20, 30)
t2 = (10, 20, 30)
t3 = t1

print("Membership operator Eg")
print("yellow" in color)
print("black" not in color)
print("brown" in color)

print("Identity operator Eg")
print(t1 is t2)
print(t1 is t3)
print(t3 is t2)