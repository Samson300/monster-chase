import pygame
import random
import time
import sys
import math

pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("sounds/win.wav")
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


    class Character():
        def __init__(self):
            self.counter = 0


    class Hero(Character):
        def __init__(self):
            self.image = pygame.image.load('images/hero.png').convert_alpha()
            self.locationx = 240
            self.locationy = 240
            self.counter = 0
        def location_change(self):
            if self.locationx >= width - 60:
                self.locationx -= 3
            elif self.locationx < 35:
                self.locationx += 3
            elif self.locationy < 35:
                self.locationy += 3
            elif self.locationy >= height -65:
                self.locationy -= 3 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.locationx -= 3
                if event.key == pygame.K_RIGHT:
                    self.locationx += 3
                if event.key == pygame.K_UP:
                    self.locationy -= 3
                if event.key == pygame.K_DOWN:
                    self.locationy += 3
                
        # def map_border(self):
            # if self.locationx == width:
            #     self.locationx =
                



    
    class Monster(Character):
        def __init__(self):
            self.image = pygame.image.load('images/monster.png').convert_alpha()
            self.locationx = 400
            self.locationy = 400
            self.counter = 0
            self.dead = False
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

        # Calculates if hero caught monster
        distance = math.sqrt(math.pow(monster.locationx - hero.locationx,2) + math.pow(monster.locationy - hero.locationy,2))
        print(distance)
        if distance < 32:
            # stop_game = True
            monster.dead = True
            sounda.play()
            print("You win!")

            
            

        # Draw background

        # screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero.image, (hero.locationx, hero.locationy))
        
        if monster.dead == False:
            screen.blit(monster.image, (monster.locationx, monster.locationy))

        elif monster.dead == True:
            pass
        

        


        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
