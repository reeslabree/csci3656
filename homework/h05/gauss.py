# https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

import numpy as np
import scipy
import scipy.linalg

def solve(A, b, tol=1e-6):
    # x_0
    x = np.zeros_like(b)

    # split
    D = np.diag(A)
    P, L, U = scipy.linalg.lu(A) 
    L = np.subtract(L, D)
    U = np.subtract(U, D)

    # check that A = D + L + U
    assert(True == np.allclose(A, np.add(np.add(D, L), U)))
    
    for i in range(50):
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new

    return x
