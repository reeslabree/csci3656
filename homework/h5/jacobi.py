# https://www.quantstart.com/articles/Jacobi-Method-in-Python-and-NumPy/
import numpy as np

def solve(A, b):
    # x_0
    x = np.zeros(len(A[0]))

    # split
    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(25):
         x = (b - np.dot(R, x)) / D

    return x
