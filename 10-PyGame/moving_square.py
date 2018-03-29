import random
import pygame

pygame.init()
pygame.display.set_caption('Moving Square')

screen = pygame.display.set_mode((600, 600))
randx = 300
randy = 300
game_running = True

while game_running:
    screen.fill((0, 0, 0))
    square = pygame.draw.rect(screen, (255, 51, 153), (randx, randy, 100, 100))
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        square = pygame.draw.rect(screen, (0, 0, 0), (randx, randy, 100, 100))
        if event.key == pygame.K_ESCAPE:
            game_running = False
        elif event.key == pygame.K_LEFT:
            randx -= 20
        elif event.key == pygame.K_RIGHT:
            randx += 20
        elif event.key == pygame.K_UP:
            randy -= 20
        elif event.key == pygame.K_DOWN:
            randy += 20

        square = pygame.draw.rect(screen, (255, 51, 153), (randx, randy, 100, 100))
        pygame.display.update()
