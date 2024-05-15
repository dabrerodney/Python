# Initialize variables
count = 1
even_numbers = []

while len(even_numbers) < 10:
    if count % 2 == 0:
        even_numbers.append(count)
    count += 1

for num in even_numbers:
    print(num)
