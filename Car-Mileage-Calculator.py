def calculate_mpg():
    """
    Calculates and prints the miles per gallon (MPG) of a car.
    """
    try:
        # Get miles driven from the user
        miles_driven_str = input("Enter the number of miles driven: ")
        miles_driven = float(miles_driven_str)
 
        # Get gallons of fuel used from the user
        gallons_used_str = input("Enter the number of gallons of fuel used: ")
        gallons_used = float(gallons_used_str)
 
        # Check for invalid input (e.g., zero or negative gallons)
        if gallons_used <= 0:
            print("Gallons used must be a positive number.")
            return
 
        # Calculate MPG
        mpg = miles_driven / gallons_used
 
        # Print the result, formatted to two decimal places
        print(f"Your car's mileage is: {mpg:.2f} MPG")
 
    except ValueError:
        print("Invalid input. Please enter numerical values for miles and gallons.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
# Call the function to run the calculator
if __name__ == "__main__":
    calculate_mpg()