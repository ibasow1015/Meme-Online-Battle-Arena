from pygame import *

class Minions(sprite.Group):
    def __init__(self):
        super(Minions, self).__init__(self)
        self.spawnTimer = 0

    def update(self, timer, data):
        sprite.Group.update(self, timer, data)
        self.spawnTimer += timer

    def drawMinions(self, gameMap):
        self.draw(gameMap)

class Minion(sprite.Sprite):
    minions = Minions()
    def __init__(self, startingPosition, data):
        super(Minion, self).__init__()
        self.image = Surface((data.unit * 5, data.unit * 5))
        self.rect = self.image.get_rect()
        self.rect.center = startingPosition
        self.damageReduction = 0.1
        self.target = None
        self.speed = data.unit * 2
        Minion.minions.add(self)

    def getHealth(self):
        pass

    def getStructureDamage(self):
        pass

    def getDamage(self):
        pass

    def update(self, timer, data):
        if not timer % 1000:
            self.rect.x += data.unit
            self.rect.y += data.unit

    def setX(self, x):
        self.rect.x += x

    def setY(self, y):
        self.rect.y += y

    def getValue(self, cs):
        pass


class Melee(Minion):
    def __init__(self, startingPosition, data):
        super(Melee, self).__init__(startingPosition)
        self.health = 350
        self.damage = 15
        self.structureDamage = 60
        self.lastHit = 20
        self.assist = 10
        self.range = data.unit * 5

    def getHealth(self):
        return self.health

    def getStructureDamage(self):
        return self.structureDamage

    def getDamage(self):
        return self.damage

    def getValue(self, cs):
        if cs:
            return self.lastHit
        return self.assist
