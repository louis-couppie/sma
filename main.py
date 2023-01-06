import random
import core
from pygame.math import Vector2
from sma.agent import Agent


def computePerception(agent):
    agent.listePerception = []
    for entite in core.memory("agents"):
        if agent.body.fustrum.inside(entite.body) and agent.uuid != entite.uuid:
            agent.listePerception.append(entite)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.move(agent.decision)


def addRandomEntity(self):
    r = random.randint(0, 2)
    if r == 0:
        core.memory("agents").append(Agent())
    elif r == 1:
        core.memory("creeps").append(Creep())
    else:
        core.memory("obstacles").append(Obstacle())

def updateEnv():
    infectes = []
    for a in core.memory("agents"):
        if a.statut == "I":
            infectes.append(a)
    for i in infectes:
        i.body.update()

def contamination(pos_souris):
    pos = Vector2(pos_souris[0], pos_souris[1])
    dmin = 99999999
    infecte = None
    for agent in core.memory("agents"):
        dist = agent.body.position.distance_to(pos)
        if dmin > dist:
            dmin = dist
            infecte = agent
    infecte.statut = "I"



def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 600]

    core.memory("agents", [])

    for i in range(0, 200):
        core.memory("agents").append(Agent())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    if core.getMouseLeftClick():
        contamination(core.getMouseLeftClick())

    # Display
    for agent in core.memory("agents"):
        agent.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()

core.main(setup, run)
