# Jasmin Duishebaeva
# 22.08.2024
# Problem 2 – Write a function that takes two inputs from a user and 
# prints whether the sum is greater than 10, less than 10, or equal to 10.
input1 = float(input("Write the first number: "))
input2 = float(input("Write the second number: "))

# Calculate sum
sum_value = input1 + input2

# Compare sum to 10
if sum_value > 10:
    print("Sum is greater than 10.")
elif sum_value < 10:
    print("Sum is less than 10.")
else:
    print("Sum is equal to 10.")
