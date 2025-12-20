import circleshape
import constants
import pygame

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
        