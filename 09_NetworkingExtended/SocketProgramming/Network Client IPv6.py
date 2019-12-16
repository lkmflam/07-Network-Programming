#!/usr/bin/env python

import socket
host = "localhost"

mysock=socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
addr=(host,9898)
mysock.connect(addr)

try:
	msg= b"hi, this is a test\n"
	mysock.sendall(msg)
except socket.errno as e:
	print("Socket error ", e)
finally:
	mysock.close()
