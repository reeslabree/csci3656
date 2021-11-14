import matplotlib.pyplot as plt
import numpy as np
from eprinter import eprint

# local machine epsilon
eps = (7./3 - 4./3 - 1)
e = []

# coeff should be in order from x^0 to x^n
def g(x):
    return (np.sqrt(.75*(x+1)))

# based off of psuedocode from University of Southern Mississippi, Math Department
# long url:         www.math.usm.edu/lambers/mat460/fall09/lecture9.pdf
# bit link form:    bit.ly/3lfp5qs
def fixedpoint(x0, tol=1e-4, maxiter=100):
    k = 0

    while k < maxiter:
        x1 = g(x0)

        if k<10:
            e.append(abs(x1-1.32))

        if abs(x1 - x0) < tol:
            print("FixedPoint Iterations: ", k+1)
            return x1

        x0 = x1
        k += 1

    print("exceeded max iterations")

def main():
    print("Root: ", np.round(fixedpoint(0), 2))
    eprint(e, "Fixed Point Error")

# main def
if __name__ == '__main__':
    main()
