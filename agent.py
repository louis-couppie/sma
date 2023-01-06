import random
import core
from pygame.math import Vector2
from sma.body import Body


class Agent:
    def __init__(self):
        self.body = Body(self)
        self.listePerception = []
        self.uuid = random.randint(100000000, 999999999999999)
        self.decision = Vector2()

        self.statut = "S"
        self.est_contagieux = False
        self.est_mourant = False
        self.symptome = False

    def filtre_perception(self):
        listeInfectee = []
        for a in self.listePerception:
            if a.statut == "I" and a.symptome:
                listeInfectee.append(a)
        return listeInfectee


    def update(self):
        self.decision = Vector2(random.randint(-3, 3), random.randint(-3, 3)) # Comportement aléatoire

    def show(self):
        if self.statut == "S":
            core.Draw.circle((0, 0, 255), self.body.position, 5)
        elif self.statut == "I":
            core.Draw.circle((255, 0, 0), self.body.position, 5)
        elif self.statut == "R":
            core.Draw.circle((0, 255, 0), self.body.position, 5)