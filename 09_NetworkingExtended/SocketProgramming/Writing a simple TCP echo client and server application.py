#!/usr/bin/env python
  
    # This program is optimized for Python 2.7.12 
      and Python 3.5.2.
    # It may run on any other version with/without 
      modifications.
    
    
    import socket
    import sys
    import argparse
    
    host = 'localhost'
    data_payload = 2048
    backlog = 5 
    
    
    def echo_server(port):
        """ A simple echo server """
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, 
                          socket.SOCK_STREAM)
        # Enable reuse address/port 
        sock.setsockopt(socket.SOL_SOCKET, 
                      socket.SO_REUSEADDR, 1)
        # Bind the socket to the port
        server_address = (host, port)
        print ("Starting up echo server  on %s 
                     port %s" % server_address)
        sock.bind(server_address)
        # Listen to clients, backlog argument 
          specifies the max no. 
          of queued connections
        sock.listen(backlog) 
        while True: 
            print ("Waiting to receive message 
                    from client")
            client, address = sock.accept() 
            data = client.recv(data_payload) 
            if data:
                print ("Data: %s" %data)
                client.send(data)
                print ("sent %s bytes back 
                       to %s" % (data, address))
            # end connection
            client.close() 
    
    if __name__ == '__main__':
        parser = argparse.ArgumentParser
        (description='Socket Server Example')
        parser.add_argument('--port', 
        action="store", dest="port", type=int, 
                           required=True)
        given_args = parser.parse_args() 
        port = given_args.port
        echo_server(port)













#After testing with basic socket APIs in Python, let us create a TCP socket server and client now. Here, you #will have the chance to utilize your basic knowledge gained in the previous scripts.

#In this example, a server will echo whatever it receives from the client. We will use the Python argparse #module to specify the TCP port from a command line. Both the server and client script will take this #argument.

#First, we create the server. We start by creating a TCP socket object. Then, we set the reuse address so #that we can run the server as many times as we need. We bind the socket to the given port on our local #machine. In the listening stage, we make sure we listen to multiple clients in a queue using the backlog #argument to the listen() method. Finally, we wait for the client to be connected and send some data to the #server. When the data is received, the server echoes back the data to the client.
