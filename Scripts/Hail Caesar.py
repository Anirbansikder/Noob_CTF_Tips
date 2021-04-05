string = input()
shit = "abcdefghijklmnopqrstuvwxyz"
SHIT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26, 0, -1):
    print("rot", 26 - i, ':', end=' ')
    for j in string:
        if j in shit:
            print(shit[shit.index(j) - i], end='')
        elif j in SHIT:
            print(SHIT[SHIT.index(j) - i], end='')
        else:
            print(j, end='')
    print('')