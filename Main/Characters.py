import pygame
import math
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.dest = [x, y]
        self.fireDest = [x, y]
        self.gold = 200
        self.animationState = 0
        self.fireState = 0
        self.animationDirection = 'right'
        self.movementState = 'still'
        self.fireOn = 'off'

    def move(self, epsilon=6):
        # location command
        destX, destY = self.dest[0], self.dest[1]
        fdestX, fdestY = self.fireDest[0], self.fireDest[1]
        # current location
        x, y = self.rect.center[0], self.rect.center[1]
        fx, fy = self.fireRect.center[0], self.fireRect.center[1]
        # distance to travel
        dx = destX - x
        dy = destY - y
        fdx = fdestX - fx
        fdy = fdestY - fy

        # placeholder for direction
        xDir, yDir = 1, 1
        fxDir, fyDir = 1, 1
        if (dx < 0):
            xDir = -1
        if (fdx < 0):
            fxDir = -1
        if (dy < 0):
            yDir = -1
        if (fdy < 0):
            fyDir = -1
            # do nothing if character is within range to prevent spazzing
        if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
            self.rect.center = (x, y)
            self.movementState = 'still'
        elif (dy < epsilon and dy > -epsilon):
            self.rect.center = (x + self.speed * xDir, y)
            self.fireRect.center = (fx + self.speed * xDir, fy)
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            self.rect.center = (x, y + self.speed * yDir)
            self.fireRect.center = (fx, fy + self.speed * yDir)
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
            self.fireRect.center = (fx + i, fy + j)
            self.movementState = 'moving'
            if (abs(i) > abs(j) or yDir == 1):
                if (xDir > 0):
                    self.animationDirection = 'right'
                else:
                    self.animationDirection = 'left'
            else:
                self.animationDirection = 'up'

        if (fdy < epsilon and fdy > -epsilon and fdx < epsilon and fdx > -epsilon):
            self.fireRect.center = (fx, fy)
            self.fireOn = 'off'
        elif (fdy < epsilon and fdy > -epsilon):
            self.fireRect.center = (fx + self.speed * fxDir, fy)
            if (fxDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (fdx < epsilon and fdx > -epsilon):
            self.fireRect.center = (fx, fy + self.speed * fyDir)
            if (fxDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        else:
            # get vector angle
            theta = abs(math.atan(fdy / fdx))
            # calculate unit vector
            i = self.speed * math.cos(theta) * fxDir
            j = self.speed * math.sin(theta) * fyDir
            self.fireRect.center = (fx + i, fy + j)
            self.movementState = 'moving'
            if (abs(i) > abs(j) or fyDir == 1):
                if (fxDir > 0):
                    self.animationDirection = 'right'
                else:
                    self.animationDirection = 'left'
            else:
                self.animationDirection = 'up'

    def drawFire(self, display):
        self.ability3Move()

        x, y = self.fireRect[0], self.fireRect[1]

        display.blit(self.fireImage, (x, y))

    def update(self, display):
        if (self.fireOn == 'on'):
            self.drawFire(display)

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

import Mario
import Bowser

def initCharacter(data):
    data.player = Bowser.Bowser(50, 50, 'Player1')
    data.players.add(data.player)


def drawCharacter(display, data):
    data.players.update(display)
    data.players.draw(display)




