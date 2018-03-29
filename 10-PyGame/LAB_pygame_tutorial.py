import sys
import random
import pygame

#main
pygame.init()
pygame.display.set_caption('Whack-A-Mole')

screen = pygame.display.set_mode((600, 600))
rectplace = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 100))
limit = 500000 #programs run in millisecond
randx = 0
randy = 0
score = 0
running = True

while running:
    pos = pygame.mouse.get_pos() #stores the mouse position.
    (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()
    if rectplace.collidepoint(pos) and pressed1 == 1:
        score += 1
        print('Score: ', score)
        limit = 500000
    if limit == 500000:
        rectplace = pygame.draw.rect(screen, (0, 0, 0), (randx, randy, 100, 100))
        randx = random.randrange(100, 500)
        randy = random.randrange(100, 500)
        rectplace = pygame.draw.rect(screen, (255, 255, 255), (randx, randy, 100, 100))
        limit = 0
        pygame.display.update() #updates the loop (frame --> event --> process --> frame)
    limit += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
