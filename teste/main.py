import numpy as np


def Lagrange(arrX, arrY, valorInterP=[]):

    arrX = np.array(arrX, dtype='float64')
    arrY = np.array(arrY, dtype='float64')

    coef = []
    for i in range(len(valorInterP)):

        for k in range(len(arrX)):
            L = 1
            for j in range(len(arrX)):
                if k != j:
                    L = L * (valorInterP[i] - arrX[j]) / (arrX[k] - arrX[j])
                    # print(L)
            coef.append(L)

    aux = np.array(coef)
    return aux


xx = np.linspace(-0.5, 3.25)

x = [0, 1, 2, 3]
y = [1, 6, 5, -8]

arr = Lagrange(x, y, xx)
print(arr)
