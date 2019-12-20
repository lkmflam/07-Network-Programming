# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces. It will acept whoever is wanting to connect.
PORT = 50111              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	#Instantiates the socket and sets to "s" for use later
    s.bind((HOST, PORT))	#Binds the host and port together. Basically makes this the address of the client
    s.listen(1)		#Means that the server is only listening to one client. Can be multiple though.
    conn, addr = s.accept()	#Sets the accepted socket connection to two variables for use later.
    with conn:
        print('Connected by', addr)	#Prints who connected with. Like the address. 
        while True:	#States that while receiving information (data), it will store in data. 
            data = conn.recv(1024)
            data = data.decode()
            if not data: break	#If no data is received from the client then it will break out of the loop
            print(data) #This will print whatever was received from the client.
            if "a" in data:
                data = data.replace("a", "#")
            if "e" in data:
                data = data.replace("e", "#")
            if "i" in data:
                data = data.replace("i", "#")
            if "o" in data:
                data = data.replace("o", "#")
            if "u" in data:
                data = data.replace("u", "#")
            final = data
            print(final)
            finalstring = final.encode()
            conn.sendall(finalstring) #Will send back what it recieved.
