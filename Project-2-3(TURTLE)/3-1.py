from turtle import *
from random import randint

shape('classic')
speed('fast')
color('red')

while True:
    forward(randint(1, 30))
    left(randint(-179, 180))
