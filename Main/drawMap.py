import pygame


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
		self.background = Background(data)

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
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(
            'sprites/grass.png'
            ''), (data.mapWidth//7, data.mapHeight//7))



