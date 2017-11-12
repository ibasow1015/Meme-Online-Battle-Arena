import pygame
import math
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, data, pos, name):
        pygame.sprite.Sprite.__init__(self)
        x, y = pos
        self.dest = [x, y]
        self.gold = 200
#<<<<<<< HEAD
        self.pos = [x, y]
#=======
        self.animationState = 0
        self.animationDirection = 'right'
        self.movementState = 'still'
#>>>>>>> e6e575192fe8608703c0ca9e028dd028841b22b1

    def move(self, data, epsilon=6):
        # location command
        destX, destY = self.dest[0], self.dest[1]
        # current location
        """x, y = self.rect.center[0] + data.scrollX, \
               self.rect.center[1] + data.scrollY"""
        x, y = self.pos[0], self.pos[1]
        """print(self.rect.center[0], self.rect.center[1])"""
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
#<<<<<<< HEAD
            #self.rect.center = (x, y)
            self.movementState = 'still'
        elif (dy < epsilon and dy > -epsilon):
            #self.rect.center = (x + self.speed * xDir, y)
            x += self.speed*xDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            #self.rect.center = (x, y + self.speed * yDir)
            y += self.speed*yDir
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
#<<<<<<< HEAD
            #self.rect.center = (x + i, y + j)
            x += i
            y += j
            self.movementState = 'moving'
            if (abs(i) > abs(j) or yDir == 1):
                if (xDir > 0):
                    self.animationDirection = 'right'
                else:
                    self.animationDirection = 'left'
            else:
                self.animationDirection = 'up'

        self.rect.center = (x - data.scrollX, y - data.scrollY)
        self.pos = [x, y]


    def update(self, data):
        self.move(data)
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
    data.player = Bowser.Bowser(data, (50, 50), 'Player1')
    data.players.add(data.player)


def drawCharacter(display, data):
    data.players.update(data)
    data.players.draw(display)
