# Welcome message for the Squeeze Juice Company salary calculation program
print("Welcome to the Squeeze Juice Company Employee Salary Calculator!")

# Loop to keep the program running until the user inputs -1 to exit
while True:
    # Request user input for the number of hours worked
    hours_worked = float(input("Please enter the number of hours worked (or enter -1 to exit): "))
    
    # Exit condition: If the user inputs -1, the program will terminate
    if hours_worked == -1:
        print("Exiting the program. Thank you for using the Squeeze Juice Company Employee Salary Calculator!")
        break

    # Request user input for the hourly wage
    hourly_wage = float(input("Please enter the hourly wage: "))

    # Check if the hours worked are less than or equal to 40
    if hours_worked <= 40:
        # Calculate salary for regular hours (less than or equal to 40 hours)
        salary = hours_worked * hourly_wage
    else:
        # Calculate salary for regular 40 hours and overtime (hours above 40)
        regular_salary = 40 * hourly_wage
        overtime_hours = hours_worked - 40
        overtime_salary = overtime_hours * (hourly_wage * 1.5)
        salary = regular_salary + overtime_salary

    # Output the calculated salary
    print(f"The total salary for the employee is: {salary} ")

