import random
from pygame.math import Vector2
import core
from agario.CircularFustrum import CircularFustrum


class Body:
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.mass = 10
        self.fustrum = CircularFustrum(self)

        self.vMax = 10
        self.aMax = 5
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self, decision):
        if decision.length() > self.aMax:
            decision.scale_to_length(self.aMax)
        self.vitesse += decision
        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)
        self.position += self.vitesse

    def draw(self):
        core.Draw.circle(self.color, self.position, self.mass)
