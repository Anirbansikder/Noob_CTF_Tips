# hill decode
from sage.all import *

def hill_decode(key,ct,n):
    mat = []
    for i in range(0, len(key), n):
        temp = []
        curr = key[i:i+n]
        for ch in curr:
            temp.append(ord(ch) - ord('a'))
        mat.append(temp)
    R = IntegerModRing(26)
    inv_key = matrix(R,mat).inverse()
    msg = ''
    for i in range(0, len(ct), n):
        num_ct = []
        for ch in ct[i:i+n]:
            num_ct.append(ord(ch) - ord('a'))
        vector_ct = vector(num_ct)
        
        pt = inv_key*vector_ct
        for num in pt:
            msg += chr(int(num) + ord('a'))
    return msg

def main():
    pass

if __name__ == "__main__": 
    main()