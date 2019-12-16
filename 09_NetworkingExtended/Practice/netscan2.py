#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	
	arp_request = scapy.ARP(pdst=ip)
	arp_request.show()
	#scapy.Ether()
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast.show()
	arp_request_broadcast = broadcast/arp_request
	#scapy.ls(scapy.Ether()) #Get information
	arp_request_broadcast.show()
	#print(broadcast.summary())

scan("10.128.102.0/24")
