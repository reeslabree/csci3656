import csv
import numpy as np
import datetime
import luchol
import jacobi
import gauss
import pprint
pp = pprint.PrettyPrinter(indent=4)

def load_matrix(filename):
    mat = []

    with open(filename) as file:
        rows = (csv.reader(file)) #, delimiter=','))
        
        for row in rows:
            mat.append(row)

    return mat    

def timing(method, A, b, n=50):
    t_avg = 0
    for i in range(n):
        t = datetime.datetime.utcnow()
        method(A, b)
        t = (t-datetime.datetime.utcnow()).total_seconds()
        t_avg += t/n
    return t_avg

def error_compare(x_truth, x):
    return np.linalg.norm(np.subtract(x_truth, x)) / np.linalg.norm(x_truth)

def main():
    files = []
    for i in range(1,6):
        files.append("mat"+str(i)+"-1.txt")

    for file in files:
        print("\n\nAnalyzing: " + file)

        # load matrix
        A = np.array(load_matrix(file), dtype='float')
    
        # 1. generate right hand of ones
        b = []
        for i in range(len(A)):
            b.append(1)
        b = np.array(b, dtype='float')
        
        
        # 2. solve with generic linear solver
        try:
            x_truth = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            print("Matrix is singular and cannot be solved")
            break

        print("--RELATIVE ERROR COMPARISON--")

        # 3. solve with LU decomp or Cholesky
        x_luc = luchol.solve(A, b)
        print("LU Decomp / Cholesky Relative Error: " + str(error_compare(x_truth, x_luc)))

        # 4. solve with Jacobi
        x_j = jacobi.solve(A, b) 
        print("              Jacobi Relative Error: " + str(error_compare(x_truth, x_j)))
        
        # 5. Solve with Gauss-Seidel
        x_gs = gauss.solve(A, b)
        print("        Gauss-Seidel Relative Error: " + str(error_compare(x_truth, x_gs)))

        # timing study for each
        print("\n--TIMING STUDY--")
        print("LU Decomp / Cholesky Time: " + str(timing(luchol.solve, A, b)))
        print("              Jacobi Time: " + str(timing(jacobi.solve, A, b)))
        print("        Gauss-Seidel Time: " + str(timing(gauss.solve, A, b)))


if __name__ == "__main__":
    main()
