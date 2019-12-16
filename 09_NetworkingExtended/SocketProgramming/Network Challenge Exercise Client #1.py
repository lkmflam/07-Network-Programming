from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 11267      # same port number
BUFFER = 80             # size of the buffer

DEALER = (HOSTNAME, PORTNUMBER)
PLAYER = Socket(AF_INET, SOCK_STREAM)
PLAYER.connect(DEALER)

#The player is prompted for a guess until the secret number is found. The script for the player #then continues below:

print('player is ready to guess')
while True:
    bestguess = input('Give Password : ')
    GUESS = bestguess.upper()
    PLAYER.send(GUESS.encode())
    ANSWER = PLAYER.recv(BUFFER).decode()
    print('>', ANSWER)
    if ANSWER == 'That password is correct! Welcome.':
        break

PLAYER.close()
