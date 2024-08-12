# Jasmin Duishebaeva
# 08.05.2024
# Problem 5 – Write a program to draw some kind of picture. 
# Be creative and experiment with the turtle methods provided in "Summary of Turtle Methods". 
import turtle
turtle.speed(10) 
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    turtle.pencolor(colors[i % 6])
    turtle.forward(i)
    turtle.left(59)
turtle.done()