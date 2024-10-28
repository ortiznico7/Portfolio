start_amount = 960.23
end_amount = 1093.73
increment = 1.50

# Calculate the number of iterations
num_iterations = int((end_amount - start_amount) / increment) + 1

for i in range(num_iterations):
    currentRentAmnt = start_amount + (i * increment)  # Calculate current rent amount
    print(currentRentAmnt)
    print(f"Your rent amount is currently at {currentRentAmnt:.2f}.")

print("You have reached a monthly payment of 1093.73 or over. Please let us know if you need adjustments to your budgeting skills.")
