import pygame
import os
import math

class ChainChomp(pygame.sprite.Sprite):
    def __init__(self,pos,team):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join('sprites/chain-chomp/chain_chomp_r1.png'))
        self.image=pygame.transform.scale(self.image,(150,150))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.pos=pos
        self.animationState=0
        self.animationDirection='Right'
        self.health=3000
        self.range=1000
        self.damage=200
        self.speed=1
        self.team=team
        self.dest=pos
        self.post=pos

    def update(self,data):
        for player in data.players:
        	if(self.canAttack(player)):
        		self.attack(data,player)
        self.move(data)

    def canAttack(self,player):
        dist=((player.rect.center[0]-self.rect.center[0])**2+(player.rect.center[1]+self.rect.center[1])**2)**.5
        if(dist<=self.range):
            self.destX,self.destY=player.rect.center[0],player.rect.center[1]
        else:
            self.destX,self.destY=self.post[0],self.post[1]

    def attack(self,data,player):
    	if(pygame.sprite.collide_rect(self,player)):
    		player.health-=self.damage

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
            x += self.speed*xDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            y += self.speed*yDir
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
        print(x,y)
        self.pos = [x, y]

def initTowers(data):
    margin = 100
    height = data.mapHeight
    width = data.mapWidth
    towerRad = height // 100

    data.towers.add(ChainChomp((margin - towerRad,
                         height * 3 // 10 - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((margin - towerRad,
                             height // 2 - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((width // 2 - towerRad,
                             height - margin - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((width * 7 // 10 - towerRad,
                             height - margin - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((width // 2 - 4 * margin - towerRad,
                 height // 2 + 4 * margin - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((width // 4 - towerRad,
                             height * 3 // 4 - towerRad // 2),'blue'))
    data.towers.add(ChainChomp((width * 3 // 10 - towerRad,
                             margin - towerRad // 2),'red'))
    data.towers.add(ChainChomp((width // 2 - towerRad,
                             margin - towerRad // 2),'red'))
    data.towers.add(ChainChomp((width - margin - towerRad,
                             height // 2 - towerRad // 2),'red'))
    data.towers.add(ChainChomp((width - margin - towerRad,
                             height * 7 // 10 - towerRad // 2),'red'))
    data.towers.add(ChainChomp((width // 2 + 4 * margin - towerRad,
                 height // 2 - 4 * margin - towerRad // 2),'red'))
    data.towers.add(ChainChomp((width * 3 // 4 - towerRad,
                             height // 4 - towerRad // 2),'red'))

def updateTowers(display,data):
    data.towers.update(data)
    data.towers.draw(display)