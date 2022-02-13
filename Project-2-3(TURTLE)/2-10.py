import turtle as t

t.shape('classic')
t.speed('fastest')


def circle_2(length, alpha):
    for k in range(0, 360 // alpha):
        t.forward(length)
        t.left(alpha)
    for k in range(0, 360 // alpha):
        t.forward(length)
        t.right(alpha)


# n = int(input()) #число лепестков


LENGTH_circ = 2
ALPHA_circ = 2
n = 5
for i in range(0, n):
    circle_2(LENGTH_circ, ALPHA_circ)
    t.right(180 / n)

input()
