class MyException(Exception):
    pass

def password(paswd):
    correct_paswd = "Hello"
    if paswd != correct_paswd:
        raise MyException("Incorrect Password")
    else:
        print("Correct Password")

try:
    paswd = input("Enter the Password: ")
    password(paswd)
except MyException as e:
    print("Exception:", e)

# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum

# try:
#     n = int(input("Enter a number: "))
#     print(getSum(n))
# except ValueError:
#     print("Invalid input, Print enter a valid integerhe")