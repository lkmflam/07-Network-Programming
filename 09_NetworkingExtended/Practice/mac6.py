#!/usr/bin/env python
#Automated to change the MAC address

import subprocess

#Shows what is changing 
interface = input("Interface > ")
new_mac = input("New MAC > ")

#Shows what the the interface is changing to

print("Changing Mac Changer Address: " + interface + " to " + new_mac)

#Made more secure by taking out the true so no one can inject malicious code here. The brackets help.
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw ether",new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])
