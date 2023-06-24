#!/usr/bin/python

from f_text import *
from rainb_text import *
from c_text import *
from bg1 import bg1_run
from hash import multi_hash
from ssh_cex import ssh_cex_run
from ftp_anon import ftp_anon_run
from mac_finder import *
from pscanm import ps_s3_run
import os

def run_app():
	try:
		while(True):
			print (standard_green('Basic\nToolkit'), color_green('Spw'))
			print (color_blue('\n====== '), color_red('Toolkit_modules'), color_blue(' ======\n'),
			color_green('\n 1. Port_scannner\n 2. Service_banner\n 3. SSH_command_execution\n 4. FTP_anonymous_login \n 5. Multi_hashing\n 6. Mac_finder\n'),
			color_yellow('*. ctrl-c_to_exit\n'),
			color_blue('\n====== '), color_red('Toolkit_modules'), color_blue(' ======\n'))

			choice = input(color_blue('[*] Enter module number: '))
			print ('\n')
			if choice == '1':
				os.system('clear')
				ps_s3_run()
				os.system('clear')
			elif choice == '2':
				os.system('clear')
				bg1_run()
				os.system('clear')
			elif choice == '3':
				os.system('clear')
				ssh_cex_run()
				os.system('clear')
			elif choice == '4':
				os.system('clear')
				ftp_anon_run()
				os.system('clear')
			elif choice == '5':
				os.system('clear')
				multi_hash()
				os.system('clear')
			elif choice == '6':
				os.system('clear')
				mac_finder_run()
				os.system('clear')
			else:
				print (color_red('[*] Invalid Input'))

	except KeyboardInterrupt:
		print (color_red('\n[*] quitting\n'))
		quit()

if __name__ == '__main__':
	run_app()

