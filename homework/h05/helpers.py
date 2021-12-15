# https://www.gaussianwaves.com/2013/05/solving-a-triangular-matrix-using-forward-backward-substitution/ 
import numpy as np

def fwd_sub(A, b):
    n = b.size
    x = np.zeros_like(b)

    x[n-1] = b[n-1]/A[n-1, n-1]
    C = np.zeros((n,n))
    for i in range(0, n, 1):
        bb = 0
        for j in range (0, i):
            bb += A[i, j]*x[j]

        C[i, i] = b[i] - bb
        x[i] = C[i, i]/A[i, i]

    return x

def back_sub(A, b):
    n = b.size
    x = np.zeros_like(b)

    x[n-1] = b[n-1]/A[n-1, n-1]
    C = np.zeros((n,n))
    for i in range(n-2, -1, -1):
        bb = 0
        for j in range (i+1, n):
            bb += A[i, j]*x[j]

        C[i, i] = b[i] - bb
        x[i] = C[i, i]/A[i, i]

    return x

def dlu(A):
    U = np.triu(A, 1)
    L = np.tril(A, -1)
    D = np.tril(np.triu(A))

    return D, L, U

def test_back_sub():
    U = np.triu([[4.,12.,-16.],[12.,37.,-43.],[-16.,-43.,98.]])
    y = np.array([1.,2.,3.])         
    x = back_sub(U, y)

    try:
        assert((abs(U@x - y) < 1e-5).all())
        print('Correct!')
    except:
        raise Exception("Incorrect")

def test_fwd_sub():
    L = np.tril([[4.,12.,-16.],[12.,37.,-43.],[-16.,-43.,98.]])
    b = np.array([1.,2.,3.])         
    y = fwd_sub(L, b)

    try:
        assert((abs(L@y - b) < 1e-5).all())
        print('Correct!')
    except:
        raise Exception("Incorrect")

def test_dlu():
    A = np.array([[1,2,3],[2,3,4],[3,4,5]])

    D, L, U = dlu(A)

    print("A: ", A)
    print("D, L, U\n", D, "\n", L, "\n", U)

#test_dlu()
#test_fwd_sub()
#test_back_sub()
