#!/usr/bin/env python

from socket import *

#HOST = '127.0.0.1'
HOST = input("Please enter the server name: ")
#PORT = 21567
PORT = int(input("Please enter the port number: "))
BUFSIZ = 1024

ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()
