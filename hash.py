#!/usr/bin/python

import hashlib
from c_text import *
from f_text import *

def multi_hash():
	print (standard_green("Multi\nHasher"), color_yellow("Output formats: md5, sha1, sha224, sha256, sha512\n\n"))
	hashvalue = input(color_blue("[*] Enter string to hash: "))
	# md5 hash
	hashjob1 = hashlib.md5()
	hashjob1.update(hashvalue.encode())
	print (color_green("[+] md5:"), hashjob1.hexdigest())

	# SHA1 hash
	hashjob2 = hashlib.sha1()
	hashjob2.update(hashvalue.encode())
	print (color_green("[+] SHA1:"), hashjob2.hexdigest())

	# SHA224
	hashjob3 = hashlib.sha224()
	hashjob3.update(hashvalue.encode())
	print (color_green("[+] SHA224:"), hashjob3.hexdigest())

	# SHA 256
	hashjob4 = hashlib.sha256()
	hashjob4.update(hashvalue.encode())
	print (color_green("[+] SHA256:"), hashjob4.hexdigest())

	# SHA512
	hashjob5 = hashlib.sha512()
	hashjob5.update(hashvalue.encode())
	print (color_green("[+] SHA512:"), hashjob5.hexdigest())

	input(color_yellow("\n\n[*] Press Enter to return to main menu"))

if __name__ == '__main__':
	multi_hash()
