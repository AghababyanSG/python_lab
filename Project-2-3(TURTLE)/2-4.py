import turtle as t
import numpy as np

polygon_n = 360
#int(input(polygon_n))

x = 0
t.shape('turtle')

while x <= polygon_n:

    t.forward(1)
    t.left(360 / polygon_n)
    x += 1
