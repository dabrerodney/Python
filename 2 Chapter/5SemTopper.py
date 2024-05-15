
subjects = ["Adv Java", "Env Studies", "OS", "SW Testing"]

pramesh_marks = [65, 68, 59, 55]
satish_marks = [56, 69, 67, 59]

pramesh_total = sum(pramesh_marks)
satish_total = sum(satish_marks)

pramesh_percentage = (pramesh_total / (len(subjects) * 100)) * 100
satish_percentage = (satish_total / (len(subjects) * 100)) * 100

if pramesh_total > satish_total:
    topper = "Pramesh"
else:
    topper = "Satish"

print(f"Pramesh Results:")
print(f"\tTotal Marks: {pramesh_total}")
print(f"\tPercentage: {pramesh_percentage:.2f}%")

print(f"\nSatish Results:")
print(f"\tTotal Marks: {satish_total}")
print(f"\tPercentage: {satish_percentage:.2f}%")

print(f"\nTopper of 5th Semester: {topper}")
