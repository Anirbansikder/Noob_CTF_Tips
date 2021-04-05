# CRYPTO

## Useful Tips and Resource

1. Learn [SageMath](https://doc.sagemath.org/html/en/tutorial/)
2. Great Writeup for [CRYPTO](https://blog.cryptohack.org/cryptoctf2020)
3. ```from Crypto.Util.number import *``` this contains ```inverse```, ```long_to_bytes```, ```bytes_to_long```

<hr>

### Foobar CTF

1. If you are provided with only e and several cipher text follow this [RSA](https://crypto.stackexchange.com/questions/43583/deduce-modulus-n-from-public-exponent-and-encrypted-data)
2. Now another method to solve, which I applied was that ```(x^e)%N ``` would always remain same if x is same . So I gave unique number to every ct and then assigned alphabets . Now either use [boxentriq](https://www.boxentriq.com/) or [quipquip](https://www.quipqiup.com/) .
3. [Cracking RNGs: Linear Congruential Generators](https://tailcall.net/blog/cracking-randomness-lcgs/) . In the ctf only N and e were given and ENC(flag+next_num) .
Another Guy Explained it well -> [Script](https://github.com/mendung-10-6/ctf-writeups/blob/master/FooBarCTF%202021/intern.md)
4. We Were Given Hill file . Yash's Solution to [HILL](../Scripts/4.py)
5. Script For Pascal's Residue -> [SCRIPT](../Scripts/5.py)