from turtle import *
import numpy as np

shape('turtle')
speed('fastest')


def polygon(step1, angle1):
    for k in range(angle1):
        forward(step1)
        left(360 / angle1)
    right(90 + (180 / angle1))


step0 = 20
left(150)
step = 2 * step0 * np.sqrt(3)
angle = 3
for i in range(10):
    polygon(step, angle)

    penup()
    forward(step0)
    pendown()

    angle += 1
    step = 2 * (angle - 1) * step0 * np.sin(np.pi / angle)
    left(90 + (180 / angle))

hideturtle()
input()
