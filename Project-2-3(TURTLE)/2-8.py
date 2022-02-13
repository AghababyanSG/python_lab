import turtle as t

n = int(input())

t.shape('classic')
t.speed('fastest')

i = 0
while i <= n * 4:
    t.forward(10 + i * 10)
    t.left(90)
    i += 1

input()
