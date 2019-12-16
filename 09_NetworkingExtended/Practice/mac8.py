#!/usr/bin/env python
#Automated to change the MAC address

import subprocess
import optparse

#Adding a function
def change_mac(interface, new_mac):

#Shows what the the interface is changing to
print("Changing Mac Changer Address: " + interface + " to " + new_mac)

#Made more secure by taking out the true so no one can inject malicious code here. The brackets help.
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="add the new MAC address")

(options, arguments)=parser.parse_args()

#Shows what is changing 
change_mac(options.interface, options.new_mac)






