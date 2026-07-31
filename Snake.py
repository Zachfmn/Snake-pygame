import pygame
import random

pygame.init()

# config
WINDOW_SIZE = WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
SPEED = 10

gameWindow = pygame.display.set_mode(WINDOW_SIZE)

# colour
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# images
#
#
#

pygame.display.set_caption(title="Snake")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

exit_game = False

while exit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

pygame.display.quit()
pygame.quit()