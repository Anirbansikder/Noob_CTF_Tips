# ========(In case of binary type input, uncomment and remove line 26)========
# inpt = input()
# another = ''
# for i in range(len(inpt)):
#     if i % 2 == 1:
#         another += inpt[i] + ' '
#     else:
#         another += inpt[i]
# shit = ''
# for i in another.split():
#     if i == '00':
#         shit += 'A'
#     elif i == '10':
#         shit += 'C'
#     elif i == '01':
#         shit += 'G'
#     else:
#         shit += 'T'
# =============================================================================
l1 = []
for i in "ACGT":
    for j in "ACGT":
        for k in "ACGT":
            l1.append(i + j + k)
l2 = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .")
shit = input()
shit2 = ''
for i in range(len(shit)):
    if i % 3 == 2:
        shit2 += shit[i] + " "
    else:
        shit2 += shit[i]
for i in shit2.split():
    print(l2[l1.index(i)], end='')
