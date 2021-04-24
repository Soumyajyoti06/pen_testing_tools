import pyfiglet
import sys
import socket
import whois
from datetime import datetime
from printy import printy

ascii_banner = pyfiglet.figlet_format("PORT SCANNER by Subhodeep Moitra")
printy(ascii_banner,"rBU")
printy ("The program is written for research purposes. \nFor any type of misusage of this program the author is not responsible...\n ", "rBU")

target = input ("Enter the target host: ")

# Defining a target
if len(sys.argv) == 2:
	
	# translate hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid host name")

# Add Banner
print("-" * 50)
print(f'The {target} IP ADDRESS is {socket.gethostbyname(target)}')
print(whois.whois(target))
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	
	# will scan ports between 1 to 65,535
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n There was an interrupt !!!\n Stopping the program")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Found .... ")
		sys.exit()
except socket.error:
		print("\n Host not responding")
		sys.exit()
