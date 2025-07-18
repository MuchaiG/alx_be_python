# Step 1: Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Step 2: Use a while loop to handle rows
row = 0
while row < size:
    # Step 3: Use a for loop to print stars in the current row
    for col in range(size):
        print("*", end="")
    print()  # move to the next line after each row
    row += 1
