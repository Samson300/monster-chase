import pygame
import random
import time
import sys

def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load('images/background.png').convert_alpha()
    # hero_image = pygame.image.load('images/hero.png').convert_alpha()
    

    
    class Hero():
        def __init__(self):
            self.image = pygame.image.load('images/hero.png').convert_alpha()
            self.locationx = 240
            self.locationy = 240
            self.counter = 0
        def location_change(self):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.locationx -= 5
                if event.key == pygame.K_RIGHT:
                    self.locationx += 5
                if event.key == pygame.K_UP:
                    self.locationy -= 5
                if event.key == pygame.K_DOWN:
                    self.locationy += 5
                



    
    class Monster():
        def __init__(self):
            self.image = pygame.image.load('images/monster.png').convert_alpha()
            self.locationx = 400
            self.locationy = 400
            self.counter = 0
        def location_jump(self):
            if self.locationx == width:
                self.locationx = 0
            elif self.locationx == 0:
                self.locationx = width
            elif self.locationy == height:
                self.locationy = 0
            elif self.locationy == 0:
                self.locationy = height
        
        def location_change(self):
        
            if self.counter <= 100:
                self.locationx += 5
                self.counter += 1
            elif self.counter <= 200:
                self.locationx -= 5
                self.counter += 1
            elif self.counter <= 300:
                self.locationy += 5
                self.counter += 1
            elif self.counter <= 400:
                self.locationy -= 5
                self.counter += 1
            elif self.counter <= 500:
                self.locationy += 5
                self.locationx += 5
                self.counter += 1
            elif self.counter <= 600:
                self.locationy -= 5
                self.locationx -= 5
                self.counter += 1
            elif self.counter <= 700:
                self.locationy += 5
                self.locationx -= 5
                self.counter += 1
            elif self.counter <= 800:
                self.locationy -= 5
                self.locationx += 5
                self.counter += 1
            else:
                self.counter = 0
    monster = Monster()
    hero = Hero()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster.location_jump()
        monster.location_change()
        hero.location_change()


        # Draw background

        # screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero.image, (hero.locationx, hero.locationy))
        screen.blit(monster.image, (monster.locationx, monster.locationy))

        


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
