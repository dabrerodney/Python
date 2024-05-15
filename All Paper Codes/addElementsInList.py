l1 = []
len = int(input("Enter the length of the string: "))
for i in range(1, len+1):
    i = int(input("Enter the elememts: "))
    l1.append(i)

print("Current List", l1)

l1.append(10)
print("After Appending", l1)

l1.extend([20,30])
print("After Extending", l1)

l1.insert(2, 100)
print("After inserting", l1)