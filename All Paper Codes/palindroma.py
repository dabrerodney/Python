def checkString(str):
    return str[::-1]

str = input("Enter the string: ")
new_str = checkString(str)

if str == new_str:
    print(f"{str} is a palindrome")
else:
    print(f"{str} ia not a palindrom")
