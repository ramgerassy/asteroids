from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame # type: ignore
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    Shot.containers = (shots,updatable,drawable)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.is_collided(shot):
                    asteroid.split()
                    shot.kill()
                    
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()