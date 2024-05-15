import Operation

a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))

add = Operation.addition(a, b)
sub = Operation.subtraction(a, b)

print("Addition: ",add)
print("Subtraction: ",sub)