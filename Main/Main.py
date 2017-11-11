import pygame,sys
from pygame.locals import *
import Characters
import UI
import icons

def init(data):
	data.players=pygame.sprite.Group()

	Characters.initCharacter(data)
	icons.initIcons(data)

def mouseDown(event,data):
	if(event.button==3):
		data.player.dest=event.pos

def mouseUp(event,data):
    pass

def keyDown(event,data):
    print(event.key)

def keyUp(event,data):
   	pass

def timerFired(data):
    pass

def redrawAll(display, data):
    Characters.drawCharacter(display,data)
    UI.drawTaskbar(display,data)
    icons.drawIcons(display,data)

def run(width=300, height=300):
	def redrawAllWrapper(display, data):
		display.fill((255,255,255))
		redrawAll(display, data)
		pygame.display.update()  

	def mouseDownWrapper(event, display, data):
		mouseDown(event, data)
		redrawAllWrapper(display, data)

	def mouseUpWrapper(event, display, data):
		mouseUp(event, data)
		redrawAllWrapper(display, data)

	def keyDownWrapper(event, display, data):
		keyDown(event,data)
		redrawAllWrapper(display, data)

	def keyUpWrapper(event, display, data):
		keyUp(event,data)
		redrawAllWrapper(display, data)

	def quit():
		pygame.quit()
		sys.exit()

	def timerFiredWrapper(display, data):
		timerFired(data)
		redrawAllWrapper(display, data)
		data.fpsClock.tick(data.fps)

	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.fps=30 #frames per second
	data.fpsClock=pygame.time.Clock()
	init(data)

	# initialize module and display
	pygame.init()
	data.font=pygame.font.SysFont('helvetica',15)
	display = pygame.display.set_mode((data.width,data.height))
	pygame.display.set_caption('RTS')

	#main loop
	while(True):
		for event in pygame.event.get():
			if(event.type==QUIT):
				quit()
			if(event.type==KEYDOWN):
				keyDownWrapper(event,display,data)
			if(event.type==KEYUP):
				keyUpWrapper(event,display,data)
			if(event.type==MOUSEBUTTONDOWN):
				mouseDownWrapper(event,display,data)
			if(event.type==MOUSEBUTTONUP):
				mouseUpWrapper(event,display,data)
		timerFiredWrapper(display,data)

run(600,600)