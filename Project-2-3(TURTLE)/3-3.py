from turtle import *

shape('classic')
color('blue')
speed('fastest')

file = open('font.txt', 'r')
font = int(file.read())

s = 20 * font
width(font)
d = s * (2 ** 0.5)
angle = 45
penup()
goto(-6 * s, 0)
pendown()


def draw(route):
    for angle, step, pen in route:
        if pen == 0:
            penup()
        else:
            pendown()

        rt(angle)
        fd(step)


m = [

    [(0, s, 1), (2 * angle, 2 * s, 1), (2 * angle, s, 1), (2 * angle, 2 * s, 1), (2 * angle, 2 * s, 0)],
    [(2 * angle, s, 0), (-3 * angle, d, 1), (3 * angle, 2 * s, 1), (4 * angle, 2 * s, 0), (2 * angle, s, 0)],
    [(0, s, 1), (2 * angle, s, 1), (angle, d, 1), (-3 * angle, s, 1), (-2 * angle, 2 * s, 0), (2 * angle, s, 0)],
    [(0, s, 1), (3 * angle, d, 1), (-3 * angle, s, 1), (3 * angle, d, 1), (3 * angle, 2 * s, 0), (2 * angle, 2 * s, 0)],
    [(2 * angle, s, 1), (-2 * angle, s, 1), (2 * angle, s, 1), (4 * angle, 2 * s, 1), (2 * angle, s, 0)],
    [(2 * angle, 2 * s, 0), (-2 * angle, s, 1), (-2 * angle, s, 1), (-2 * angle, s, 1), (2 * angle, s, 1), (2 * angle, s, 1), (0, s, 0)],
    [(0, s, 0), (3 * angle, d, 1), (-angle, s, 1), (-2 * angle, s, 1), (-2 * angle, s, 1), (-2 * angle, s, 1), (2 * angle, s, 0),
     (2 * angle, 2 * s, 0)],
    [(0, s, 1), (3 * angle, d, 1), (-angle, s, 1), (4 * angle, 2 * s, 0), (2 * angle, 2 * s, 0)],
    [(0, s, 1), (2 * angle, 2 * s, 1), (2 * angle, s, 1), (2 * angle, s, 1), (2 * angle, s, 1), (4 * angle, s, 1), (2 * angle, s, 1),
     (2 * angle, 2 * s, 0)],
    [(0, s, 1), (2 * angle, s, 1), (angle, d, 1), (4 * angle, d, 1), (-3 * angle, s, 1), (2 * angle, s, 1), (2 * angle, 2 * s, 0)]

]

draw(m[1])
draw(m[4])
draw(m[1])
draw(m[7])
draw(m[0])
draw(m[0])

hideturtle()

input()
