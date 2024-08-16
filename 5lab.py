# Jasmin Duishebaeva
# 08.15.2024

# Problem 5: Convert radians to degrees based on user input and compare it with math.degrees.

import math

radians = float(input("Enter radians value: "))
degrees = radians * (180 / math.pi)  # Conversion formula
print("Converted Degrees:", degrees)
print("math.degrees:", math.degrees(radians))
