person1 = int(input("Enter the age of first person: "))
person2 = int(input("Enter the age of second persion: "))
person3 = int(input("Enter the age of third person: "))

oldest = max(person1, person2, person3)
youngest = min(person1, person2, person3)

print (f"The oldest age is {oldest}")
print (f"The youngest age is {youngest}")