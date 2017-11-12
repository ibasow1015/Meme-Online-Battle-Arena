from pygame import *
import os


class Minions(sprite.Group):
    def __init__(self):
        super(Minions, self).__init__(self)
        self.spawnTimer = 0

    def update(self, timer, data):
        sprite.Group.update(self, timer, data)
        self.spawnTimer += timer

    def drawMinions(self, gameMap):
        self.draw(gameMap)

    def spawnMinionWave(self, position, side, lane, data):
        self.add(Melee((position[0], position[1] + 5 * 28), side, lane, data))
        self.add(Melee((position[0], position[1] + 4 * 28), side, lane, data))
        self.add(Melee((position[0], position[1] + 3 * 28), side, lane, data))
        self.add(Melee((position[0], position[1] + 2 * 28), side, lane, data))
        self.add(Melee((position[0], position[1] + 1 * 28), side, lane, data))
        self.add(Melee((position[0], position[1] + 0 * 28), side, lane, data))

class Minion(sprite.Sprite):
    minions = Minions()

    def __init__(self, startingPosition, data):
        super(Minion, self).__init__()
        self.rect = self.image.get_rect()
        self.rect.center = startingPosition
        self.damageReduction = 0.1
        self.target = None
        self.speed = data.unit * 2
        self.width = 30
        self.height = 30
        Minion.minions.add(self)

    def getHealth(self):
        pass

    def getStructureDamage(self):
        pass

    def getDamage(self):
        pass

    def update(self, timer, data):
        if not timer % 1000:
            if self.side == "left":
                if self.lane == "top":
                    if self.rect.y > 200 - data.scrollY:
                        self.rect.y -= 6
                    if self.rect.y < 200 - data.scrollY:
                        self.rect.y = 200 - data.scrollY
                    if self.rect.x < 5000 + data.scrollX and self.rect.y <= \
                            200 - data.scrollY:
                        self.direction = "right"
                        self.image = image.load(
                            os.path.join('sprites/Koopa/move %s.png' % (
                                self.direction)))
                        self.image = transform.scale(self.image,
                                                     (self.width, self.height))
                        self.rect.x += 6

    def setX(self, x):
        self.rect.x += x

    def setY(self, y):
        self.rect.y += y

    def getValue(self, cs):
        pass


class Melee(Minion):
    def __init__(self, startingPosition, data, side, lane):
        self.side = side
        self.lane = lane
        if side == "left":
            if lane == "top":
                self.direction = "up"
        self.image = image.load(os.path.join('sprites/Koopa/move %s.png' %(
            self.direction)))
        super(Melee, self).__init__(startingPosition, data)
        self.image = transform.scale(self.image, (self.width, self.height))
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
