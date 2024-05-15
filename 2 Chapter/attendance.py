classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
  print("Student is allowed to sit in the exam.")
else:
#   medical_cause = input("Does the student have a medical cause (Y/N)? ").upper()
#   if medical_cause == 'Y':
#     print("Student may be allowed to sit in the exam with approval from relevant authorities.")
#   else:
    print("Student is NOT allowed to sit in the exam.")
