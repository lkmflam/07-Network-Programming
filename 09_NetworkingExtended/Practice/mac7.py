#!/usr/bin/env python
#Automated to change the MAC address

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="add the new MAC address")

(options, arguments)=parser.parse_args()

#Shows what is changing 
interface = options.interface
new_mac = options.new_mac

#Shows what the the interface is changing to

print("Changing Mac Changer Address: " + interface + " to " + new_mac)

#Made more secure by taking out the true so no one can inject malicious code here. The brackets help.
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])

# Type: "python3 mac7.py - i eth1 -m 00:10:20:30:40:50" to use

