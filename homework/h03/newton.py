#!/usr/bin/python
import sys
import warnings
import numpy as np
from tables import make_table

# kekw im just ignoring the warnings about overflow
warnings.filterwarnings('ignore')

# f(x)
def f(x):
   return ((1/(1+np.exp(x))) - .5)

#f'(x)
def df(x):
    return (-1*np.exp(x))/((1+np.exp(x))**2)

# newtons method function implementation
def newtons(x_0, tol=1e-9, max_iter=100):
    x_i = x_0
    i = 0.0
    
    while np.abs(f(x_i)) > tol and i<max_iter:
        x_i = x_i - f(x_i)/df(x_i)
        i += 1

    if (i >= max_iter):
        return np.nan
    else:
        return x_i

# check our work
def main():
    x = np.linspace(-2.5, 2.5, 50)
    y = []
    for x_0 in x:
        j = newtons(x_0)
        y.append(np.abs(np.round(j,4)))
        
    make_table(x,y)

# main decleration
if __name__ == "__main__":        
    main()
