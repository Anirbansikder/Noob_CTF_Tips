# Pscals chemistry Lab
from Crypto.Util.number import *
from gmpy2 import *
def L(x,n):
  return (x-1)//n

g = 
n = 
c = 
def fermat_factors(n):
    assert n % 2 != 0
    a = isqrt(n)
    b2 = square(a) - n
    while not is_square(b2):
        a += 1
        b2 = square(a) - n
    return a + isqrt(b2), a - isqrt(b2)


p, q = fermat_factors(n)

print(p)
print(q)

l = lcm(p-1,q-1)
u = inverse(L(pow(g,l,pow(n,2)),n),n)
flag = b""
flag = long_to_bytes((L(pow(c,l,pow(n,2)),n)*u)%n)
print(flag)