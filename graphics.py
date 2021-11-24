import pygame, math
pygame.init()

# Defining color
BLACK = (0x00, 0x00, 0x00)
WHITE = (0xFF, 0xFF, 0xFF)
RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test Drive")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
