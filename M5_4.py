# Jasmin Duishebaeva
# 08.05.2024
# Problem 4 – Consider a program that iterates the integers from 1 to 50.
# For multiples of three print “Divisible by three” instead of the number and for the multiples of five print
# “Divisible by five”. For numbers which are multiples of both three and five print “Divisible by both”.
# Use draw.io to draw the flow of execution. Then write the program. Submit both the flowchart and the code.
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)