# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	#Instantiating the socket as s, just like the server.
    s.connect((HOST, PORT))	#Connects to the host on that port. Kind of like the address.
    s.sendall(input("Please enter the message you would like to send to the server: "))	#Send to other end of socket (receiver) a message saying.
    data = s.recv(1024)	
print('Received', repr(data))	# .repr() is a representation of the string of an object. 
#So, this line will print "Recieved" and the representation of data which is the message that went across.