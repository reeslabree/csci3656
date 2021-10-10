import numpy as np
import pprint
import scipy
import scipy.linalg
import helpers as hp

def solve(A, b):
    # check for symmetric
    is_symmetric = np.allclose(mat, mat.T, rtol=rtol, atol=atol) 

    # if symmetric, solve with cholesky
    if(is_symmetric == True):
        L = scipy.linalg.cholesky(A, lower=True)
        U = scipy.linalg.cholesky(A, lower=False)
        y = hp.fwd_sub(L, b)
        x = hp.back_sub(U, y)

    # if not symmetric, solve with lu decomp
    else:
        P, L, U = scipy.linalg.lu(A)
        y = hp.fwd_sub(L, b)
        x = hp.back_sub(U, y)

    return x
