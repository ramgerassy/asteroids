import pygame # type: ignore
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE,PLAYER_RADIUS
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()