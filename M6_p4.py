# Jasmin Duishebaeva
# 08.22.2024
# Problem 4 – Write a function that takes a year as a parameter and 
# returns True if the year is a leap year, False if it is otherwise.
# Consider the requirements of a leap year:
# -	The year is evenly divisible by 4
# -	If the year can be evenly divided by 100 it is NOT a leap year, unless:
# 	If the year is also evenly divisible by 400, then it is a leap year.


# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
input_year = int(input("Enter a year: "))
if is_leap_year(input_year):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")
