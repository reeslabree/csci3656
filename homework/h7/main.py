# Rees LaBree, Homework 7

import math
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# f(x)
def f(x, theta):
    return 1/(1+math.exp(-1*theta*x))

# graphs
def print_graphs(c, theta):
    x = np.linspace(-5, 5, 1000)
    
    y_p = []
    y_f = []
    
    for x_i in x:
        y_p.append(np.polyval(c, x_i))
        y_f.append(f(x_i, theta))

    plt.plot(x, y_p)
    plt.plot(x, y_f)
    plt.show()

# generates the training data
def gen_train_data(theta):
    x = np.linspace(-5, 5, 7)
    y = []

    tab = PrettyTable()
    tab.field_names = ["x_i", "y_i"]

    for x_i in x:
        y_i = f(x_i, theta) 
        y.append(y_i)
        tab.add_row([x_i, y_i])

    print(tab)

    return x, y

# generates the test data
def gen_test_data(theta):
    x = np.linspace(-5, 5, 101)
    y = []
 
    for x_i in x:
        y_i = f(x_i, theta) 
        y.append(y_i)
    print()
    print("Mean   : ", np.mean(y))
    print("Std Dev: ", np.std(y))
    print()
    return x, y

# calculates the coefficients using vandermonde system
def vandermonde(x, y):
    A = []
    
    for x_i in x:
        x_row = []
        for j in range(len(x)):
            x_row.append(x_i**j)
        A.append(x_row)
    
    c = np.linalg.solve(A, y).tolist()[::-1]
    flipped_c = c[::-1]

    # table of coefficients
    tab = PrettyTable()
    tab.field_names = ["x term", "coeff"]
    for i in range(7):
        tab.add_row([i, flipped_c[i]])
    print(tab)

    return c

# checks that the vandermonde polynomial is correct
def qualify_vandermonde(c, x, y):
    for i, x_i in enumerate(x):
        y_i = np.polyval(c, x_i)
        if y_i - y[i] > 1e-9:
            return False
    
    return True

# calculates the maximum error
def error_vandermonde(x, y, c):
    print("length: ", len(x))
    error_max = 0

    for i, x_i in enumerate(x):
        error = (np.abs(y[i]-np.polyval(c, x_i)) / np.abs(y[i]))
        if error > error_max:
            error_max = error

    return error_max

# main program
def main(theta = [1, 10]):
    for t in theta:
        print("THETA: ", t)
        train_x, train_y = gen_train_data(t)
        test_x, test_y   = gen_test_data(t)
        c = vandermonde(train_x, train_y)
        if qualify_vandermonde(c, train_x, train_y) == False:
            print("Vandermonde Failure")
        print_graphs(c, t)
        e = error_vandermonde(test_x, test_y, c)
        print("Absolute Error: ", e, "\n\n\n")

# run main if init
if __name__ == "__main__":
    main()
