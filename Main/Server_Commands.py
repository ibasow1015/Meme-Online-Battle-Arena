import socket
import threading
from queue import Queue

def initClient(data):
	HOST = "128.237.132.204" # put your IP address here if playing on multiple computers
	PORT = 50003
	data.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	data.server.connect((HOST,PORT))
	print("connected to server")

def handleServerMsg(data,server, serverMsg):
  data.server.setblocking(1)
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

def move2Server(data,player,pos):
	msg='%s m %d\n'%(player,pos)
	print('sending:',msg)
	data.server.send(msg.encode())

def interpretServer()