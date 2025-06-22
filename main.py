import pygame # type: ignore
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()