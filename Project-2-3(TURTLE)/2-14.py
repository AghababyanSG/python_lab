from turtle import *
import numpy as np

step = 50


def star(n):
    polygon_angles_sum = (n - 2) * 180
    one_angle = 180 - 2 * (180 - polygon_angles_sum / n)
    print(one_angle)
    for i in range(n):
        forward(step)
        if n > 8:
            left((180 - one_angle) * 2)
        else:
            left(180 - one_angle)


shape('classic')
speed('slowest')

star(5)
penup()
forward(5 * step)
pendown()
star(11)

input()
