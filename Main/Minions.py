from pygame import *
import os
import math

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
            for i in range(6):
                x = i * 50 * (side == "right")
                y = i * 50 * (side == "left")
                self.add(Melee((position[0] + x, position[1] + y), destination,
                               side, lane, data))
        if lane == "bottom":
            for i in range(6):
                x = i * 50 * (side == "left")
                y = i * 50 * (side == "right")
                self.add(Melee((position[0] + x, position[1] + y), destination,
                               side, lane, data))
        if lane == "mid":
            for i in range(6):
                x = y = i * 50
                x *= -1 if side == "right" else 1
                y *= -1 if side == "left" else 1
                self.add(Melee((position[0] + x, position[1] + y),
                               destination, side, lane, data))

    def move(self, x, y, data):
        for minion in self.sprites():
            minion.setCenter(x, y, data)


class Minion(sprite.Sprite):
    minions = None

    def __init__(self, startingPosition, destination, data):
        super(Minion, self).__init__()
        self.destination = destination
        self.rect = self.image.get_rect()
        self.rect.center = startingPosition
        self.damageReduction = 0.1
        self.target = None
        self.width = 30
        self.height = 30
        self.hitbox = 25
        self.auto = False
        self.state = 1
        if Minion.minions is not None:
            Minion.minions.add(self)
        else:
            Minion.minions = Minions()
            Minion.minions.add(self)

    def distance(self, other):
        return math.sqrt((self.rect.x - other.rect.x) ** 2 + (self.rect.y -
                                                        other.rect.y) ** 2)
    def inRange(self, other):
        return self.distance(other) <= self.range

    def getTarget(self, data):
        print(len(data.leftMinions.sprites()))
        print(len(data.rightMinions.sprites()))
        if self.side == "right" and self.target is None:
            for target in data.leftMinions.sprites():
                if self.inRange(target):
                    self.destination = target.rect.center
                    self.target = target
                    print(self.destination, self.target)
        elif self.side == "left" and self.target is None:
            for target in data.rightMinions.sprites():
                if self.inRange(target):
                    self.destination = target.rect.center
                    self.target = target
                    print(self.destination, self.target)
    def getHealth(self):
        pass

    def getStructureDamage(self):
        pass

    def getDamage(self):
        pass

    def inBoundaries(self, data):
        if self.side == "left":
            for ally in data.leftMinions.sprites():
                if self.distance(ally) < 4:
                    return True
        elif self.side == "right":
            for ally in data.rightMinions.sprites():
                if self.distance(ally) < 4:
                    return True
        return False

    def update(self, timer, data):
        self.getTarget(data)
        if not timer % 1000:
            if self.target is None:
                self.image = image.load(
                    os.path.join('sprites/Koopa/%s move %s.png' %
                                 (self.side, self.direction)))
                self.image = transform.scale(self.image, (self.width,
                                                          self.height))
                targetX = self.destination[0] - data.scrollX
                targetY = self.destination[1] - data.scrollY
                if self.lane == "top":
                    if self.rect.x > targetX:
                        self.rect.x -= 10
                    if self.rect.y > targetY:
                        self.rect.y -= 10
                if self.lane == "bottom":
                    if self.rect.x < targetX:
                        self.rect.x += 10
                    if self.rect.y < targetY:
                        self.rect.y += 10
                if self.lane == "mid":
                    if self.rect.x > targetX:
                        self.rect.x -= 10
                    if self.rect.y > targetY:
                        self.rect.y -= 10
                    if self.rect.x < targetX:
                        self.rect.x += 10
                    if self.rect.y < targetY:
                        self.rect.y += 10
        if self.target is not None:
            self.autoAttack()


    def setCenter(self, x, y, data):
        self.rect.x += x * data.mapStep
        self.rect.y += y * data.mapStep

    def getValue(self, cs):
        pass

    def autoAttack(self):
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

        self.image = image.load(os.path.join('sprites/Koopa/%s move %s.png' %
                                             (self.side, self.direction)))
        super(Melee, self).__init__(startingPosition, destination, data)
        self.image = transform.scale(self.image, (self.width, self.height))
        self.health = 350
        self.damage = 15
        self.structureDamage = 60
        self.lastHit = 20
        self.assist = 10
        self.range = 5
        self.autoRad = self.range / 2

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

    def autoAttack(self):
        self.state += 1
        self.state %= 7
        self.image = image.load(os.path.join('sprites/Koopa/%s attack %d.png'
                                            % (self.side, self.state)))
        self.image = transform.scale(self.image, (self.width, self.height))
