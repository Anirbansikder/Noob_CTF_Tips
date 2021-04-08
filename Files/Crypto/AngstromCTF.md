# Angstrom CTF

1. Script For Finding the XOR when only length of key is known.
    ```python

    from string import printable
    from itertools import cycle, product

    KEY_LENGTH = 5
    FLAG_FORMAT_HINT = "actf"
    INPUT = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"

    input_bytes = bytearray.fromhex(INPUT)

    possible_key_characters = []

    for i in range(KEY_LENGTH):
        input_bytes_group = input_bytes[i::5]
        valid_keys_for_character = []

        for n in range(256):
            if all(chr(n ^ byte) in printable for byte in input_bytes_group):
                valid_keys_for_character.append(n)
        possible_key_characters.append(valid_keys_for_character)

    keys = product(*possible_key_characters)

    for k in keys:
        m = [chr(a ^ b) for a, b in zip(input_bytes, cycle(k))]
        plain = "".join(m)
        if "actf" in plain:
            print(plain)
    ```