#!/usr/bin/python

# Using Python2
# Created by Venujan Malaiyandi 
# First Iteration of a simple port scanner
# To check for a single port
# Using socket library 


# importing libraries 
import socket

# Create socket objects with IPv4 and TCP protocol
socketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Defualt Time as 2 seconds
socket.setdefaulttimeout(2)

# Declaring host and port details
host = raw_input("[*] Enter The Host To Scan: ")
port = int(raw_input("[*] Enter The Port To Scan: "))


# Defining portscanner function
def scanPort(port):
	if socketA.connect_ex((host, port)):
		print "Port %d is closed" % (port)
	else:
		print "Port %d is opened" % (port)

scanPort(port)
