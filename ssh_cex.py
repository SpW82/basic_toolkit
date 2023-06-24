#!/usr/bin/python

import pexpect
from c_text import *
from f_text import *

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child,command):
	child.sendline(command)
	child.expect(PROMPT)
	print (f"{color_green('[+] Output:')}\n{child.before.decode()}")

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		print (color_red('[-] Error connecting'))
		return
	if ret == 1:
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if ret == 0:
			print (color_red('[-] Error connecting'))
			return
	child.sendline(password)
	child.expect(PROMPT)
	return child


def ssh_cex_run():
	print (standard_green('SSH\nCmdEX\n'))
	host = input(color_blue("[*] Enter target IP: "))
	user = input(color_blue("[*] Enter username: "))
	password = input(color_blue("[*] Enter password: "))
	cmd = input(color_blue("[*] Enter command to execute: "))
	try:
		child = connect(user,host,password)
		send_command(child, cmd)
	except:
		print(color_red("[*] Wrong username/password"))

	input(color_yellow("[*] Press Enter to return to main menu"))

if __name__ == '__main__':
	ssh_cex_run()
