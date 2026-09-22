"""The player icon and its movement."""

import pygame

from game import settings


class Player:
    """A small icon that can move within the game window."""

    def __init__(self, position: pygame.Vector2) -> None:
        self.position = position

    def update(self, keys: pygame.key.ScancodeWrapper, delta_time: float) -> None:
        direction = pygame.Vector2(
            int(keys[pygame.K_RIGHT] or keys[pygame.K_d])
            - int(keys[pygame.K_LEFT] or keys[pygame.K_a]),
            int(keys[pygame.K_DOWN] or keys[pygame.K_s])
            - int(keys[pygame.K_UP] or keys[pygame.K_w]),
        )
        if direction.length_squared() > 0:
            self.position += direction.normalize() * settings.SPEED * delta_time

        self.position.x = max(
            settings.ICON_RADIUS,
            min(settings.WIDTH - settings.ICON_RADIUS, self.position.x),
        )
        self.position.y = max(
            settings.ICON_RADIUS,
            min(settings.HEIGHT - settings.ICON_RADIUS, self.position.y),
        )

    def draw(self, screen: pygame.Surface) -> None:
        center = (round(self.position.x), round(self.position.y))
        pygame.draw.circle(screen, settings.ICON_OUTLINE, center, settings.ICON_RADIUS)
        pygame.draw.circle(
            screen, settings.ICON_COLOR, center, settings.ICON_RADIUS - 4
        )

        eye_offset = 7
        pygame.draw.circle(
            screen, settings.BACKGROUND, (center[0] - eye_offset, center[1] - 3), 3
        )
        pygame.draw.circle(
            screen, settings.BACKGROUND, (center[0] + eye_offset, center[1] - 3), 3
        )
        pygame.draw.arc(
            screen,
            settings.BACKGROUND,
            (center[0] - 8, center[1] - 2, 16, 12),
            0.2,
            2.9,
            width=2,
        )
