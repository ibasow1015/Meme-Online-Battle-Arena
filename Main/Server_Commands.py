import socket
import threading
from queue import Queue

HOST=''
PORT=50003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.connect((HOST,PORT))
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

def move2Server(event, data):
	msg=''
	if(event.button==3):
		dest=[event.pos[0]+data.scrollX,event.pos[1]+data.scrollY]
		msg="playerDest to %d\n"%(dest)
	if(msg!=''):
		print('sending msg:',msg)
		data.server.send(msg.encode())