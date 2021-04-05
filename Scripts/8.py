from scapy.all import *

packets = rdpcap('network2.pcapng')

temp = bytes("",'utf-8')

lmao = packets[66][Raw].load[::-1]

file = open("out.zip","wb")
file.write(lmao)
file.close()