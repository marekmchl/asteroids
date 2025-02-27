import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    while True:
        # Makes the windows close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(0)
        # Pauses the game loop for 1/60th of a second
        milis = clock.tick(60)
        delta_time = milis / 1000
        # -- end of loop --
        pygame.display.flip()

if __name__ == "__main__":
    main()
