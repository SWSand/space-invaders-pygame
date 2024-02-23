import pygame
import sys
from ship import SpaceShip
from bullet import Bullet
from alien import Alien
# from alien import AlienBullet

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption('Space Invaders')
        self.clock = pygame.time.Clock()
        # SPACE BACKGROUND  
        self.space_surface = pygame.Surface((800,800))
        # HERO
        self.space_ship = SpaceShip("assets/DurrrSpaceShip.png", 400, 800)
        # BULLET 
        self.all_bullets = pygame.sprite.Group()     #  --------> {}
        # ALIEN
        self.all_aliens = pygame.sprite.Group()
        # EVENT TIMER
        self.enemy_spawn_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_spawn_timer, 500) #second parameter is time in milliseconds
        # POWERUP
        # self.powerup = pygame.sprite.Group()

        # self.powerup_spawn_event = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.powerup_spawn_event, 1000)

        # self.powerup_event = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.powerup_event, 5000)

        # self.powerup_active = False
        # self.powerup_duration = 5000


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                      current_ship_position = self.space_ship.get_position()
                      bullet_object = Bullet(current_ship_position[0]+40, current_ship_position[1])
                      self.all_bullets.add(bullet_object)
                if event.type == self.enemy_spawn_timer:
                      alien_object = Alien()
                      self.all_aliens.add(alien_object)


            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                    self.space_ship.move("a")
            if keys[pygame.K_d]:
                    self.space_ship.move("d")
            if keys[pygame.K_w]:
                    self.space_ship.move("w")
            if keys[pygame.K_s]:
                    self.space_ship.move("s")
        #<--------------------------------------------->
            self.screen.blit(self.space_surface,((0,0)))
            self.space_surface.blit(pygame.image.load("assets/OuterSpace.png"),(0,0))
            self.space_ship.draw(self.space_surface)
            self.all_bullets.draw(self.space_surface)
            self.all_bullets.update(self.all_aliens)
            self.all_aliens.draw(self.space_surface)
            self.all_aliens.update(self.space_surface, self.space_ship)
            # self.powerup.draw(self.space_surface)
            # self.space_ship.update()

            if pygame.sprite.spritecollide(self.space_ship, self.all_aliens, False):
                  pygame.quit()
                  sys.exit()

            # if pygame.sprite.spritecollide(self.space_ship, self.power_up, True):
            #       self.space_ship.speed_up()

            pygame.display.update()
            self.clock.tick(60)
                
my_game = Game()
my_game.run()