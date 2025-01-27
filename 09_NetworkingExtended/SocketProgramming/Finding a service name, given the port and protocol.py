#!/usr/bin/env python 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket 
 
def find_service_name(): 
	protocolname = 'tcp' 
	for port in [80, 25]: 
		print ("Port: %s => service name: %s" %(port, 			socket.getservbyport(port, protocolname))) 
     
print ("Port: %s => service name: %s" %(53, 			socket.getservbyport(53, 'udp'))) 
     
if __name__ == '__main__': 
	find_service_name() 

#In this script, the for-in statement is used to iterate over a #sequence of variables. So for each iteration, we use one IP #address to convert them in their packed and unpacked format.
