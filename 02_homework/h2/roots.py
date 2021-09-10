import matplotlib.pyplot as plt
import numpy as np

# local machine epsilon
eps = (7./3 - 4./3 - 1)

# coeff should be in order from x^0 to x^n
def eval(x, coeff):
    sum = 0
    for i, n in enumerate(coeff):
        sum +=  n * x**i
    return sum

# bisection method for finding roots implementation
def bisection(a, b, coeff, toler):
    
    # check initial condition
    if(eval(a, coeff)*eval(b, coeff) >= 0):
        raise Exception("f(a) * f(b) must be less than zero")

    # enter algorithm
    while (b-a)/2 > toler:
        c = (a+b)/2
        if eval(c, coeff) == 0:
            return c

        if eval(a, coeff)*eval(c, coeff) < 0:
            b = c
        else:
            a = c

    # close approximation of root
    return (a+b)/2

def main():
    coefficients = [-3, -3, 4]
    tolerance = 1e-4
    
    a1 = -1
    b1 = 0
    
    a2 = 1
    b2 = 2

    root1 = np.round(bisection(a1, b1, coefficients, tolerance), 3)
    root2 = np.round(bisection(a2, b2, coefficients, tolerance),3)

    print("Root 1: ", root1, "\nRoot 2: ", root2, "\n")

# main def
if __name__ == '__main__':
    main()
