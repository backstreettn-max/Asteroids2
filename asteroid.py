import circleshape
import constants
import pygame
import random
import logger

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid on the screen using the provided screen object
        # Example: screen.draw_circle(self.x, self.y, self.radius)
       pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        # Update the position and state of the asteroid
        # Example: self.x += self.speed * math.cos(self.angle)
        # Example: self.y += self.speed * math.sin(self.angle)
        self.position += self.velocity * dt 
        
    def split(self):
        # Split the asteroid into smaller asteroids
        # Example: new_asteroids = []
        # Example: for _ in range(3):
        # Example:     new_asteroid = Asteroid(self.x, self.y, self.radius / 2)
        # Example:     new_asteroids.append(new_asteroid)
        # Example: return new_asteroids

        # remove the current asteroid
        self.kill()

        # only split if the asteroid is big enough
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        # create two smaller asteroids
        logger.log_event("asteroid_split")
        rando_angle = random.uniform(20, 50)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Two new asteroids
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        
        # Set the new asteroids' velocities to be slightly different from the original
        asteroid1.velocity = pygame.Vector2.rotate(self.velocity, rando_angle) * 1.2
        asteroid2.velocity = pygame.Vector2.rotate(self.velocity, -rando_angle) * 1.2

        
        
       