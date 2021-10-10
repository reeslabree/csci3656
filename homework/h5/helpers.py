import numpy as np

def fwd_sub(A, b):
    x = []
    
    for i in range(len(b)):
        x.append(b[i])
        for j in range(i):
            x[i] -= A[i, j] * x[i]
        x[i] /= A[i,i]
    
    return x

def back_sub(A, b):
    x = np.zeros(np.shape(b))
    
    for i in range(len(b), 0, -1):
        x[i-1] = (b[i-1] - np.dot(A[i-1, i:], x[i:])) / A[i-1, i-1]

    return x
