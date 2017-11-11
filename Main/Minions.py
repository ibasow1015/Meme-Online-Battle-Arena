from pygame import sprite

class Minions(sprite.Group):
    def __init__(self):
        super(Minions, self).__init__(self)
        self.spawnTimer = 0

    def update(self, timer):
        sprite.Group.update(self, timer)
        self.spawnTimer += timer

    def drawMinions(self, gameMap):
        self.draw(gameMap)

class Minion(sprite.Sprite):
    minions = Minions()
    def __init__(self, startingPosition, *groups):
        super(Minion, self).__init__(*groups)
        self.rect.x = startingPosition[0]
        self.rect.y = startingPosition[1]
        self.damageReduction = 0.1
        self.target = None
        Minion.minions.add(self)

    def getHealth(self):
        pass

    def getStructureDamage(self):
        pass

    def getDamage(self):
        pass

    def update(self, timer, data):
        if not(timer % 1000):
            self.x += data.unit

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
        self.range = data.unit * 3

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