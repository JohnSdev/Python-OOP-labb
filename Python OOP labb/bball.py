import pygame
class BouncingBall:
    def __init__(self, x,y,radius,delta_x,delta_y):
        self.x=x
        self.y=y
        self.radius=radius
        self.delta_y=delta_y
        self.delta_x=delta_x

    def update(self, width, height):
        self.delta_y = self.delta_y + 9
        self.x += self.delta_x
        self.y += self.delta_y

        

        if self.x < 0:
            self.delta_x = -1 * self.delta_x
        elif self.x > width:
            self.delta_x = -1 * self.delta_x

        if self.y < 0:
            self.delta_y = -1 * self.delta_y
        elif self.y > width:
            self.delta_y = -1 * self.delta_y


    def draw(self,screen):
        pos=(int(self.x), int(self.y))
        pygame.draw.circle(screen, (255,255,255), pos, self.radius, 0)
