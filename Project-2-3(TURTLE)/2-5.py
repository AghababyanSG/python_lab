import turtle as t
import numpy
import math

t.shape('turtle')
t.speed('fast')
i = 0
while i <= 9:

    j = 0
    while j <= 3:
        t.forward(i * 20 + 20)
        t.left(90)

        j += 1

    t.penup()
    t.right(135)
    t.forward(14)
    t.left(135)
    t.pendown()

    i = i + 1

input()
