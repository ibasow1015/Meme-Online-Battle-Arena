from pygame import *
import pygame
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
            for i in range(5):
                x = i * 28 * (side == "left")
                y = i * 28 * (side == "right")
                self.add(Melee((position[0] + x, position[1] + y), destination,
                               side, lane, data))
        if lane == "bottom":
            for i in range(5):
                x = i * 28 * (side == "right")
                y = i * 28 * (side == "left")
                self.add(Melee((position[0] + x, position[1] + y),
                               destination, side, lane, data))

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
            print("Hi")
            minY = self.destination[1] - data.scrollY
            minX = self.destination[1] - data.scrollX
            if self.rect.x < minX:
                self.rect.x -= 6
            if self.rect.y > minY:
                self.rect.y -= 6

    def setCenter(self, x, y, data):
        self.rect.x += x * data.mapStep
        self.rect.y += y * data.mapStep

    def getValue(self, cs):
        pass


class Melee(Minion):
    def __init__(self, startingPosition, destination, side, lane, data):
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
