# Jasmin Duishebaeva
# 08.15.2024

# Problem 6: Calculate factorial using a for loop and compare it with math.factorial.

import math

number = int(input("Enter a number to calculate its factorial: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Calculated Factorial:", factorial)
print("math.factorial:", math.factorial(number))
