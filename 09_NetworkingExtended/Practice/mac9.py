#!/usr/bin/env python


import subprocess
import optparse


def change_mac(interface, new_mac):

	print("Changing Mac Changer Address: " + interface + " to " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether",new_mac])
	subprocess.call(["ifconfig", interface, "up"])
	subprocess.call(["ifconfig"])

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC address")
	parser.add_option("-m","--mac", dest="new_mac", help="add the new MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		#code to handle error
		parser.error("Please specify an interface, use --help for more details")
	elif not options.new_mac:
		#code to handle error
		parse.error("Please specify a new mac, use --help for more details")
	return options

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
