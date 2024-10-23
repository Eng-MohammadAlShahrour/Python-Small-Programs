# Start the program
print("Please Enter 10 numbers:")

# Define variables for the largest three numbers
max1 = float(0.0)  # The largest number
max2 = float(0.0)  # The second largest
max3 = float(0.0)  # The third largest

# Input the numbers (from 1 to 10)
for i in range(1, 11):  # Loop from 1 to 10
    while True:  # Loop until a valid number is entered
        try:
            num = float(input(f"Number {i}: "))  # Read the number
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid number.")  # Prompt user for valid input
    
    # Update the largest three numbers
    if num > max1:
        max3 = max2  # Update the third largest
        max2 = max1   # Update the second largest
        max1 = num    # Update the largest
    elif num > max2:
        max3 = max2   # Update the third largest
        max2 = num    # Update the second largest
    elif num > max3:
        max3 = num    # Update the third largest

# Print the results
print(f"The largest three numbers are: {max1}, {max2}, {max3}")
