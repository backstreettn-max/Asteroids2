import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Initialize pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyClock = pygame.time.Clock() # Clock to control frame rate and refresh rate
    updatable = pygame.sprite.Group() # All objectst that need to be updated
    drawable = pygame.sprite.Group()  # All sprites that need to be drawn
    asteroids = pygame.sprite.Group() # Asteroids in the game
    shots = pygame.sprite.Group()  # Shots fired by the player
    
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asField = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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
            if a.collides_with(player):
                print("Collision detected!", a.position, player.position)
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
                    # a.kill()
                    
                
                
               
            
        for d in drawable:
            d.draw(screen)

        #Last thing to do in the loop
        pygame.display.flip()
        
       

if __name__ == "__main__":
    main()
