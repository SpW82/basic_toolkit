#!/bin/bash

import ftplib
from c_text import *
from f_text import *

def anonlogin(hostname):
        try:
                ftp = ftplib.FTP(hostname)
                ftp.login('anonymous','anonymous')
                print (color_green(f"[+] {hostname}: FTP Anonymous Login Successful"))
                ftp.quit()
                return True
        except Exception:
                print(color_red(f"[-] {hostname}: FTP Anonymous Login Failed"))

def ftp_anon_run():
	print (standard_green("FTP\nAnonymous\nLogin"))
	host = input(color_blue("[*] Enter target IP: "))
	anonlogin(host)
	input(color_yellow("\n\n[*] Press Enter to return to main menu\n"))

if __name__ == '__main__':
	ftp_anon_run()
