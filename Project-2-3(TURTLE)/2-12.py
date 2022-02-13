import turtle as t

t.shape('classic')
t.speed('fastest')


def circle_2(length, alpha):
    for k in range(0, 360 // (2 * alpha)):
        t.forward(length)
        t.right(alpha)
    for j in range(0, 360 // (2 * alpha)):
        t.forward(length / 5)
        t.right(alpha)


Length = 5
t.left(90)
while True:
    Length += 2
    circle_2(Length, 5)