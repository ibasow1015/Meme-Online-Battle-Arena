import pygame
import math
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.dest = [x, y]
        self.gold = 200
        self.animationState = 0
        self.animationDirection = 'right'
        self.movementState = 'still'

    def move(self, epsilon=6):
        # location command
        destX, destY = self.dest[0], self.dest[1]
        # current location
        x, y = self.rect.center[0], self.rect.center[1]
        # distance to travel
        dx = destX - x
        dy = destY - y
        # placeholder for direction
        xDir, yDir = 1, 1
        if (dx < 0):
            xDir = -1
        if (dy < 0):
            yDir = -1
            # do nothing if character is within range to prevent spazzing
        if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
            self.rect.center = (x, y)
            self.movementState = 'still'
        elif (dy < epsilon and dy > -epsilon):
            self.rect.center = (x + self.speed * xDir, y)
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            self.rect.center = (x, y + self.speed * yDir)
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        else:
            # get vector angle
            theta = abs(math.atan(dy / dx))
            # calculate unit vector
            i = self.speed * math.cos(theta) * xDir
            j = self.speed * math.sin(theta) * yDir
            self.rect.center = (x + i, y + j)
            self.movementState = 'moving'
            if (abs(i) > abs(j) or yDir == 1):
                if (xDir > 0):
                    self.animationDirection = 'right'
                else:
                    self.animationDirection = 'left'
            else:
                self.animationDirection = 'up'

    def update(self):
        self.move(15)
        self.animateWalk(self.animationDirection)
        self.health += self.regen
        self.energy += self.regen
        if (self.energy > self.maxEnergy):
            self.energy = self.maxEnergy
        if (self.health > self.maxHealth):
            self.health = self.maxHealth
        self.abilityTimers()

    def setX(self, x):
        self.rect.x += x

    def setY(self, y):
        self.rect.y += y

    def changeDestination(self, dx, dy):
        self.dest[0] += dx
        self.dest[1] += dy

    def getDestination(self):
        return self.dest


class Test(Player):
    def __init__(self, x, y, name):
        Player.__init__(self, x, y, name)
        self.width = 25
        self.height = 50
        self.image = pygame.image.load(os.path.join('sprites/mario_r1.png'))
        self.image = pygame.transform.scale(self.image,
                                            (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = 25
        self.height = 50

        self.regen = 10

        self.health = 600
        self.maxHealth = 600
        self.energy = 600
        self.maxEnergy = 600
        self.speed = 10
        self.armor = 0
        self.regen = 0
        self.damage = 0
        self.magic = 0
        self.resist = 0

        self.ability4Active = False
        self.ability4Time = 0
        self.ability4Timer = 300

        self.ability3Active = False
        self.ability3Time = 0
        self.ability3Timer = 100

    def abilityTimers(self):
        if (self.ability4Active):
            self.ability4Time += 1
            if (self.ability4Time >= self.ability4Timer):
                self.ability4Active = False
                self.ability4Time = 0
                self.armor -= 20
                self.maxHealth -= 600
                self.width = 25
                self.height = 50
                if (self.health > self.maxHealth):
                    self.health = self.maxHealth
        if (self.ability3Active):
            self.ability3Time += 1
            if (self.ability3Time >= self.ability3Timer):
                self.ability3Active = False
                self.ability3Time = 0
                self.armor -= 10
                self.health -= 10
                self.width = 25
                self.height = 50

    def ability1(self):
        self.health -= 50
        if (self.health < 0):
            self.health = 0
        self.energy += 50
        if (self.energy > self.maxEnergy):
            self.energy = self.maxEnergy

    def ability2(self):
        self.health += 50
        if (self.health > self.maxHealth):
            self.health = self.maxHealth
        self.energy -= 50
        if (self.energy < 0):
            self.energy = 0

    def ability3(self):
        self.energy -= 100
        self.ability3Active = True
        self.armor += 10
        self.health += 10
        self.width *= 2
        self.height *= 2

    def ability4(self):
        self.energy -= 200
        self.ability4Active = True
        self.armor += 20
        self.maxHealth += 600
        self.health += 600
        self.width *= 4
        self.height *= 4
    def getCenter(self):
        return self.rect.center

    def animateWalk(self, direction):
        self.animationState += 1
        self.animationState %= 4
        if (direction == 'right'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario_r1.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_r1.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 1):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_r2.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_r3.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_r4.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))

        if (direction == 'left'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario_l1.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_l1.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 1):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_l2.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_l3.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_l4.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
        if (direction == 'up'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario_uN.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0 or self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_u1.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))
                elif (self.animationState == 1 or self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario_u2.png'))
                    self.image = pygame.transform.scale(self.image, (
                    self.width, self.height))


def initCharacter(data):
    data.player = Test(50, 50, 'Player1')
    data.players.add(data.player)


def drawCharacter(display, data):
    data.players.update()
    data.players.draw(display)
