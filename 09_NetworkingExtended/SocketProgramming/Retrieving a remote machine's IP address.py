#!/usr/bin/env python

# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
    
import socket
    
def get_remote_machine_info():
	remote_host = 'www.codinglux.com'
	try:
		print ("IP address of %s: %s" %(remote_host, 			socket.gethostbyname(remote_host)))
	except socket.error as err_msg:
		print ("%s: %s" %(remote_host, err_msg))
    
if __name__ == '__main__':
	get_remote_machine_info()

#This script wraps the gethostbyname() method inside a user-#defined function called get_remote_machine_info(). In this #recipe, we introduced the notion of exception handling. As you #can see, we wrapped the main function call inside a try-except #block. This means that, if some error occurs during the #execution of this function, this error will be dealt with by #this try-except block.
