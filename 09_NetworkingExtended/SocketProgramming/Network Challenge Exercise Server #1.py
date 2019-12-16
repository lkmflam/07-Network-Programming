from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''       # blank so any address can be used
PORTNUMBER = 11267  # number for the port
BUFFER = 80         # size of the buffer

DEALER_ADDRESS = (HOSTNAME, PORTNUMBER)
DEALER = Socket(AF_INET, SOCK_STREAM)
DEALER.bind(DEALER_ADDRESS)
DEALER.listen(1)

print('Server waits for the client to connect')
PLAYER, PLAYER_ADDRESS = DEALER.accept()
print('Server accepted connection request from ',\
    PLAYER_ADDRESS)

#The script for the server continues below.

my_password = "Yo Mama"
PASSWORD = my_password.upper()
print('The password is %s' % PASSWORD)

while True:
    print('The server waits for the password to enter')
    GUESS = PLAYER.recv(BUFFER).decode()
    print('dealer received ' + GUESS)
    if GUESS != PASSWORD:
        REPLY = "I'm sorry but that just was not it."
    else:
        REPLY = 'That password is correct! Welcome.'
    PLAYER.send(REPLY.encode())
    if REPLY == 'That password is correct! Welcome.':
        break

DEALER.close()
