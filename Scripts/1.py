#!/usr/bin/env python3

from PIL import Image

img = Image.open("flag.png")
w, h = img.size
data = img.load()
seen = [] # to hold the list of pixels present.
seen.append(data[0,0])
for i in range(w):
    for j in range(h):
        color = data[i, j]
        # print(color)
        if (color not in seen):
            seen.append(color)
# print(seen) 
zero = (0,1,1,255)
one = (0,1,2,255)
bin_flag = ""
for i in range(w):
    for j in range(h):
        color = data[i,j]
        if(color == zero):
            bin_flag += "0"
        elif(color == one):
            bin_flag += "1"
#print(bin_flag)
bin_flag = int(bin_flag, 2)
flag = bin_flag.to_bytes((bin_flag.bit_length() + 7) // 8, 'big').decode()
# print(flag)