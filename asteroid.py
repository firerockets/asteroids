from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)

        asteroid1.velocity = vect1
        asteroid1.velocity = vect1 * 1.2

        asteroid2.velocity = vect2
        asteroid2.velocity = vect2 * 1.2
        
