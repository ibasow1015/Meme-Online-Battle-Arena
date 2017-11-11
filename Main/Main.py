import pygame, sys
from pygame.locals import *
import characters
import Minions
import drawMap

def init(data):
    data.unit = data.width / 100
    data.scrollX = data.scrollY = 0
    data.players = pygame.sprite.Group()
    characters.initCharacter(data)
    data.minions = Minions.Minions()
    pass


def mouseDown(event, data):
    pass

def mouseDown(event,data):
	if(event.button==3):
		data.player.dest=event.pos


def mouseUp(event, data):
    pass


def keyDown(event, data):
    #print(event.key)

    #print(data.scrollX)

    if(event.key == 273):
        drawMap.move(data, 0, -1)
    elif(event.key == 274):
        drawMap.move(data, 0, 1)
    elif(event.key == 276):
        drawMap.move(data, -1, 0)
    elif(event.key == 275):
        drawMap.move(data, 1, 0)

def keyUp(event, data):
    pass


def timerFired(data):
    pass


def redrawAll(display, data):
    drawMap.drawMap(data, display)
    characters.drawCharacter(display,data)


def run(width=300, height=300):
    def redrawAllWrapper(display, data):
        display.fill((255, 255, 255))
        redrawAll(display, data)
        pygame.display.update()

    def mouseDownWrapper(event, display, data):
            mouseDown(event, data)
            redrawAllWrapper(display, data)

    def mouseUpWrapper(event, display, data):
            mouseUp(event, data)
            redrawAllWrapper(display, data)

    def keyDownWrapper(event, display, data):
            keyDown(event, data)
            redrawAllWrapper(display, data)

    def keyUpWrapper(event, display, data):
            keyUp(event, data)
            redrawAllWrapper(display, data)

    def quit():
            pygame.quit()
            sys.exit()

    def timerFiredWrapper(display, data):
            timerFired(data)
            redrawAllWrapper(display, data)
            data.fpsClock.tick(data.fps)

    # Set up data and call init
    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.fps = 30  # frames per second
    data.fpsClock = pygame.time.Clock()
    init(data)

    # initialize module and display
    pygame.init()
    display = pygame.display.set_mode((data.width, data.height))
    pygame.display.set_caption('RTS')

    # main loop
    while (True):
        for event in pygame.event.get():
            if (event.type == QUIT):
                quit()
            if (event.type == KEYDOWN):
                keyDownWrapper(event, display, data)
            if (event.type == KEYUP):
                keyUpWrapper(event, display, data)
            if (event.type == MOUSEBUTTONDOWN):
                mouseDownWrapper(event, display, data)
            if (event.type == MOUSEBUTTONUP):
                mouseUpWrapper(event, display, data)
        timerFiredWrapper(display, data)


run(600, 600)
