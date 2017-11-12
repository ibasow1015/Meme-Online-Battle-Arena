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

    def spawnMinionWave(self, position, destination, side, lane, data):
        if lane == "top":
            if side == "left":
                self.add(Melee((position[0], position[1] + 5 * 28), destination,
                               side, lane, data, 0))
                self.add(Melee((position[0], position[1] + 4 * 28), destination,
                               side, lane, data, 0))
                self.add(Melee((position[0], position[1] + 3 * 28), destination,
                               side, lane, data, 0))
                self.add(Melee((position[0], position[1] + 2 * 28), destination,
                               side, lane, data, 0))
                self.add(Melee((position[0], position[1] + 1 * 28), destination,
                               side, lane, data, 0))
                self.add(Melee((position[0], position[1] + 0 * 28), destination,
                               side, lane, data, 0))
            else:
                self.add(Melee((position[0] - 5 * 28, position[1]),
                               destination, side, lane, data, 0))
                self.add(Melee((position[0] - 4 * 28, position[1]), destination,
                               side, lane, data, 1))
                self.add(Melee((position[0] - 3 * 28, position[1]),
                               destination, side, lane, data, 2))
                self.add(Melee((position[0] - 2 * 28, position[1]),
                               destination, side, lane, data, 3))
                self.add(Melee((position[0] - 1 * 28, position[1]),
                               destination, side, lane, data, 4))
                self.add(Melee((position[0] - 0 * 28, position[1]),
                               destination, side, lane, data, 5))

    def move(self, x, y, data):
        for minion in self.sprites():
            minion.setCenter(x, y, data)


class Minion(sprite.Sprite):
    minions = Minions()

    def __init__(self, startingPosition, destination, data):
        super(Minion, self).__init__()
        self.destination = destination
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
            minY = self.destination[1] - data.scrollY
            minX = self.destination[1] - data.scrollX
            if self.rect.x > minX:
                self.rect.x -= 6
            if self.rect.y > minY:
                self.rect.y -= 6



    def setCenter(self, x, y, data):
        self.rect.x += x * data.mapStep
        self.rect.y += y * data.mapStep

    def getValue(self, cs):
        pass


class Melee(Minion):
    def __init__(self, startingPosition, destination, side, lane, data,
                 position):
        self.side = side
        self.lane = lane
        if lane == "top":
            self.direction = "up" if self.side == "left" else "left"
        if lane == "mid":
            self.direction = "left" if self.side == "right" else "right"
        if lane == "bottom":
            self.direction = "down" if self.side == "right" else "right"

        self.image = image.load(os.path.join('sprites/Koopa/move %s.png' % (
            self.direction)))
        super(Melee, self).__init__(startingPosition, destination, data)
        self.image = transform.scale(self.image, (self.width, self.height))
        self.health = 350
        self.damage = 15
        self.structureDamage = 60
        self.lastHit = 20
        self.assist = 10
        self.position = position
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
