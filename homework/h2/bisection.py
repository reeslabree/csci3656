import matplotlib.pyplot as plt
import numpy as np
from eprinter import eprint

# local machine epsilon
eps = (7./3 - 4./3 - 1)
e = []

# coeff should be in order from x^0 to x^n
def eval(x, coeff):
    sum = 0
    for i, n in enumerate(coeff):
        sum +=  n * x**i
    return sum

# bisection method for finding roots implementation
def bisection(a, b, coeff, toler):
    k = 0

    # check initial condition
    if(eval(a, coeff)*eval(b, coeff) >= 0):
        raise Exception("f(a) * f(b) must be less than zero")

    # enter algorithm
    while (b-a)/2 > toler:
        
        c = (a+b)/2

        if k < 9:
            e.append(abs(c-1.32))

        if eval(c, coeff) == 0:
            return c

        if eval(a, coeff)*eval(c, coeff) < 0:
            b = c
        else:
            a = c

        k += 1

    eprint(e, "Bisection Error")
    print("Bisection Iterations: ", k)
    # close approximation of root
    return (a+b)/2

def main():
    coefficients = [-3, -3, 4]
    tolerance = 1e-4
    
    a = 1
    b = 2
    
    root = np.round(bisection(a, b, coefficients, tolerance), 2)

    print("Root: ", root)

# main def
if __name__ == '__main__':
    main()
