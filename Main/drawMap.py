import pygame


def drawMap(data, display):
	# map dimensions
	data.mapWidth = 7000
	data.mapHeight = 7000

	height = data.mapHeight
	width = data.mapWidth

	# when use arrow keys
	data.mapStep = 200

	sx = data.scrollX
	sy = data.scrollY

	margin = 100
	baseRad = height * 1 // 5
	towerRad = height // 100

	tower1Color = (0, 0, 255)
	tower2Color = (255, 0, 0)


	#print(grassImage.get_height())

	# Draw the whole map
	#pygame.draw.rect(display, (0, 255, 0), (0 - data.scrollX, 0 - data.scrollY,
										#width, height))




	# Draws bases
	pygame.draw.ellipse(display, (153, 50, 204), (0 - baseRad - sx,
											 height - baseRad // 2 - sy,
											 baseRad * 2, baseRad))
	pygame.draw.ellipse(display, (153, 50, 204), (width - baseRad - sx,
											 0 - baseRad // 2 - sy, baseRad * 2,
											 baseRad))

	# Draws blue towers
	pygame.draw.ellipse(display, tower1Color, (margin - towerRad - sx,
											   height * 3 // 10 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower1Color, (margin - towerRad - sx,
											   height // 2 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower1Color, (width // 2 - towerRad - sx,
											   height - margin - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower1Color, (width * 7 // 10 - towerRad - sx,
											   height - margin - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower1Color,
						(width // 2 - 4 * margin - towerRad - sx,
						 height // 2 + 4 * margin - towerRad // 2 - sy,
						 towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower1Color, (width // 4 - towerRad - sx,
											   height * 3 // 4 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))

	# Draws red towers
	pygame.draw.ellipse(display, tower2Color, (width * 3 // 10 - towerRad - sx,
											   margin - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width // 2 - towerRad - sx,
											   margin - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width - margin - towerRad - sx,
											   height // 2 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width - margin - towerRad - sx,
											   height * 7 // 10 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower2Color,
						(width // 2 + 4 * margin - towerRad - sx,
						 height // 2 - 4 * margin - towerRad // 2 - sy,
						 towerRad * 2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width * 3 // 4 - towerRad - sx,
											   height // 4 - towerRad // 2 - sy,
											   towerRad * 2, towerRad))

def move(data, x, y):
    # x, y is either 0 or 1 or -1
    data.scrollX += x * data.mapStep
    data.scrollY += y * data.mapStep


class backGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(
            'sprites/grass.png'
            ''), (1000, 1000))


def drawBoard(self, display):
    backGround.__init__(self)

    sx = self.scrollX
    sy = self.scrollY

    for i in range(7):
        for j in range(7):
            display.blit(self.image,
                         (0 - sx + 1000 * i, 0 - sy + 1000 * j, 1000, 1000))
