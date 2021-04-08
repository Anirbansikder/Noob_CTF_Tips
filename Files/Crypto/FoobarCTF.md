# FOOBAR CTF

1. If you are provided with only e and several cipher text follow this [RSA](https://crypto.stackexchange.com/questions/43583/deduce-modulus-n-from-public-exponent-and-encrypted-data)
2. Now another method to solve, which I applied was that ```(x^e)%N ``` would always remain same if x is same . So I gave unique number to every ct and then assigned alphabets . Now either use [boxentriq](https://www.boxentriq.com/) or [quipquip](https://www.quipqiup.com/) .
3. [Cracking RNGs: Linear Congruential Generators](https://tailcall.net/blog/cracking-randomness-lcgs/) . In the ctf only N and e were given and ENC(flag+next_num) .
Another Guy Explained it well -> [Script](https://github.com/mendung-10-6/ctf-writeups/blob/master/FooBarCTF%202021/intern.md)
4. We Were Given Hill file . Yash's Solution to Hill ->

    ```python
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
    ```
5. Script For Pascal's Residue ->
    ```python
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
    ```