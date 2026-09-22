"""A tiny Pygame app with a keyboard-controlled icon."""

import pygame


WIDTH = 800
HEIGHT = 600
BACKGROUND = (24, 30, 45)
ICON_COLOR = (70, 190, 255)
ICON_OUTLINE = (225, 245, 255)
SPEED = 300


def draw_icon(screen: pygame.Surface, position: pygame.Vector2) -> None:
    """Draw a small, self-contained icon at the given center position."""
    center = (round(position.x), round(position.y))
    pygame.draw.circle(screen, ICON_OUTLINE, center, 22)
    pygame.draw.circle(screen, ICON_COLOR, center, 18)

    eye_offset = 7
    pygame.draw.circle(
        screen, BACKGROUND, (center[0] - eye_offset, center[1] - 3), 3
    )
    pygame.draw.circle(
        screen, BACKGROUND, (center[0] + eye_offset, center[1] - 3), 3
    )
    pygame.draw.arc(
        screen,
        BACKGROUND,
        (center[0] - 8, center[1] - 2, 16, 12),
        0.2,
        2.9,
        width=2,
    )


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Icon")
    clock = pygame.time.Clock()

    position = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
    running = True

    while running:
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(
            int(keys[pygame.K_RIGHT] or keys[pygame.K_d])
            - int(keys[pygame.K_LEFT] or keys[pygame.K_a]),
            int(keys[pygame.K_DOWN] or keys[pygame.K_s])
            - int(keys[pygame.K_UP] or keys[pygame.K_w]),
        )
        if direction.length_squared() > 0:
            direction = direction.normalize()
            position += direction * SPEED * delta_time

        position.x = max(22, min(WIDTH - 22, position.x))
        position.y = max(22, min(HEIGHT - 22, position.y))

        screen.fill(BACKGROUND)
        draw_icon(screen, position)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
