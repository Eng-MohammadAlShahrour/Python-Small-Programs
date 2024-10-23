import random  # Importing the random number generation library

# Start of the program
print("Multiplication Table Learning Program")

# Initialize variables for the count of correct and incorrect attempts
correct_attempts = 0
incorrect_attempts = 0
continue_MULT = True  # Set continue_MULT to True at the beginning

# Start the loop for continuation
while continue_MULT:
    # Generate two random integers between 1 and 10
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    
    # Ask the user for the result of the multiplication
    user_answer = float(input(f"What is the result of {number1} * {number2}? "))  # Read the user's answer
    
    # Check the correctness of the answer
    if user_answer == (number1 * number2):
        print("Correct answer!")  # If the answer is correct
        correct_attempts = correct_attempts + 1  # Increase the count of correct attempts in a basic way
    else:
        print(f"Incorrect answer. The correct result is: {number1 * number2}")  # If the answer is incorrect
        incorrect_attempts = incorrect_attempts + 1  # Increase the count of incorrect attempts in a basic way

    # Ask the user if they want to continue
    user_choice = input("Do you want to continue? (Y - Yes, N - No): ")  # Read the user's choice for continuation
    if user_choice == 'N':  # If the user chooses not to continue
        continue_MULT = False  # End the MULT

# Print the final results
print(f"Number of correct attempts: {correct_attempts}")  # Print the number of correct attempts
print(f"Number of incorrect attempts: {incorrect_attempts}")  # Print the number of incorrect attempts
