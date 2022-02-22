import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.draw.rect(screen, (255, 255, 255), (0, 0, 400, 400))
pygame.draw.circle(screen, (252, 246, 76), (200, 200), 100)
pygame.draw.circle(screen, (252, 0, 0), (150, 180), 20)
pygame.draw.circle(screen, (252, 0, 0), (250, 180), 15)
pygame.draw.circle(screen, (0, 0, 0), (150, 180), 10)
pygame.draw.circle(screen, (0, 0, 0), (250, 180), 8)
pygame.draw.rect(screen, (0, 0, 0), (150, 245, 100, 20))

yp = -3
pygame.draw.polygon(screen, (0, 0, 0), [(180, 176), (183, 171), (97, 116), (95, 120)])
pygame.draw.polygon(screen, (0, 0, 0), [(296, 142 - yp), (300, 145 - yp), (220, 170 - yp), (216, 167 - yp)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
