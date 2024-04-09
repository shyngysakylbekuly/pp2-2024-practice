import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))  # Fill the screen with white color
    color = (0, 128, 255)
    rectangle = pygame.Rect(30, 30, 60, 30)
    pygame.draw.rect(screen, color, rectangle)

    pygame.display.flip()

pygame.quit()
sys.exit()
