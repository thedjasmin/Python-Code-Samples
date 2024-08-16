import math

# Jasmin Duishebaeva
# 08.15.2024

# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.

def areaOfCircle(r):
    return math.pi * r * r

# Example usage
radius = int(input("Write radius: "))
print("The area of the circle with radius", radius, "is", areaOfCircle(radius))
