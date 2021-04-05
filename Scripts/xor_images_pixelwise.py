import matplotlib.pyplot as plt
import numpy as np
x = plt.imread(input("Enter 1st file (with path) : "))
y = plt.imread(input("Enter 2nd file (with path) : "))
if len(x.shape) == 3:
    z = [[[] for _ in range(x.shape[1])] for __ in range(x.shape[0])]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            shit = []
            for k in range(x.shape[2]):
                shit.append(x[i][j][k] ^ y[i][j][k])
            z[i][j] = shit[:]
    plt.imshow(z)
else:
    z = np.array([[0 for _ in range(x.shape[1])] for __ in range(x.shape[0])])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i][j] = x[i][j] ^ y[i][j]
plt.imshow(z, cmap="gray")