import csv
import numpy as np
import colorgraph
import dotgraph

# https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
def is_symmetric(mat, atol=1e-8, rtol=1e-5):
    return np.allclose(mat, mat.T, rtol=rtol, atol=atol) 

# https://stackoverflow.com/questions/43884189/check-if-a-large-matrix-is-diagonal-matrix-in-python
def is_diagonal(mat):
    new_mat = np.ones(mat.shape, dtype=float)
    np.fill_diagonal(new_mat, 0)
    return np.count_nonzero(np.multiply(new_mat, mat)) == 0

# https://www.geeksforgeeks.org/check-whether-given-matrix-orthogonal-not/
def is_orthogonal(mat):
    m = len(mat)
    n = len(mat[0])
    if (m != n) :
        return False
     
    for i in range(0, n) :
        for j in range(0, n) :
            sum = 0
            for k in range(0, n) :
                sum = sum + (a[i][k] *
                             a[j][k])
         
        if (i == j and sum != 1) :
            return False
        if (i != j and sum != 0) :
            return False
 
    return True

for i in range(1,6):
    print("MATRIX " + str(i))

    mat = []

    with open("mat" + str(i) + ".txt") as file:
        rows = (csv.reader(file, delimiter=','))
        
        for row in rows:
            mat.append(row)

   # determine dimension
    print("Dimenion:\nRows: " + str(len(mat)) + ", Columns: " + str(len(mat[0])) + "\n")
    
    # determine number of zeros
    zeros = 0
    for i in mat:
        for j in i:
            if np.abs(0.0 - float(j)) <= 1e-9:
                zeros += 1

    print("Number of Zeros:\n" + str(zeros) + "\n")

    dotgraph.make_dot_graph(mat)
    mat = np.matrix(mat, dtype=float) 
    colorgraph.make_color_graph(mat) 

    # determine if symmetric
    print("Is Symmetric?:")
    if is_symmetric(mat):
        print("yes\n")
    else:
        print("no\n")


    # determine diagonality
    print("Is Diagonal?:")
    if is_diagonal(mat):
        print("yes\n")
    else:
        print("no\n")

    # determine orthagonality
    print("Is Orthogonal?:")
    if is_orthogonal(mat):
        print("yes\n")
    else:
        print("no\n")

    # determine rank
    print("Rank:")
    print(np.linalg.matrix_rank(mat))
    print("")

    # singular values
    u,v,s = np.linalg.svd(mat)
    print("Smallest Singular Value:\n" + str(np.min(s)) + "\n")
    print("Largest Singular Value:\n" + str(np.max(s)) + "\n")

    # condition number
    print("Condition Number:\n" + str(np.linalg.cond(mat)) + "\n")

    # right hand sides
    for i in range(5):
        rand_right = []
        for j in range(len(mat)):
            rand_right.append([np.random.random()])
        rand_right = np.matrix(rand_right)
        try:
            np.linalg.solve(mat, rand_right)
        except:
            print("Could not solve for a random right-hand-side")

    print("\n")
