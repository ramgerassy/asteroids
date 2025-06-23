import pygame # type: ignore
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand = random.uniform(20,50)
        ast_1_angle = self.velocity.rotate(rand)
        ast_2_angle = self.velocity.rotate(-rand)
        ast_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x,self.position.y,ast_radius)
        ast_2 = Asteroid(self.position.x,self.position.y,ast_radius)
        ast_1.velocity = ast_1_angle*1.2
        ast_2.velocity = ast_2_angle*1.2