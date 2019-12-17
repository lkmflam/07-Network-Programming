#!/usr/bin/env python 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
 
def convert_integer(): 
	data = 1234 
    # 32-bit 
	print("Original: %s => Long  host byte order: %s, 		Network byte order: %s" %(data, socket.ntohl(data), 		socket.htonl(data))) 
    # 16-bit 
	print("Original: %s => Short  host byte order: %s, 		Network byte order: %s" %(data, socket.ntohs(data), 		socket.htons(data))) 
 
  	
if __name__ == '__main__': 
    convert_integer() 

#Here, we take an integer and show how to convert it between #network and host byte orders. The ntohl() socket class function #converts from the network byte order to host byte order in a #long format. Here, n represents network and h represents host; l #represents long and s represents short, that is, 16-bit.
