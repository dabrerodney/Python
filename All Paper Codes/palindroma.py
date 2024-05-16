# def checkString(str):
#     return str[::-1]

# str = input("Enter the string: ")
# new_str = checkString(str)

# if str == new_str:
#     print(f"{str} is a palindrome")
# else:
#     print(f"{str} ia not a palindrom")

# l1 = [23, 99, 56, 72, 57, 88]
# print("Before sorting", l1)
# l1.sort()
# print("After Sorting", l1)

def sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum

number = 12345
print("Sum of digits in", number, "is:", sum_of_digits(number))


