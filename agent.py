import random
from pygame.math import Vector2
from agario.body import Body
from agario.creep import Creep


class Agent:
    def __init__(self):
        self.body = Body()
        self.listePerception = []
        self.uuid = random.randint(100000000, 999999999999999)
        self.decision = Vector2()

    def filtre_perception(self):
        creeps = []
        obstacles = []
        proies = []
        predateurs = []
        for entite in self.listePerception:
            if isinstance(entite, Agent):
                if entite.body.mass > self.body.mass:
                    predateurs.append(entite)
                else:
                    proies.append(entite)
            elif isinstance(entite, Creep):
                creeps.append(entite)
            else:
                obstacles.append(entite)
        return proies, predateurs, obstacles, creeps

    def update(self):
        proies, predateurs, obstacles, creeps = self.filtre_perception()

        if proies == [] and predateurs == [] and obstacles == [] and creeps == []:
            self.decision = Vector2(random.randint(-2, 2), random.randint(-2, 2))
            return

        res = Vector2(0, 0)
        for creep in creeps:
            pass
        for proie in proies:
            pass
        for obstacle in obstacles:
            pass
        for pred in predateurs:
            pass
        self.decision = Vector2(random.randint(-2, 2), random.randint(-2, 2))


        # for E in aEviter:
        #     if isinstance(E, Agent):
        #         res += self.body.position - E.body.position
        #     else:
        #        res += self.body.position - E.position
        # for M in aManger:
        #     if isinstance(M, Agent):
        #        res += M.body.position - self.body.position
        #    else:
        #        res += M.position - self.body.position
        # if len(aManger) != 0 or len(aEviter) != 0:
        #    res /= len(aManger) + len(aEviter)
        # self.decision = res

    def show(self):
        self.body.draw()
