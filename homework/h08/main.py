import csv
import random
import numpy as np
import matplotlib.pyplot as plt

# normal() and qr() methods pulled from "HW8_test_problem.ipynb"
def normal(A, b):
    ATA = np.dot(A.transpose(), A)
    ATb = np.dot(A.transpose(), b) 
    L = np.linalg.cholesky(ATA) 
    y = np.linalg.solve(L, ATb) 
    x_ne = np.linalg.solve(L.transpose(), y) 
    return x_ne

def qr(A, b):
    Q, R = np.linalg.qr(A)
    QTb = np.dot(Q.transpose(), b)
    x_qr = np.linalg.solve(R, QTb)
    return x_qr    

def main():
    # load txt file matrix as A 
    A = []
    with open("loadme.txt") as file:
        A = np.loadtxt("loadme.txt", delimiter=',') 

    # generate 100 random vectors b_i in R^m - we'll use this later
    b = []
    for i in range(100):
        b.append(np.random.randint(1, 101, 101))
      
    # sever the first k columns of the matrix A and do some fun stuff with 'em
    err_size = []
    err_norm_k = []
    err_qr_k = []
    cond_k = []
    for k in range(40, 66):
        # A_k = first k columns of A
        A_k = A[:, :k]

        # report size
        print("       Size: ", np.shape(A_k))

        # report rank
        print("       Rank: ", np.linalg.matrix_rank(np.matrix(A_k, dtype=float))) 

        # report condition
        cond = np.linalg.cond(np.matrix(A_k, dtype=float))
        cond_k.append(cond)
        print("Condition #: ", cond, "\n")

        # time to use our 100 random vectors b_i in b
        err_norm_sum = 0
        err_qr_sum = 0
        for b_i in b:
            
            # use np.linalg.lstsq to find x_true
            x_true = np.linalg.lstsq(A_k, b_i, rcond=None)[0]

            # use normal equation solver to find x_ne
            x_ne = normal(A_k, b_i)
            
            # use qr solver to find x_qr
            x_qr = qr(A_k, b_i)
           
            # uh... figure out the error differences between x_ne and x_true / x_qr and x_true
            err_norm = np.linalg.norm(np.subtract(x_ne, x_true), 2) / np.linalg.norm(x_true, 2)
            err_qr = np.linalg.norm(np.subtract(x_qr, x_true), 2) / np.linalg.norm(x_true, 2)

            # keep track of error avg
            err_norm_sum += err_norm
            err_qr_sum += err_qr

        # compute error for all b for an individual A_k
        err_size.append(k)
        err_norm_k.append(err_norm_sum / len(b))
        err_qr_k.append(err_qr_sum / len(b))
        
    # graph average error versus k for QR and Normal 
    plt.grid(True, which="both")
    plt.semilogy(err_size, err_norm_k, marker='o', label="normal error")
    plt.semilogy(err_size, err_qr_k, marker='o', label="qr error")
    leg = plt.legend(loc="upper left")
    plt.xlim([40, 65])
    plt.title("Average Error vs. Number of Columns (k)") 
    plt.xlabel("k")
    plt.ylabel("Error")
    plt.show()

    # graph condition number of A_k vs k
    plt.grid(True, which="both")
    plt.semilogy(err_size, cond_k, marker='o')
    plt.xlim([40,65])
    plt.xlabel("k")
    plt.ylabel("Condition Number")
    plt.title("Condition Number vs Number of Columns (k)")
    plt.show()

if __name__ == "__main__":
    main()
