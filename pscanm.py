#!/usr/bin/python

import socket
from termcolor import colored
from f_text import *
from c_text import *


def portscanner(host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if sock.connect_ex((host,port)):
		print (color_red(f"[-] Port {port} closed"))
	else:
		print (color_green(f"[+] Port {port} open"))


def portscanner_multi(host):
	p_list = [21, 22, 23, 25, 53, 80, 110, 111, 443, 8080]
#	p_list  = range(1, 501)
	one_open = False
	for port in p_list:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if sock.connect_ex((host,port)):
			print (color_red(f"[-] Port {port} closed"))
#			pass
		else:
			print (color_green(f"[+] Port {port} open"))
#			one_open = True

#	if one_open == False:
#		print (color_red('[-] All ports closed/filtered'))


def ps_s3_run():
	print (standard_green('Port\nScan'))
	host = input(color_blue("[*] Enter target host IP: "))
	print (color_yellow('[*] Scanning Top 10 ports ...'))
	portscanner_multi(host)
	input(color_yellow("\n\n[*] Press Enter to return to main menu"))

if __name__ == '__main__':
	ps_s3_run()
