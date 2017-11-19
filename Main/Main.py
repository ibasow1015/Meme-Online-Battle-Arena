import pygame, sys
from pygame.locals import *
import Characters
import Mario
import Bowser
import Yoshi
import UI
import icons
import Minions
import drawMap
import ChainChomp
import Projectiles
import socket
import threading
from queue import Queue

HOST = "128.237.178.173" # put your IP address here if playing on multiple
# computers
PORT = 50003
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
print("connected to server")


def handleServerMsg(server, serverMsg):
    server.setblocking(1)
    msg = ""
    command = ""
    while True:
        msg += server.recv(10).decode("UTF-8")
        command = msg.split("\n")
        while (len(command) > 1):
            readyMsg = command[0]
            msg = "\n".join(command[1:])
            serverMsg.put(readyMsg)
            command = msg.split("\n")


def init(data):
    data.backGround = drawMap.backGround()
    data.mapWidth = 7000
    data.mapHeight = 7000
    data.unit = data.width / 100
    data.towers = pygame.sprite.Group()
    ChainChomp.initTowers(data)
    data.players = pygame.sprite.Group()
    Characters.initCharacter(data)
    data.leftMinions = Minions.Minions()
    data.rightMinions = Minions.Minions()
    data.leftMinions.spawnMinionWave((500, data.mapHeight * 7 / 8), (500, 500),
                                     "left", "top", data)
    data.rightMinions.spawnMinionWave((data.mapWidth * 7 / 8, 500), (500, 500),
                                      "right", "top", data)
    data.rightMinions.spawnMinionWave((6500, data.mapHeight * 1 / 10),
                                      (6500, 6500),
                                      "right", "bottom", data)
    data.leftMinions.spawnMinionWave((data.mapWidth * 1 / 10, 6500), (6500,
                                                                      6500),
                                     "left", "bottom", data)

    data.rightMinions.spawnMinionWave(
        (data.mapWidth * 7 / 8, data.mapHeight * 1 / 10), (3500, 3500),
        "right", "mid", data
    )
    data.leftMinions.spawnMinionWave(
        (data.mapWidth * 1 / 10, data.mapHeight * 7 / 8), (3500, 3500),
        "left", "mid", data
    )
    data.timer = 0
    icons.initIcons(data)
    data.scrollX = data.scrollY = 0
    data.fireOn = "off"
    data.mapStep = 50
    Projectiles.initProjectiles(data)


def mouseDown(event, data):
    msg=''
    if(event.button==3):
        data.player.autoAttack(data,event.pos)
        
    if (event.button == 3 and data.fireOn == 'off'):
        data.player.dest = [event.pos[0] + data.scrollX,
                            event.pos[1] + data.scrollY]
        #msg+='move %d %d\n'%(event.pos[0]+data.scrollX,event.pos[
        # 1]+data.scrollY)

    if (event.button == 3 and data.fireOn == 'on'):
        data.player.fireDest = list(event.pos)
        if data.player.getName() == "Bowser":
            if data.player.fireOn == 'off':
                data.player.ability3()
        data.fireOn = "off"
        #msg += 'B3 %s\n' % (str(event.pos))

    if (msg != ''):
        print('sending:', msg)
        data.server.send(msg.encode())


def mouseUp(event, data):
    if(event.button==3):
        data.player.autoAttack(data,event.pos)
    if (event.button == 3 and data.fireOn == 'off'):
        data.player.dest = [event.pos[0] + data.scrollX,
							event.pos[1] + data.scrollY]

    if (event.button == 3 and data.fireOn == 'on'):

        if data.player.getName() == "Bowser":
            data.player.fireDest = list(event.pos)
            if data.player.fireOn == 'off':
                data.player.ability3()
        if data.player.getName() == 'Yoshi':
            data.player.rollDest = list(event.pos)
            if data.player.roll:
                data.player.ability3()
        data.fireOn = "off"


