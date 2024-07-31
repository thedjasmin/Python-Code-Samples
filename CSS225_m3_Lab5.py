# Jasmin Duishebaeva
# 07.22.2024
# Problem 5 - Write a program that will compute MPG for a car. 
# Prompt the user to enter the number of miles driven and the number of gallons used. 
# Print a nice message with the answer.
miles = int(input("How many miles driven? "))
gallons = int(input("How many gallons used? "))
MPG = int(miles / gallons)
print("Your MPG is ", MPG)
