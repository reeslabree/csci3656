from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np

# calculate jacobian
def jacobian(x):
    j = [[(3*(x[0]**2)+1), -3*x[1]**2],
         [2*x[0], 2*x[1]]]

    return np.array(j)

# function declerations 
def f1(x_1, x_2):
    return ((x_1**3)-(x_2**3)+x_1)

def f2(x_1, x_2):
    return ((x_1**2)+(x_2**2)-1)

# f matrix
def f_matrix(x, f_1=f1, f_2=f2):
    k = [0,0]
    k[0] = f_1(x[0], x[1])
    k[1] = f_2(x[0], x[1])
    return np.array(k)

# newton's algorithm
def newtons(x, f_1=f1, f_2=f2, max_iter=150, tol= 1e-9):
    x_i = x
    
    for i in range(max_iter):
        x = x_i
        
        f = f_matrix(x)
        j = jacobian(x)
        p = np.linalg.solve(j, f)

        x_i = np.array(x_i) - p        
        
         
        # anyone in the mood for some printf debugging?
        '''
        print("x   = ", x)
        print("p   = ", p)
        print("x_i = ", x_i)
        print("norm f       = ", np.linalg.norm(f)) 
        print("norm delta x = ", np.linalg.norm([x_i[0] - x[0], x_i[1] - x[1]]))
        '''

        if((np.linalg.norm(f) < tol) or (np.linalg.norm(x_i-x) < tol)):
            break


    return x_i

# problem 1 graphs
def gen_plots(intersect = [[.5, -.5],[-.5, .5]]):
    x1 = np.linspace(-1.5, 1.5, 1000)
    y1 = np.cbrt(x1**3+x1)
    plt.plot(x1, y1)

    # create f2 plot
    x2 = np.linspace(-1.0, 1.0, 1000)
    y2 = np.linspace(-1.0, 1.0, 1000)
    X2, Y2 = np.meshgrid(x2,y2)
    F2 = X2**2 + Y2**2 - 1
    plt.contour(X2, Y2, F2, [0])
    
    # intersections
    plt.plot(intersect[0], intersect[1], 'ro') 
    
    # show plots
    plt.show()

# problem 3 tables
def create_table():
    tab = PrettyTable()
    tab.field_names = ["initial guess", "newton's solution"]
    tab.align = "l"

    x = np.logspace(1, 3, 10)
    y = np.ones(np.shape(x))
    
    for i, x in enumerate(x):
        col_1 = [np.round(x,3), np.round(y[i], 3)]
        tab.add_row([col_1, newtons([x, y[i]])])
        
    print(tab)
    
# problem 4 failure
def failure():
    print("Failure at (1e5,1)")
    print(newtons([1e5, 1]))

def main():
    x_0 = newtons([-1,-1]).tolist();
    x_1 = newtons([1 , 1]).tolist();
    
    x = [[x_0[0], x_1[0]], [x_0[1], x_1[1]]]

    gen_plots(np.array(x))

    create_table()

    failure()    

if __name__ == "__main__":
    main()
