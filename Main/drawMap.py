import pygame


def drawMap(data, display):
	width = 7000
	height = 7000
	data.mapStep = 500

	margin = 20
	baseRad = height * 1//5
	towerRad = height//100

	tower1Color = (0, 0, 255)
	tower2Color = (255, 0, 0)

	pygame.draw.rect(display, (0,255,0), (data.scrollX, data.scrollY, \
	                              width, height))

	pygame.draw.ellipse(display, (0,0,0), (0-baseRad,
	                    height-baseRad//2, baseRad*2, baseRad))
	pygame.draw.ellipse(display, (0, 0, 0), (width-baseRad,
	                                 0-baseRad//2, baseRad*2, baseRad))
	pygame.draw.ellipse(display, tower1Color, (margin-towerRad,
	                    height*3//10-towerRad//2, towerRad*2, \
	                             towerRad))
	pygame.draw.ellipse(display, tower1Color, (margin-towerRad,
	                    height//2-towerRad//2, towerRad*2, towerRad))
	pygame.draw.ellipse(display, tower1Color, (width//2-towerRad,
	                    height-margin-towerRad//2, towerRad*2,
	                                           towerRad))
	pygame.draw.ellipse(display, tower1Color, (width*7//10-towerRad,
	                    height-margin-towerRad//2, towerRad*2,
	                                           towerRad))
	pygame.draw.ellipse(display, tower1Color,(width//2 -
	                                          4*margin-towerRad,
	                    height//2 + 4*margin-towerRad//2, towerRad*2,
	                                          towerRad))
	pygame.draw.ellipse(display, tower1Color, (width//4-towerRad,
	                    height*3//4-towerRad//2, towerRad*2, towerRad))

	pygame.draw.ellipse(display, tower2Color, (width * 3//10-towerRad,
	                    margin-towerRad//2, towerRad*2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width//2-towerRad,
	                    margin-towerRad//2, towerRad*2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width - margin-towerRad,
	                    height//2-towerRad//2, towerRad*2, towerRad))
	pygame.draw.ellipse(display, tower2Color, (width - margin-towerRad,
	                    height*7//10-towerRad//2, towerRad*2,
	                                           towerRad))
	pygame.draw.ellipse(display, tower2Color, (width//2+
	                                           4*margin-towerRad,
	                    height//2- 4*margin-towerRad//2, towerRad*2,
	                                           towerRad))
	pygame.draw.ellipse(display, tower2Color, (width*3//4-towerRad,
	                    height//4-towerRad//2, towerRad*2, towerRad))

def move(data, x, y):
	data.scrollX += x*data.mapStep
	data.scrollY += y*data.mapStep

	print(data.scrollX, data.scrollY)