#!/usr/bin/env python
#Automated to change the MAC address

import subprocess
#Shows what is changing 
interface = "eth0"
print("Changing Mac Changer Address: " + interface)

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:33:44:55:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)
