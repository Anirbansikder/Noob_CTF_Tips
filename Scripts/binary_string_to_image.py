import matplotlib.pyplot as plt
s = input("Enter string : ")
shit = len(s)
l1 = []
for i in range(1, int(shit ** 0.5) + 1):
    if shit % i == 0:
        l1.append(i)
        l1.append(shit // i)
print("Possible images : ")
for i in range(len(l1)):
    print(i + 1, end='. ')
    print(l1[i], shit // l1[i], sep=' x ')
print("Choose : (" + '/'.join([str(_ + 1) for _ in range(len(l1))]) + ') : ')
image = []
choice = l1[int(input()) - 1]
i, j = 0, shit // choice
while(j <= shit):
    image.append([int(_) for _ in list(s[i:j])])
    i, j = j, j + shit // choice
for i in image:
    print(i)
plt.imshow(image, cmap='gray')