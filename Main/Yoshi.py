import Characters
import pygame
import os
import math

class Yoshi(Characters.Player):
	def __init__(self, data, pos, name,team):
		Characters.Player.__init__(self,data, pos, name,team)
		x, y = pos
		self.width = 50
		self.height = 50
		self.image = pygame.image.load(
			os.path.join('sprites/yoshi/yoshi_r1.png'))
		self.image = pygame.transform.scale(self.image,
		                                    (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

		self.roll = False
		self.tongue = False
		self.rollState = 0
		self.tongueState = 0
		self.character = 'Yoshi'

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
		self.direct = 'right'

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
		if(self.energy>20):
			self.energy -= 20

			print(self.dest)
			self.dest = self.rollDest

	def ability4(self):
		if(self.energy>5):
			self.energy -= 5

			if(self.tongue): self.tongue = False
			else: self.tongue = True

	def move(self, data, epsilon=6):
	# location command
		destX, destY = self.dest[0], self.dest[1]

		# current location
		x, y = self.pos[0], self.pos[1]

		print(destX, destY)

		dx = destX - x
		dy = destY - y

		xDir, yDir = 1, 1

		if (dx < 0):
			xDir = -1
		if (dy < 0):
			yDir = -1

		if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
			self.roll = False
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

	def animateWalk(self,direction):

		if(self.roll):
			self.rollState+=1
			self.rollState%=7
			if(self.rollState==0):
				self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_s1.png'))
				self.image=pygame.transform.scale(self.image,(self.width,self.height))
				if(direction == 'left'):
					self.image=pygame.transform.flip(self.image, True, False)
			if (self.rollState == 1):
				self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_s2.png'))
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				if (direction == 'left'):
					self.image = pygame.transform.flip(self.image, True, False)
			if (self.rollState == 2):
				self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_s3.png'))
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				if (direction == 'left'):
					self.image = pygame.transform.flip(self.image, True, False)
			if (self.rollState == 3):
				self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_s4.png'))
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				if (direction == 'left'):
					self.image = pygame.transform.flip(self.image, True, False)
			if (self.rollState == 4):
				self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_s5.png'))
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				if (direction == 'left'):
					self.image =pygame.transform.flip(self.image, True, False)
			if (self.rollState == 5):
				self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_s6.png'))
				self.image = pygame.transform.scale(self.image, (self.width, self.height))
				if (direction == 'left'):
					self.image = pygame.transform.flip(self.image, True, False)

		elif(self.tongue):
			self.tongueState += 1
			self.tongueState %= 8

			if(self.movementState=='still'):
				if (self.tongueState == 0):
					self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_t1.png'))
					self.image = pygame.transform.scale(self.image, (self.width, self.height))
					if (direction == 'left'):
						self.image = pygame.transform.flip(self.image, True, False)
				elif (self.tongueState == 1 or self.tongueState == 6):
					self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_t2.png'))
					self.image = pygame.transform.scale(self.image, (self.width*2,self.height))
					if (direction == 'left'):
						self.image = pygame.transform.flip(self.image, True,False)
				elif (self.tongueState == 2 or self.tongueState == 5):
					self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_t3.png'))
					self.image = pygame.transform.scale(self.image,(self.width*3, self.height))
					if (direction == 'left'):
						self.image = pygame.transform.flip(self.image, True,False)
				elif (self.tongueState == 3):
					self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_t4.png'))
					self.image = pygame.transform.scale(self.image,(self.width*4,self.height))
					if (direction == 'left'):
						self.image = pygame.transform.flip(self.image, True,False)
				elif(self.tongueState == 7):
						self.tongue = False

		else:
			self.animationState += 1
			self.animationState %= 7

			if(direction=='right' or direction == 'up'):
				if(self.movementState == 'still'):
					self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_r1.png'))
					self.image=pygame.transform.scale(self.image,(self.width,self.height))
				else:
					if(self.animationState==0):
						self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_r1.png'))
						self.image=pygame.transform.scale(self.image,(self.width,self.height))
					elif(self.animationState==1 or self.animationState == 6):
						self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_r4.png'))
						self.image=pygame.transform.scale(self.image,(self.width,self.height))
					elif(self.animationState==2 or self.animationState == 5):
						self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_r3.png'))
						self.image=pygame.transform.scale(self.image,(self.width,self.height))
					elif(self.animationState==3):
						self.image=pygame.image.load(os.path.join('sprites/yoshi/yoshi_r2.png'))
						self.image=pygame.transform.scale(self.image,(self.width,self.height))

			elif(direction=='left'):
				if (self.movementState == 'still'):
					self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_r1.png'))
					self.image = pygame.transform.scale(self.image,(self.width, self.height))
					self.image = pygame.transform.flip(self.image, True, False)
				else:
					if (self.animationState == 0):
						self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_r1.png'))
						self.image = pygame.transform.scale(self.image, (self.width, self.height))
						self.image = pygame.transform.flip(self.image, True, False)
					elif (self.animationState == 1 or self.animationState == 6):
						self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_r2.png'))
						self.image = pygame.transform.scale(self.image, (self.width, self.height))
						self.image = pygame.transform.flip(self.image, True, False)
					elif (self.animationState == 2 or self.animationState == 5):
						self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_r3.png'))
						self.image = pygame.transform.scale(self.image, (self.width, self.height))
						self.image = pygame.transform.flip(self.image, True, False)
					elif (self.animationState == 3):
						self.image = pygame.image.load(os.path.join('sprites/yoshi/yoshi_r4.png'))
						self.image = pygame.transform.scale(self.image, (self.width, self.height))
						self.image = pygame.transform.flip(self.image, True, False)