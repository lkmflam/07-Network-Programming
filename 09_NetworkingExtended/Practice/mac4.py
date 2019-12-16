#!/usr/bin/env python
#Automated to change the MAC address

import subprocess
#Shows what is changing 
interface = "eth0"
new_mac = "00:33:44:55:66:77"

#Shows what the the interface is changing to

print("Changing Mac Changer Address: " + interface + " to " + new_mac)

subprocess.call("ifconfig" + interface + " down", shell=True)
subprocess.call("ifconfig" + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)
subprocess.call("ifconfig", shell=True)
