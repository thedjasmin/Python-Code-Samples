# Jasmin Duishebaeva
# 08.05.2024
# Problem 3 – Write a program that asks the user for the number of sides, 
# the length of the side, the color of the line, and the fill color of a regular polygon. 
# The program should draw the polygon and then fill it in.
import turtle
sides = int(input("Write the number of sides: "))
length = int(input("Write the length of the side: "))
line_color = input("Write the color of the line: ")
fill_color = input("Write the fill color: ")

turtle.color(line_color)
turtle.begin_fill()
turtle.fillcolor(fill_color)

for _ in range(sides):
    turtle.forward(length)
    turtle.left(360 / sides)

turtle.end_fill()
turtle.done()