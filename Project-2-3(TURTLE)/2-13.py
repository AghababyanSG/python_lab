from turtle import *
import numpy as np

PI = 3.141592

shape('classic')
speed('fastest')


def circle(length, angle):
    for k in range(0, 360 // angle):
        forward(length)
        left(angle)


def quarter_circle(length, angle):
    for k in range(0, 360 // (4 * np.abs(angle)) + 1):
        forward(length)
        left(angle)


length_big = 5
angle_big = 5

length_small = 1
angle_small = 8

length_quarter = 5
angle_quarter = 10

color('black', 'yellow')
begin_fill()
circle(length_big, angle_big)
end_fill()

penup()
left(90)
forward(75)

left(90)
forward(27)
right(90)
pendown()

color('navy', 'navy')
begin_fill()
circle(length_small, angle_small)
end_fill()

penup()
left(270)
forward(68)
left(90)
pendown()

r_small = length_small / (2 * np.sin(angle_small * PI / 180))
print(r_small)

color('navy', 'navy')
begin_fill()
circle(length_small, angle_small)
end_fill()

penup()
left(90)
forward(41)
left(90)
forward(15)

pendown()
width(4)
color('cyan')
forward(25)

penup()
forward(15)

left(90)

color('red')
quarter_circle(length_quarter, angle_quarter)
left(180)

pendown()
quarter_circle(length_quarter, -angle_quarter)
quarter_circle(length_quarter, -angle_quarter)

input()
