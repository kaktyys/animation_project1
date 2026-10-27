import random
import math

class Particle:
    def __init__(self, x: float, y: float, color: tuple):
        self.x = x
        self.y = y
        self.color = color
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.alpha = 255
        self.life = random.randint(30, 60)

    def update(self):
        gravity = 0.15
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        self.alpha = max(0, int((self.life / 60) * 255))

class Firework:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.particles = [Particle(x, y, self.color) for _ in range(60)]
        self.is_alive = True

    def update(self):
        for p in self.particles:
            p.update()
        self.particles = [p for p in p.particles if p.life > 0]
        if not self.particles:
            self.is_alive = False
