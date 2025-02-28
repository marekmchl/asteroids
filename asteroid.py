import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            child1_vec = self.velocity.rotate(angle)  * 1.2
            child2_vec = self.velocity.rotate(-angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, new_radius)
            child1.velocity = child1_vec
            child2 = Asteroid(self.position.x, self.position.y, new_radius)
            child2.velocity = child2_vec
