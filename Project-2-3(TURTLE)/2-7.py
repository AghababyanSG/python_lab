import turtle as t

n = int(input())

t.shape('classic')
t.speed('fastest')

i = 0
while i <= n * 360:

    t.forward(i/1000)
    t.left(1)
    i += 1

input()
