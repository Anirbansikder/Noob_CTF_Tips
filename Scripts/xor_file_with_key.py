import sys
f = bytearray(open(input("Enter file with path : "), 'rb').read())
shit = bytearray([int(_) for _ in input("Enter key (integer values of the bytes) : ").split()])
xord_byte_array = bytearray(len(f))
for i in range(len(f)):
    xord_byte_array[i] = f[i] ^ shit[i % len(shit)]
open(input("Enter output file with path : "), 'wb').write(xord_byte_array)