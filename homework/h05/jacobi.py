# https://www.quantstart.com/articles/Jacobi-Method-in-Python-and-NumPy/
import numpy as np
from helpers import dlu

def solve(A, b):
    D, L, U = dlu(A)
    x = [1]*len(b)
    x = np.array(np.array(x))
    for i in range(50):
        x=(b-np.dot((L+U), x))/D

    return x
