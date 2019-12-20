# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces. It will acept whoever is wanting to connect.
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	#Instantiates the socket and sets to "s" for use later
    s.bind((HOST, PORT))	#Binds the host and port together. Basically makes this the address of the client
    s.listen(1)		#Means that the server is only listening to one client. Can be multiple though.
    conn, addr = s.accept()	#Sets the accepted socket connection to two variables for use later.
    with conn:
        print('Connected by', addr)	#Prints who connected with. Like the address. 
        while True:	#States that while receiving information (data), it will store in data. 
            data = conn.recv(1024)
            if not data: break	#If no data is received from the client then it will break out of the loop
            print(data) #This will print whatever was received from the client.
            vowel = "a", "e", "i", "o", "u"
            for vowel in data:
                data.replace(vowel, "#")
            print(data)
            conn.sendall(data) #Will send back what it recieved.