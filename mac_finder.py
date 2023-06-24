#!/usr/bin/python

import scapy.all as scapy
from f_text import *
from c_text import *

def get_target_mac(target_ip) -> str:
	arp_request = scapy.ARP(pdst=target_ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	finalpacket = broadcast/arp_request
	answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
	mac = answer[0][1].hwsrc
#	print (color_green(f'Mac : {mac}'))
	return(mac)

def mac_finder_run():
	print (standard_green('Mac\nFinder'))
	print (color_yellow("Must be root to run\n\n"))
	target = input(color_blue('[*] Enter target IP address: '))
	try:
		f_mac = get_target_mac(target)
		print (color_green(f'[*] Mac found: {f_mac}'))
	except:
		print (color_red('[*] Mac not found'))

	input(color_yellow("\n\n[*] Press Enter to return to main menu\n"))

if __name__ == '__main__':
	print (standard_green('Mac\nFinder\n'))
	print (color_yellow("Must be root to run\n"))
	target = input(color_blue('[*] Enter target IP address: '))
	f_mac = get_target_mac(target)
	print (color_green(f'[*] Mac found: {f_mac}'))