def keypress(data):
    keys = pygame.key.get_pressed()
    x, y = 0, 0
    if keys[pygame.K_w] and data.scrollY > -200:
        y += -1
    if keys[pygame.K_s] and data.scrollY < data.mapHeight:
        y += 1
    if keys[pygame.K_a] and data.scrollX > -200:
        x += -1
    if keys[pygame.K_d] and data.scrollX < data.mapWidth:
        x += 1
    drawMap.move(data, x, y)
    data.leftMinions.move(-x, -y, data)
    data.rightMinions.move(-x, -y, data)


def keyDown(event, data):
    msg = ''
    # print(event.key)

    # print(data.scrollX)

    if (event.unicode == '1'):
        data.player.ability1()
        #msg += '%s1\n' % (data.player.letter)
    if (event.unicode == '2'):
        data.player.ability2()
        #msg += '%s2\n' % (data.player.letter)
    if (event.unicode == '3'):
        if data.player.getName() == 'Bowser':
            data.fireOn = 'on'
            #msg += 'B3\n'
        elif data.player.getName() == 'Yoshi':
            data.player.roll = True
        else:
            data.player.ability3()
            #msg += 'M3\n'
    if (event.unicode == '4'):
        data.player.ability4()
        #msg += '%s4\n' % (data.player.letter)

    if (msg != ''):
        print('sending:', msg)
        data.server.send(msg.encode())


def keyUp(event, data):
    pass


def timerFired(data):
    if (serverMsg.qsize() > 0):
        msg = serverMsg.get(False)

        try:
            print("received: ", msg, "\n")
            msg = msg.split()
            command = msg[0]
            print(command)

            if (command == 'newPlayer'):
                newPID = msg[1]
                while (True):
                    print('Select character:')
                    character = input('-->').lower()
                    if (character == 'mario'):
                        user = Mario.Mario(data, (50, 50), newPID, 'red')
                        data.players.add(user)
                        print('player added')
                        break
                    elif (character == 'bowser'):
                        user = Bowser.Bowser(data, (50, 50), newPID, 'blue')
                        data.players.add(user)
                        print('player added')
                        break
                    elif (character == 'yoshi'):
                        user = Yoshi.Yoshi(data, (50, 50), newPID,'blue')
                        data.players.add(user)
                        print('player added')
                        break
                    print('invalid input')
                print(data.players)

            if (command == 'move'):
                x = int(msg[2])
                y = int(msg[3])
                coords = (x, y)
                print('coords:', coords)
                user = msg[1]
                for player in data.players:
                    if(player.name==user):
                        player.dest=[coords[0],coords[1]]

            if (command == 'B1'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'B'):
                        player.ability1()

            if (command == 'B2'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'B'):
                        player.ability2()

            if (command == 'B4'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'B'):
                        player.ability4()

            if (command == 'M1'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'M'):
                        player.ability1()

            if (command == 'M2'):
                print('mario ability 2')
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'M'):
                        player.ability2()

            if (command == 'M3'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'M'):
                        player.ability3()

            if (command == 'M4'):
                user = msg[1]
                for player in data.players:
                    if (player.name == user and player.letter == 'M'):
                        player.ability4()

        except:
            print("failed")
            serverMsg.task_done()

        data.timer += 250
        data.leftMinions.update(data.timer, data)
        data.rightMinions.update(data.timer, data)
        pass

def redrawAll(display, data):
    drawMap.drawBoard(data, display)
    drawMap.drawMap(data, display)
    Characters.drawCharacter(display, data)
    data.leftMinions.drawMinions(display)
    data.rightMinions.drawMinions(display)
    ChainChomp.updateTowers(display, data)
    Projectiles.drawProjectiles(display, data)
    UI.drawTaskbar(display, data)
    icons.drawIcons(display, data)


def run(width=300, height=300, serverMsg=None, server=None):
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
    data.server = server
    data.serverMsg = serverMsg
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


serverMsg = Queue(100)
threading.Thread(target=handleServerMsg, args=(server, serverMsg)).start()

run(1280, 720, serverMsg, server)
