# Jasmin Duishebaeva
# 08.15.2024

# Problem 2: Write a Python function to check whether a number is in a given range.

def checkRange(num):
    if num in range(1, 10):
        print(num, "is in the range.")
    else:
        print(num, "is not in the range.")

# Example usage
number = int(input("write the number:"))
checkRange(number)
