# Ask user for quantity
quantity = int(input("Enter the quantity you want to purchase: "))

# Calculate total cost
unit_cost = 100
total_cost = quantity * unit_cost

# Apply discount if total cost is more than 1000
if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount

# Print total cost for user
print("Total cost:", total_cost)
