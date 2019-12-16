#!/usr/bin/env python
#Use lsc() to see the available tools in Scapy

import scapy.all as scapy

def scan(ip):
	#Below wants more information about the request
	arp_request = scapy.ARP()
	arp_request.pdst=ip # Will be put in where the IPs are
	print(arp_request.summary())
	scapy.ls(scapy.ARP())

#This is the gateway IP found using route -n
scan("10.128.102.0/24")
#                  ^ Changes it to a range 
