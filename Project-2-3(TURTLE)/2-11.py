import turtle as t

t.shape('classic')
t.speed('fastest')


def circle_2(length, alpha):
    for k in range(0, 360 // alpha):
        t.forward(length)
        t.left(alpha)
    for j in range(0, 360 // alpha):
        t.forward(length)
        t.right(alpha)


Length = 2
t.left(90)
while True:
    Length += 2
    circle_2(Length, 5)