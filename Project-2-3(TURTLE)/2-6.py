import turtle as t

n = int(input())

t.shape('classic')
t.speed('fast')

i = 1
while i <= n:
    t.forward(100)
    t.right(180)
    t.forward(100)
    t.right(180)
    t.right(360 / n)

    i = i + 1

input()