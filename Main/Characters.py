import pygame
import math


class Player(pygame.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self, data, pos, name):
        pygame.sprite.Sprite.__init__(self)
        x, y = pos
        self.dest = [x, y]
        self.gold = 200
        self.pos = [x, y]
        self.animationState = 0
        self.animationDirection = 'right'
        self.movementState = 'still'

    def move(self, data, epsilon=6):
        # location command
        destX, destY = self.dest[0], self.dest[1]
        # current location
        x, y = self.pos[0], self.pos[1]
        dx = destX - x
        dy = destY - y
        xDir, yDir = 1, 1
        if (dx < 0):
            xDir = -1
        if (dy < 0):
            yDir = -1
        if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
            self.movementState = 'still'
        elif (dy < epsilon and dy > -epsilon):
            x += self.speed * xDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            y += self.speed * yDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'

        else:
            theta = abs(math.atan(dy / dx))
            # calculate unit vector
            i = self.speed * math.cos(theta) * xDir
            j = self.speed * math.sin(theta) * yDir
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
=======
	def __init__(self, data, pos, name):
	    pygame.sprite.Sprite.__init__(self)
	    x, y = pos
	    self.dest = [x, y]
	    self.gold = 200
	    self.pos = [x, y]
	    self.animationState = 0
	    self.animationDirection = 'right'
	    self.movementState = 'still'
	    self.name=name

	def move(self, data, epsilon=6):
	    # location command
	    destX, destY = self.dest[0], self.dest[1]
	    # current location
	    x, y = self.pos[0], self.pos[1]
	    dx = destX - x
	    dy = destY - y
	    xDir, yDir = 1, 1
	    if (dx < 0):
	        xDir = -1
	    if (dy < 0):
	        yDir = -1
	    if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
	        self.movementState = 'still'
	    elif (dy < epsilon and dy > -epsilon):
	        x += self.speed * xDir
	        if (xDir > 0):
	            self.animationDirection = 'right'
	        else:
	            self.animationDirection = 'left'
	    elif (dx < epsilon and dx > -epsilon):
	        y += self.speed * yDir
	        if (xDir > 0):
	            self.animationDirection = 'right'
	        else:
	            self.animationDirection = 'left'

	    else:
	        theta = abs(math.atan(dy / dx))
	        # calculate unit vector
	        i = self.speed * math.cos(theta) * xDir
	        j = self.speed * math.sin(theta) * yDir
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

	def update(self, display,data):
		self.move(data)
		self.animateWalk(self.animationDirection)
		self.health += self.regen
		self.energy += self.regen
		if (self.energy > self.maxEnergy):
		    self.energy = self.maxEnergy
		if (self.health > self.maxHealth):
		    self.health = self.maxHealth
		self.abilityTimers()
		self.drawStatusBars(display,data)

	def drawStatusBars(self,display,data):

		boxX = self.rect.x-10
		HealthboxY = self.rect.y-20
		EnergyboxY = self.rect.y-10
		boxWidth = self.rect.width+20
		healthBoxHeight = 10
		energyBoxHeight=5

		nameLabel=data.font.render(self.name,1,(255,255,255))
		display.blit(nameLabel,(self.rect.x-2,HealthboxY-17))

		pygame.draw.rect(display, (255, 0, 0),
						(boxX, HealthboxY, boxWidth, healthBoxHeight))
		healthPercentage = data.player.health / data.player.maxHealth
		pygame.draw.rect(display, (0, 255, 0),
						(boxX, HealthboxY, boxWidth * healthPercentage, healthBoxHeight))
		for i in range(data.player.maxHealth//100):
			x=boxX+(boxWidth/(data.player.maxHealth/100))*(i+1)
			pygame.draw.line(display,(0,0,0),(x,HealthboxY),(x,HealthboxY+healthBoxHeight))

		pygame.draw.rect(display, (255, 0, 0),
						(boxX, EnergyboxY, boxWidth, energyBoxHeight))
		energyPercentage = data.player.energy / data.player.maxEnergy
		pygame.draw.rect(display, (255, 255, 0),
						(boxX, EnergyboxY, boxWidth * energyPercentage, energyBoxHeight))

		for i in range(data.player.maxEnergy//100):
			x=boxX+(boxWidth/(data.player.maxEnergy/100))*(i+1)
			pygame.draw.line(display,(0,0,0),(x,EnergyboxY),(x,EnergyboxY+energyBoxHeight))
>>>>>>> parent of 3ae0b97... lanes


import Mario
import Bowser


def initCharacter(data):
    data.player = None
    while (data.player == None):
        print('Select character:')
        character = input('-->').lower()
        if (character == 'mario'):
            data.player = Mario.Mario(data, (50, 50), 'Player1')
            break
        elif (character == 'bowser'):
            data.player = Bowser.Bowser(data, (50, 50), 'Player1')
            break
        print('invalid input')
    data.players.add(data.player)


def drawCharacter(display, data):
<<<<<<< HEAD
    data.players.update(data)
=======
    data.players.update(display,data)
>>>>>>> parent of 3ae0b97... lanes
    data.players.draw(display)
