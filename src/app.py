import pygame
import random
from src.models.animation_model import Firework
from src.renderers.renderer import Renderer


class App:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Фейерверки - Вариант 1")
        self.clock = pygame.time.Clock()
        self.renderer = Renderer(self.screen)
        self.fireworks = []
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.renderer.render(self.fireworks)
            pygame.display.flip()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if random.random() < 0.03:
            rx = random.randint(100, 700)
            ry = random.randint(100, 400)
            self.fireworks.append(Firework(rx, ry))

        for fw in self.fireworks:
            fw.update()

        self.fireworks = [fw for fw in self.fireworks if fw.is_alive]
