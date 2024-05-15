# num_terms = int(input("Enter the number of terms: "))

# a, b = 0, 1
# count = 0

# while count < num_terms:
#   print(a, end=" ")
#   c = a + b
#   a = b
#   b = c
#   count += 1


a=2
for i in range(1,6,2):
 for j in range(i):
  print(a, end=' ')
  a+=2
 print()