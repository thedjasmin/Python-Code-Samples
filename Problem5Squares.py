import turtle

# Jasmin Duishebaeva
# 08.15.2024

# Problem 5: Use the following chunk of code as a base to produce the image shown below.

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

size = 20
for i in range(5):
    drawSquare(alex, size)
    size += 20
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

wn.exitonclick()
