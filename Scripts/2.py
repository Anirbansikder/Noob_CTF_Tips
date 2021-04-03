from scapy.all import *

packets = rdpcap('find_me.pcapng')

bytes = (packets[0][Raw].load + packets[1][Raw].load + packets[2][Raw].load + packets[2][Raw].load)
f = open("sample.wav", "wb")
f.write(bytes)
f.close()