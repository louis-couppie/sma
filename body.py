import random
from pygame.math import Vector2
import core
from sma.CircularFustrum import CircularFustrum
import epidemie


class Body:
    def __init__(self, parent):
        self.parent = parent
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.mass = 10
        self.fustrum = CircularFustrum(self,epidemie.epidemie["dist_contagion"])

        self.vMax = 3
        self.aMax = 3

        self.incubation = 0
        self.contagion = 0
        self.deces = 0

    def move(self, decision):
        if decision.length() > self.aMax:
            decision.scale_to_length(self.aMax)
        self.vitesse += decision
        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        destination = self.position + self.vitesse
        if destination.x > core.WINDOW_SIZE[0] or destination.x < 0:
            self.vitesse.x = -1
            self.acc.x = -1
        if destination.y > core.WINDOW_SIZE[1] or destination.y < 0:
            self.vitesse.y = -1
            self.acc.y = -1
        self.position += self.vitesse

    def update(self):
        # Evolution de la maladie
        if self.contagion < epidemie.epidemie["duree_contagion"]:
            self.contagion += 1
        else:
            self.parent.est_contagieux = True
        if self.incubation < epidemie.epidemie["duree_incubation"]:
            self.incubation += 1
        else:
            if self.parent.est_mourant or random.randint(0,100) < epidemie.epidemie["mortalite"]:
                self.parent.symptome = True
                self.deces += 1
                if self.deces >= epidemie.epidemie["duree_deces"]:
                    self.parent.statut = "D"
        # Contamination
        if self.parent.est_contagieux:
            for b in self.parent.listePerception:
                if b.statut == "S" and random.randint(0, 100) <= epidemie.epidemie["taux_contagion"]:
                    b.statut == "I"