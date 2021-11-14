import numpy as np
import matplotlib.pyplot as plt

# function definition
def fun(x):
    return np.sin(2*np.pi*x) + np.cos(3*np.pi*x)

# create training (x, y) pairs
def gen_train(x_min=-1, x_max=1, num=33):
    x = np.linspace(x_min, x_max, num)
    y = []
    for x_i in x:
        y.append(fun(x_i))

    return x, y

# normal and qr least squares algorithm's, fleeced from homework 8
def normal(A, b):
    ATA = np.dot(A.transpose(), A)
    ATb = np.dot(A.transpose(), b) 
    if(len(ATA) == np.linalg.matrix_rank(ATA)):
        L = np.linalg.cholesky(ATA) 
        y = np.linalg.solve(L, ATb) 
        x_ne = np.linalg.solve(L.transpose(), y) 
        return x_ne
    return [-1, 0]

def qr(A, b):
    Q, R = np.linalg.qr(A)
    QTb = np.dot(Q.transpose(), b)
    x_qr = np.linalg.solve(R, QTb)
    return x_qr    

# use x to make the tall A matrix
def calc_tall(x_train, deg):
    # vandermonde matrix is from x^0 to x^n-1, call with deg+1
    A = np.vander(x_train, deg+1)
    # vandermonde returns a flipped matrix, so we flip it back
    A = np.fliplr(A)
    return A

# use specificed algorithm to find coeff
def calc_coeff(x_train, y_train, deg=7, alg=qr):
    A = calc_tall(x_train, deg)
    coeff = alg(A, y_train)
    return coeff

def draw_plot(coeff):
    x = np.linspace(-1, 1, 1000)
    y_poly = []
    y_fun = []
    
    # solve for data
    for x_i in x:
        y_poly.append(np.polyval(np.flipud(coeff), x_i))
        y_fun.append(fun(x_i))
    
    # plot stuff
    plt.plot(x, y_poly, label="Polynomial Approximation")
    plt.plot(x, y_fun, label="True Function")
    plt.title("Comparing the Polynomial Approximation to the True Function")
    leg = plt.legend(loc="upper right")
    plt.show()

def qualify(x_min=-1, x_max=1, deg_max=7, num=100):
    x_train, y_train = gen_train()
    x_test = [np.random.uniform(low=-1.0, high=1.0) for i in range(num)]
    y_test = [fun(x) for x in x_test]
    
    y_true = 0
    for y_i in y_test:
        y_true += (y_i**2)
    y_true /= len(y_test)
    p_error_qr = []
    p_error_ne = []
    d_qr = []
    d_ne = []

    for d in range(1, 32):
        coeff_qr = calc_coeff(x_train, y_train, d)
        e_sum_qr = 0
        for i, x_i in enumerate(x_test):
            e_sum_qr += (y_test[i] - np.polyval(np.flipud(coeff_qr), x_i))
         
        e_sum_qr /= len(x_test) 
        p_error_qr.append((np.abs(e_sum_qr) / np.abs(y_true))**0.5)
        d_qr.append(d)

    for d in range(1, 32):
        coeff_ne = calc_coeff(x_train, y_train, d, alg=normal)
        if sum(coeff_ne) == -1:
            continue
        e_sum_ne = 0
        for i, x_i in enumerate(x_test): 
            e_sum_ne += (y_test[i] - np.polyval(np.flipud(coeff_ne), x_i))
        e_sum_ne /= len(x_test)
        p_error_ne.append((np.abs(e_sum_ne) / np.abs(y_true))**0.5)
        d_ne.append(d)

    plt.figure()
    plt.semilogy(d_qr, p_error_qr)
    plt.semilogy(d_ne, p_error_ne, '--')
    plt.legend(["QR", "Normal"])
    plt.xlabel("Degree")
    plt.ylabel("Error")
    plt.title("Error vs Degree")
#    plt.grid(True, which="both")
    plt.show()

def main():
    x_train, y_train = gen_train()
    coeff_qr = calc_coeff(x_train, y_train)
#   coeff_norm = calc_coeff(x_train, y_train, alg=normal)
    draw_plot(coeff_qr) 
    qualify()

if __name__ == "__main__":
    main()
