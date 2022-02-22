import pygame
from random import randint
import numpy as np


def clouds(color, number, radius, rect_size, rect_pos):
    for i in range(0, number):
        # print(rect_size[0])
        # print(rect_size[1])
        length = randint(0, int(rect_size[0] / 2))
        height = int(randint(0, rect_size[1]))
        pygame.draw.circle(screen, 'black', (rect_pos[0] + length, rect_pos[1] - height), radius + 1)
        pygame.draw.circle(screen, color, (rect_pos[0] + length, rect_pos[1] - height), radius)


def tree(tree_size, tree_pos):
    a = 16  # высота перемещения
    radius = 20
    pygame.draw.rect(screen, (20, 20, 0), (tree_pos[0] - 3 // tree_size, tree_pos[1], 10 / tree_size, 70 // tree_size))
    pygame.draw.circle(screen, 'black', (tree_pos[0] - (a + 5) // tree_size, tree_pos[1]), (radius + 1) // tree_size)
    pygame.draw.circle(screen, 'forest green', (tree_pos[0] - (a + 5) // tree_size, tree_pos[1]), radius // tree_size)
    pygame.draw.circle(screen, 'black', (tree_pos[0] + (a + 5) // tree_size, tree_pos[1]), (radius + 1 // tree_size))
    pygame.draw.circle(screen, 'forest green', (tree_pos[0] + (a + 5) // tree_size, tree_pos[1]), radius // tree_size)
    pygame.draw.circle(screen, 'black', (tree_pos[0] + 5 // tree_size, tree_pos[1] - (a - 4) // tree_size),
                       (radius + 1) // tree_size)
    pygame.draw.circle(screen, 'forest green', (tree_pos[0] + 5 // tree_size, tree_pos[1] - (a - 4) // tree_size),
                       radius // tree_size)
    pygame.draw.circle(screen, 'black', (tree_pos[0] - (10 + 5) // tree_size, tree_pos[1] - 3 * (a - 4) // tree_size),
                       (radius + 1) // tree_size)
    pygame.draw.circle(screen, 'forest green',
                       (tree_pos[0] - (10 + 5) // tree_size, tree_pos[1] - 3 * (a - 4) // tree_size),
                       radius // tree_size)
    pygame.draw.circle(screen, 'black', (tree_pos[0] + (10 + 5) // tree_size, tree_pos[1] - 3 * (a - 4) // tree_size),
                       (radius + 1) // tree_size)
    pygame.draw.circle(screen, 'forest green',
                       (tree_pos[0] + (10 + 5) // tree_size, tree_pos[1] - 3 * (a - 4) // tree_size),
                       radius // tree_size)
    pygame.draw.circle(screen, 'black', (tree_pos[0] + 5 // tree_size, tree_pos[1] - 4.5 * (a - 4) // tree_size),
                       (radius + 1) // tree_size)
    pygame.draw.circle(screen, 'forest green', (tree_pos[0] + 5 // tree_size, tree_pos[1] - 4.5 * (a - 4) // tree_size),
                       radius // tree_size)


def star(number, color, radius, delta_r, position):
    # start of coordinates are from center
    for i in range(number * 2):
        if i % 2 == 0:
            a = position[0] + int(np.cos(np.pi * i / number) * (radius + delta_r))
            b = position[1] + int(np.sin(np.pi * i / number) * (radius + delta_r))
            c = np.array([a, b])
            if i != 0:
                coordinates = np.vstack((coordinates, c))
            else:
                coordinates = np.array(c)
        else:
            a = (position[0] + int(np.cos(np.pi * i / number) * radius))
            b = position[1] + int(np.sin(np.pi * i / number) * radius)
            c = (a, b)
            coordinates = np.vstack((coordinates, c))

    print(coordinates)
    pygame.draw.polygon(screen, color, coordinates, width=0)


def house(position, size):
    length = 100 // size
    height = 75 // size
    w_side = 30 // size  # window side size
    pygame.draw.polygon(screen, 'brown', [(position[0], position[1]),
                                          (position[0] + length, position[1]),
                                          (position[0] + length, position[1] + height),
                                          (position[0], position[1] + height)])
    pygame.draw.polygon(screen, 'crimson', [(position[0], position[1]),
                                            (position[0] + length // 2, position[1] - height // 2),
                                            (position[0] + length, position[1])])
    pygame.draw.rect(screen, 'orange',
        (position[0] + (length - w_side) // 2 - 1, position[1] + (height - w_side) // 2 - 1, w_side + 2, w_side + 2))
    pygame.draw.rect(screen, 'cyan',
                     (position[0] + (length - w_side) // 2, position[1] + (height - w_side) // 2, w_side, w_side))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((455, 300))
pygame.draw.rect(screen, (51, 204, 204), (0, 0, 500, 150))
pygame.draw.rect(screen, (0, 204, 0), (0, 150, 500, 150))
clouds('white', 5, 15, [100, 30], [200, 30])
tree(1, [280, 130])
star(36, 'black', 25 + 1, 3 + 1, [370, 40])  # black star
star(36, 'gold', 25, 3, [370, 40])
house([100, 80], 0.8)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
