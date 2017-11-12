import Characters
import pygame
import os
import math

class Bowser(Characters.Player):
	def __init__(self, data, pos, name):
		Characters.Player.__init__(self,data, pos, name)
		x, y = pos
		self.width=25
		self.height=50
		self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r1.png'))
		self.image=pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.x = x
		self.y = y

		#i hate github

		self.width=50
		self.height=50
		self.fireWidth=30
		self.fireHeight=30

		self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_1.png'))
		self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth,self.fireHeight))
		self.fireRect = self.fireImage.get_rect()
		self.fireRect.center = (x - 5, y)


		self.character='Bowser'

		self.regen=10

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
		self.direct = 'right'

	def getName(self):
		return self.character

	def abilityTimers(self):
		pass

	def ability1(self):
		self.health -= 50
		if (self.health < 0):
			self.health = 0
		self.energy += 50
		if (self.energy > self.maxEnergy):
			self.energy = self.maxEnergy

	def ability2(self):
		if(self.energy>50):
			self.health += 50
			if (self.health > self.maxHealth):
				self.health = self.maxHealth
			self.energy -= 50
			if (self.energy < 0):
				self.energy = 0

	def ability3(self):
		if (self.energy > 10):
			self.energy -= 10
			if(self.fireOn == 'on'):
				self.fireOn = 'off'
			elif(self.fireOn == 'off'):
				self.fireOn = 'on'
			self.fireRect.center = (self.rect.center[0], self.rect.center[1])
			self.x = 0


	def ability3Move(self):
		self.fireState+=1
		self.fireState%=10


		if(self.fireRect.center[0] >= 1280 or self.fireRect.center[0] <= 0):
			self.fireOn = 'off'



		if(self.animationDirection=='left'):
			if(self.fireState==0):
				self.fireImage=pygame.image.load(os.path.join('sprites/fireBall/fire_1.png'))
				self.fireImage=pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 1):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_2.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 2):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_3.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 3):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_4.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 4):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_5.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 5):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_6.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 6):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_7.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 7):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_8.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 8):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_9.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 9):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_10.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
		elif(self.animationDirection == 'right' or self.animationDirection == 'up'):
			if (self.fireState == 0):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_1.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (
				self.fireWidth, self.fireHeight))
			if (self.fireState == 9):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_2.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 8):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_3.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 7):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_4.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 6):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_5.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 5):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_6.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 4):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_7.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 3):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_8.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 2):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_9.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))
			if (self.fireState == 1):
				self.fireImage = pygame.image.load(os.path.join('sprites/fireBall/fire_10.png'))
				self.fireImage = pygame.transform.scale(self.fireImage, (self.fireWidth, self.fireHeight))

	def ability4(self):
		pass


	def getCenter(self):
		return self.rect.center

	def move(self, data, epsilon=6):
		super().move(data, epsilon)
		fdestX, fdestY = self.fireDest[0], self.fireDest[1]
		fx, fy = self.fireRect.center[0], self.fireRect.center[1]
		fdx = fdestX - fx
		fdy = fdestY - fy
		fxDir, fyDir = 1, 1
		if (fdx < 0):
			fxDir = -1
		if (fdy < 0):
			fyDir = -1
		if (fdy < epsilon and fdy > -epsilon and fdx < epsilon and fdx >
				-epsilon):
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

	def animateWalk(self,direction):
		self.animationState+=1
		self.animationState%=7
		if(direction=='right'):
			self.direct='right'

			if(self.movementState=='still'):
				self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r2.png'))
				self.image=pygame.transform.scale(self.image,(self.width,self.height))
				if (self.fireOn == 'on'):
					self.image = pygame.image.load(os.path.join('sprites/bowser/bowser_openMouth.png'))
					self.image = pygame.transform.scale(self.image,(self.width, self.height))
					self.image = pygame.transform.flip(self.image, True, False)
			elif(self.fireOn == 'on'):
				self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_openMouth.png'))
				self.image=pygame.transform.scale(self.image,(self.width,self.height))
				self.image = pygame.transform.flip(self.image, True, False)
			else:
				if(self.animationState==0):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r2.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==1 or self.animationState == 6):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r3.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==2 or self.animationState == 5):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r4.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==3):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_r1.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
		elif(direction=='left'):
			self.direct='left'

			if(self.movementState=='still'):
				self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_l2.png'))
				self.image=pygame.transform.scale(self.image,(self.width,self.height))
				if (self.fireOn == 'on'):
					self.image = pygame.image.load(os.path.join('sprites/bowser/bowser_openMouth.png'))
					self.image = pygame.transform.scale(self.image,(self.width, self.height))
			elif (self.fireOn == 'on'):
				self.image = pygame.image.load(os.path.join('sprites/bowser/bowser_openMouth.png'))
				self.image = pygame.transform.scale(self.image,(self.width, self.height))
			else:
				if(self.animationState==0):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_l2.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==1 or self.animationState == 6):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_l3.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==2 or self.animationState == 5):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_l4.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==3):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_l1.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
		elif(direction=='up'):
			if(self.movementState=='still'):
				self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_uN.png'))
				self.image=pygame.transform.scale(self.image,(self.width,self.height))
			else:
				if(self.animationState==0 or self.animationState==2 or self.animationState==4 or self.animationState==6):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_uR.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				elif(self.animationState==1 or self.animationState==3 or self.animationState==7):
					self.image=pygame.image.load(os.path.join('sprites/bowser/bowser_uL.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))

