# https://www.gaussianwaves.com/2013/05/solving-a-triangular-matrix-using-forward-backward-substitution/ 
import numpy as np

def fwd_sub(A, b):
    A = np.flipud(A)
    A = np.fliplr(A)
#    b = np.flipud(b)
    b = np.fliplr(b)

    # fwd sub is just upside down and flipped forward sub
    return back_sub(A, b)

def back_sub(A, b):
    x = np.zeros(np.shape(b))
  
    for j in range(len(x)-1, -1, -1):
        sum_k = 0
        for k in range(j+1, len(x)):
            sum_k += A[j][k]*x[k]

        x[j] = (b[j] - sum_k) / A[j][j]

def dlu(A):
    # split
    D = np.diag(np.diag(A))

    L = np.tril(A)
    U = np.triu(A)

    L = np.subtract(L, D)
    U = np.subtract(U, D)

    # check that A = D + L + U
    assert True == np.allclose(A, np.add(np.add(D, L), U)), "yo DLU don't look right"
 
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

#test_dlu()
test_fwd_sub()
#test_back_sub()
