"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
logan = turtle.Turtle()
logan.color("red")

for i in range(100):
    logan.forward(200)
    logan.left(170)
