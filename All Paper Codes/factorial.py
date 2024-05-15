def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter the no: "))
if n<0:
    print("Negative no")
else:
    result = factorial(n)
    print(f"Factorial of {n} is {result}")