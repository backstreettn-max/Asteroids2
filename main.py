import sys
import pygame
import player
import asteroid
import asteroidfield

from email.headerregistry import Group
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyClock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    asField = asteroidfield.AsteroidField()
    new_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        time_passed = pyClock.tick(60) # 60 frames per second
        dt = time_passed / 1000
        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(new_player):
                log_event("player hit")
                print("Game over!")
                sys.exit()
                return True
               
            
        for d in drawable:
            d.draw(screen)

        #Last thing to do in the loop
        pygame.display.flip()
        
       

if __name__ == "__main__":
    main()
