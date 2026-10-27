import pygame


class Renderer:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def render(self, fireworks: list):
        self.screen.fill((10, 10, 20))

        for fw in fireworks:
            for p in fw.particles:
                s = pygame.Surface((6, 6), pygame.SRCALPHA)
                color_with_alpha = (p.color[0], p.color[1], p.color[2], p.alpha)
                pygame.draw.circle(s, color_with_alpha, (3, 3), 3)
                self.screen.blit(s, (int(p.x) - 3, int(p.y) - 3))
