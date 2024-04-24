import pygame
from pygame.locals import *

pygame.init()

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Animated Background')

# Load images
try:
    bg = pygame.image.load('bg.png').convert()  # Convert the image to improve performance
except pygame.error as e:
    print("Error loading background image:", e)
    pygame.quit()
    raise SystemExit

# Define initial position for the background
bg_x = 0
bg_y = 0

# Define speed for the background animation
bg_speed = 1

run = True
while run:
    screen.blit(bg, (bg_x, bg_y))

    # Move the background horizontally
    bg_x -= bg_speed
    if bg_x <= -screen_width:
        bg_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
