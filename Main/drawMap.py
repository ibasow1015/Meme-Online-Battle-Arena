import pygame
import ChainChomp
import os


class Map(object):
	def __init__(self, data, width, height, offset):
		#def drawMap(data, display, width, height):
		# map dimensions
		self.width = width
		self.height = height
		self.sx = offset[0]
		self.sy = offset[1]

		self.margin = 100
		self.baseRad = height * 1 // 5
		self.towerRad = height // 100

		self.tower1Color = (0, 0, 255)
		self.tower2Color = (255, 0, 0)

		self.imgwidth = data.mapWidth//7
		self.imgheight = data.mapHeight//7
		self.background = Background()

		# Draw the whole map

	def drawMap(self, display):
		# Draws bases
		pygame.draw.ellipse(display, (153, 50, 204),
						(0 - self.baseRad - self.sx,
						 self.height - self.baseRad // 2 - self.sy,
						 self.baseRad * 2, self.baseRad))
		pygame.draw.ellipse(display, (153, 50, 204),
						(self.width - self.baseRad - self.sx,
						 0 - self.baseRad // 2 - self.sy,
						 self.baseRad * 2, self.baseRad))

		# Draws blue towers
		pygame.draw.ellipse(display, self.tower1Color,
					(self.margin - self.towerRad - self.sx,
					self.height * 3 // 10 - self.towerRad // 2 - self.sy,
					self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower1Color,
					(self.margin - self.towerRad - self.sx,
					 self.height // 2 - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower1Color,
					(self.width // 2 - self.towerRad - self.sx,
					 self.height-self.margin - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower1Color,
					(self.width * 7 // 10 - self.towerRad - self.sx,
					 self.height-self.margin - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower1Color,
					(self.width// 2 - 4 * self.margin - self.towerRad - self.sx,
					 self.height // 2 + 4 * self.margin - \
					 self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower1Color,
					(self.width // 4 - self.towerRad - self.sx,
					 self.height * 3 // 4 - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))

		# Draws red towers
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width * 3 // 10 - self.towerRad - self.sx,
					 self.margin - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width // 2 - self.towerRad - self.sx,
					 self.margin - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width - self.margin - self.towerRad - self.sx,
					 self.height // 2 - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width - self.margin - self.towerRad - self.sx,
					 self.height * 7 // 10 - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width // 2 + 4 * self.margin - self.towerRad -self.sx,
					 self.height // 2 - 4 * self.margin -\
					 self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		pygame.draw.ellipse(display, self.tower2Color,
					(self.width * 3 // 4 - self.towerRad - self.sx,
					 self.height // 4 - self.towerRad // 2 - self.sy,
					 self.towerRad * 2, self.towerRad))
		for i in range(7):
			for j in range(7):
				display.blit(self.background.image,
						 (0 - self.sx + self.imgwidth * i, 0 - self.sy + self.imgheight * j, self.imgwidth,
							  self.imgheight))



def move(data, x, y):
  # x, y is either 0 or 1 or -1
  data.scrollX += x * data.mapStep
  data.scrollY += y * data.mapStep


class Background(pygame.sprite.Sprite):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.road_h=pygame.image.load(os.path.join('sprites/grass_road_h.png'))
      self.road_h=pygame.transform.scale(self.road_h,(1000,1000))
      self.road_c3=pygame.image.load(os.path.join('sprites/grass_road_c3.png'))
      self.road_c3=pygame.transform.scale(self.road_c3,(1000,1000))
      self.road_c4=pygame.image.load(os.path.join('sprites/grass_road_c4.png'))
      self.road_c4=pygame.transform.scale(self.road_c4,(1000,1000))
      self.road_c1=pygame.image.load(os.path.join('sprites/grass_road_c1.png'))
      self.road_c1=pygame.transform.scale(self.road_c1,(1000,1000))
      self.road_c2=pygame.image.load(os.path.join('sprites/grass_road_c2.png'))
      self.road_c2=pygame.transform.scale(self.road_c2,(1000,1000))
      self.road_d=pygame.image.load(os.path.join('sprites/grass_road_d.png'))
      self.road_d=pygame.transform.scale(self.road_d,(1000,1000))
      self.road_du=pygame.image.load(os.path.join('sprites/grass_road_du.png'))
      self.road_du=pygame.transform.scale(self.road_du,(1000,1000))
      self.road_dd=pygame.image.load(os.path.join('sprites/grass_road_dd.png'))
      self.road_dd=pygame.transform.scale(self.road_dd,(1000,1000))
      self.road_vdl=pygame.image.load(os.path.join('sprites/grass_road_vdl.png'))
      self.road_vdl=pygame.transform.scale(self.road_vdl,(1000,1000))
      self.road_vdr=pygame.image.load(os.path.join('sprites/grass_road_vdr.png'))
      self.road_vdr=pygame.transform.scale(self.road_vdr,(1000,1000))
      self.road_hdd=pygame.image.load(os.path.join('sprites/grass_road_hdd.png'))
      self.road_hdd=pygame.transform.scale(self.road_hdd,(1000,1000))
      self.road_hdu=pygame.image.load(os.path.join('sprites/grass_road_hdu.png'))
      self.road_hdu=pygame.transform.scale(self.road_hdu,(1000,1000))
      self.road_v=pygame.image.load(os.path.join('sprites/grass_road_v.png'))
      self.road_v=pygame.transform.scale(self.road_v,(1000,1000))
      self.default=pygame.transform.scale(pygame.image.load(
          'sprites/grass.png'
          ''), (1000, 1000))
      self.image = self.default

def drawBoard(data, display):

  sx = data.scrollX
  sy = data.scrollY

  for i in range(7):
      for j in range(7):
          if(i==j and i==0):
            data.backGround.image=data.backGround.road_c3
          elif(i+j==6 and j==0):
            data.backGround.image=data.backGround.road_c2
          elif(i+j==6 and j==6):
            data.backGround.image=data.backGround.road_c1
          elif(i==j and i==6):
            data.backGround.image=data.backGround.road_c4
          elif(i+j==5 and j==0):
            data.backGround.image=data.backGround.road_hdu
          elif(i+j==7 and i==1):
            data.backGround.image=data.backGround.road_hdd
          elif(i+j==7 and j==1):
            data.backGround.image=data.backGround.road_vdr
          elif(i+j==5 and j==5):
            data.backGround.image=data.backGround.road_vdl
          elif(i+j==5):
            data.backGround.image=data.backGround.road_du
          elif(i+j==7):
            data.backGround.image=data.backGround.road_dd
          elif(i+j==6):
            data.backGround.image=data.backGround.road_d
          elif(j==0 or j==6):
            data.backGround.image=data.backGround.road_h
          elif(i==0 or i==6):
            data.backGround.image=data.backGround.road_v
          else:
            data.backGround.image = data.backGround.default
          display.blit(data.backGround.image,(0 - sx + 1000 * i, 0 - sy + 1000 * j, 1000, 1000))

