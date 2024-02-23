# import pygame
# import random
# import sys
# from ship import SpaceShip


# class Alien(pygame.sprite.Sprite):

#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.green_alien = pygame.image.load("assets/GreenAlien.png")
#         self.red_alien = pygame.image.load("assets/RedAlien.png")
#         self.yellow_alien = pygame.image.load("assets/YellowAlien.png")
#         self.spawnable_aliens = [self.green_alien,self.red_alien, self.yellow_alien]
#         self.image = self.spawnable_aliens[random.randint(0,2)]
#         self.rect = self.image.get_rect(center = (20,20))
#         self.going_right = True
#         self.shooting_cooldown = random.randint(0,100)
#         self.all_alien_bullets = pygame.sprite.Group()

#     def update(self,screen, space_ship_object):
        
#         if self.going_right == True:
#             self.rect.x += 5
#             if self.rect.x == 760:
#                 self.rect.y +=50
#                 self.going_right = False
#         else:
#             self.rect.x -= 5    
#             if self.rect.x == 0:
#                 self.rect.y += 50
#                 self.going_right = True   

#         self.shooting_cooldown = random.randint(0,100)
        
#         if self.shooting_cooldown == 10:
#             alien_bullet_object = space_ship_object(self.rect.x, self.rect.y)
#             self.all_alien_bullets.add(alien_bullet_object)
#             self.shooting_cooldown = random.randint(0,100)

#         self.all_alien_bullets.draw(screen)
#         self.all_alien_bullets.update(space_ship_object)
