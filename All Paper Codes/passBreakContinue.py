# Using pass in a loop
print("Using pass:")
for i in range(5):
    if i == 2:
        pass  # pass does nothing, it's a placeholder
    print(f"Current value: {i}")

print("\nUsing break:")
# Using break to exit a loop early
for i in range(5):
    if i == 2:
        break  # break exits the loop
    print(f"Current value: {i}")

print("\nUsing continue:")
# Using continue to skip the current iteration
for i in range(5):
    if i == 2:
        continue  # continue skips the rest of the loop for this iteration
    print(f"Current value: {i}")

# Using pass in a function
def my_function():
    pass  # pass is used as a placeholder for future code

# Function with break
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"First even number found: {number}")
            break  # exit the loop once the first even number is found

# Function with continue
def skip_odds_and_print(numbers):
    for number in numbers:
        if number % 2 != 0:
            continue  # skip odd numbers
        print(f"Even number: {number}")

# Call the functions
print("\nUsing break in a function:")
find_first_even([1, 3, 5, 6, 7, 8])

print("\nUsing continue in a function:")
skip_odds_and_print([1, 2, 3, 4, 5, 6])
