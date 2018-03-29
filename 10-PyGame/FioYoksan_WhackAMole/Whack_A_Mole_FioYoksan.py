import sys
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from pygame.font import *
import time

pygame.init()

position_list = [(100, 350), (300, 350), (500, 350), (100, 150), (300, 150), (500, 150)]

class Mole(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('mole-clip-art-mole.png')
        self.rect = self.image.get_rect()
        self.rect.center = position_list[random.randint(0, 5)]

    #move the mole to random location
    def move(self):
        self.rect.center = position_list[random.randint(0, 5)]

class Hammer(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('hammer.png')
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    #makes the sprite follow the mouse cursor
    def update(self):
        self.rect.center = mouse.get_pos()


class TenSecond(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('ten_seconds.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300, 200)

class TenWhacks(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('ten_whacks.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300, 350)

class GameOver(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('game_over.png')
        self.rect = self.image.get_rect()
        self.rect.center = (300, 250)

from pygame.mixer import *
mixer.init()
mixer.stop()


#main
display.set_caption('Whack-A-Mole')
screen = display.set_mode((600, 500))

#hide the mouse cursor
mouse.set_visible(False)

font = Font(None, 25)

#CREATE SPRITES
tensecond_button = TenSecond()
tenwhacks_button = TenWhacks()
buttons = Group(tensecond_button, tenwhacks_button)

my_mole = Mole()
my_hammer = Hammer()
hammer_sprite = Group(my_hammer)
all_sprites = Group(my_mole, my_hammer)

game_over = GameOver()
ending = Group(game_over)


game_running = True

while game_running:
    mixer.Sound("gravity_falls.wav").play(-1)
    score = 0

    starting_time = time.time()
    mole_timer = time.time()

    screen.fill((0, 0, 0))
    buttons.draw(screen)
    hammer_sprite.draw(screen)
    hammer_sprite.update()

    display.update()

    pos = mouse.get_pos()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False

        if event.type == MOUSEBUTTONDOWN:

            if my_hammer.hit(tensecond_button):
                while True:
                    screen.fill((0,153,0))

                    for i in range(0, 6):
                        holes = pygame.draw.circle(screen, (0, 102, 0), position_list[i], 80, 80)

                    all_sprites.draw(screen)
                    all_sprites.update()

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                        elif event.type == MOUSEBUTTONDOWN:
                            if my_hammer.hit(my_mole):
                                mixer.Sound("whack_sound.wav").play()
                                my_mole.move()
                                score += 1
                                mole_timer = time.time()

                    if time.time() - mole_timer >= 2:
                        my_mole.move()
                        mole_timer = time.time()


                    your_time = int(time.time() - starting_time)
                    time_text = font.render("Time: " + str(your_time), True, (0, 0, 0))
                    screen.blit(time_text, (100, 25))
                    if your_time >= 10:
                        ending.draw(screen)
                        display.update()
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                    screen.blit(score_text, (250, 25))

                    display.update()

            elif my_hammer.hit(tenwhacks_button):
                while True:
                    screen.fill((0,153,0))

                    for i in range(0, 6):
                        holes = pygame.draw.circle(screen, (0, 102, 0), position_list[i], 80, 80)

                    all_sprites.draw(screen)
                    all_sprites.update()

                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                        elif event.type == MOUSEBUTTONDOWN:
                            if my_hammer.hit(my_mole):
                                mixer.Sound("whack_sound.wav").play()
                                my_mole.move()
                                score += 1
                                mole_timer = time.time()

                    if time.time() - mole_timer >= 2:
                        my_mole.move()
                        mole_timer = time.time()

                    your_time = int(time.time() - starting_time)
                    time_text = font.render("Time: " + str(your_time), True, (0, 0, 0))
                    screen.blit(time_text, (100, 25))
                    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
                    screen.blit(score_text, (250, 25))
                    if score >= 10:
                        ending.draw(screen)
                        display.update()
                    display.update()
