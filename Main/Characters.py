import pygame
import math

class Player(pygame.sprite.Sprite):
	def __init__(self,x,y,name):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.Surface((50,50))
		self.rect=self.image.get_rect()
		self.rect.center=(x,y)
		self.speed=10
		self.dest=(x,y)

	def move(self,epsilon=6):
		destX,destY=self.dest[0],self.dest[1]
		x,y=self.rect.center[0],self.rect.center[1]
		dx=destX-x
		dy=destY-y
		xDir,yDir=1,1
		if(dx<0):
			xDir=-1
		if(dy<0):
			yDir=-1
		if(dy<epsilon and dy>-epsilon and dx<epsilon and dx>-epsilon):
			self.rect.center=(x,y)
		elif(dy<epsilon and dy>-epsilon):
			self.rect.center=(x+self.speed*xDir,y)
		elif(dx<epsilon and dx>-epsilon):
			self.rect.center=(x,y+self.speed*yDir)
		else:
			theta=abs(math.atan(dy/dx))
			i=self.speed*math.cos(theta)*xDir
			j=self.speed*math.sin(theta)*yDir
			self.rect.center=(x+i,y+j)

	def update(self):
		self.move()

def initCharacter(data):
	data.player=Player(50,50,'Player1')
	data.players.add(data.player)

def drawCharacter(display,data):
	data.players.update()
	data.players.draw(display)