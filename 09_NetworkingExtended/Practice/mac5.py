#!/usr/bin/env python
#Automated to change the MAC address

import subprocess
#Shows what is changing 
interface = input("Interface > ")
new_mac = input("New MAC > ")

#Shows what the the interface is changing to

print("Changing Mac Changer Address: " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig ", shell=True)
