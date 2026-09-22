"""Main game loop."""

import pygame

from game import settings
from game.player import Player


def run_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Moving Icon")
    clock = pygame.time.Clock()
    player = Player(pygame.Vector2(settings.WIDTH / 2, settings.HEIGHT / 2))

    running = True
    while running:
        delta_time = clock.tick(settings.FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(pygame.key.get_pressed(), delta_time)
        screen.fill(settings.BACKGROUND)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
