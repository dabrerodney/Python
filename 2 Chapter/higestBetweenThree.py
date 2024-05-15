a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

if a > b and a > c:
    print ("A is greater")
elif b > a and b > c:
    print ("B is greater")
elif c > a and c > b:
    print ("C is greater")
else:
    print ("All three nos are equal")  