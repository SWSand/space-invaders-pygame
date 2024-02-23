import pygame


class SpaceShip:

    def __init__(self, image, x, y):
        self.space_ship_surface = pygame.image.load(image)
        self.rect = self.space_ship_surface.get_rect(midbottom=(x, y))
        # self.powered_up_active = False
        # self.powered_up_timer = 0
        self.speed = 5

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.space_ship_surface, self.rect)

    def move(self, direction):
        if direction == "a":
            if self.rect.x >= 20:
                self.rect.x -= self.speed
        if direction == "d":
            if self.rect.x <= 700:
                self.rect.x += self.speed
        if direction == "w":
            if self.rect.y >= 300:
                self.rect.y -= self.speed
        if direction == "s":
            if self.rect.y <= 700:
                self.rect.y += self.speed

    # def speed_up(self):
    #     self.speed += 15
    #     self.powered_up_active = True
    #     self.powered_up_timer = 300

    # def update(self):
    #     pass
        # if self.powered_up > 0 and self.powered_up_active == True:
        #     self.powered_up_timer -= 1

        # if self.powered_up == 0:
        #     self.speed = 5
        #     self.powered_up_active = False
