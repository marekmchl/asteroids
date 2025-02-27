import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS,
    PLAYER_TURN_SPEED
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # The game loop
    while True:
        # Makes the windows close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(0)
        updatable.update(delta_time)
        for item in drawable:
            item.draw(screen)

        # Pauses the game loop for 1/60th of a second
        milis = clock.tick(60)
        delta_time = milis / 1000
        # -- end of loop --
        pygame.display.flip()

if __name__ == "__main__":
    main()
