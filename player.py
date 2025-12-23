from circleshape import CircleShape
import constants
import pygame
import shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt  # Update position based on forward vector and speed

    def shoot(self):
        # Implement shooting logic here
        # For example, create a new shot object and add it to the game's list of shots
        # Return the new shot object or add it to the game's list of shots
        new_shot = shot.Shot(self.position.x, self.position.y)  # Return the new shot object or add it to the game's list of shots
        new_shot.velocity = pygame.Vector2(0, 1)
        new_shot.rotation = self.rotation
        new_shot.velocity *= constants.PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_a]:
            self.rotate(-dt)


        if keys[pygame.K_d]:
            self.rotate(+dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward if the 's' key is pressed