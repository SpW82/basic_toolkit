#!/usr/bin/python

import socket
from f_text import *
from c_text import *

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def bg1_run():
	print (standard_green("Service\nBanner"))
	ip = input(color_blue("[*] Enter target host IP: "))
	port = int(input(color_blue("[*] Enter target port: ")))
	banner = retBanner(ip,port)
#	banner =  (str(banner).strip('\n'))
	if banner:
#		banner = str(banner.strip("b'"))
#		banner = banner.strip("\r")
		print (color_green("[*] Banner retrieved\n[+]") , color_yellow(f"{ip}/{str(port)} :"), color_green(f"{str(banner.decode())}"))
	else:
		print (color_red("[-] Banner not retrieved"))

	input(color_yellow("\n\n[*] Press Enter to return to main menu\n"))

if __name__ == '__main__':
	bg1_run()
