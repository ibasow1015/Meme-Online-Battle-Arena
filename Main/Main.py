import pygame, sys
from pygame.locals import *
import Characters
import UI
import icons
import Minions
import drawMap


def init(data):
    data.unit = data.width / 100
    data.players = pygame.sprite.Group()
    Characters.initCharacter(data)
    data.minions = Minions.Minions()
    data.minion = Minions.Minion((100, 30), data)
    data.minions.add(data.minion)
    data.timer = 0
    icons.initIcons(data)
    data.scrollX = data.scrollY = 0
    data.mapStep = 20


def mouseDown(event, data):
    if (event.button == 3):
        data.player.dest = [event.pos[0] + data.scrollX,\
                            event.pos[1] + data.scrollY]


def mouseUp(event, data):
    pass

def keypress(data):
    keys = pygame.key.get_pressed()
    x, y = 0, 0
    if keys[pygame.K_w]:
        y += -1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x += -1
    if keys[pygame.K_d]:
        x += 1
    drawMap.move(data, x, y)


def keyDown(event, data):
    # print(event.key)

    # print(data.scrollX)

    if (event.unicode == '1'):
        data.player.ability1()
    if (event.unicode == '2'):
        data.player.ability2()
    if (event.unicode == '3'):
        data.player.ability3()
    if (event.unicode == '4'):
        data.player.ability4()


def keyUp(event, data):
    if (event.key == 273):
        data.downPressed = False


def timerFired(data):
    data.timer += 250
    data.minions.update(data.timer, data)
    pass


def redrawAll(display, data):
    drawMap.drawBoard(data, display)
    drawMap.drawMap(data, display)
    Characters.drawCharacter(display, data)
    data.minions.drawMinions(display)
    UI.drawTaskbar(display, data)
    icons.drawIcons(display, data)


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
    data.font = pygame.font.SysFont("helvetica", 15)
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

        keypress(data)

        timerFiredWrapper(display, data)


run(1280, 720)
