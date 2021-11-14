import math
import numpy as np
import matplotlib.pyplot as plt
import csv

def make_dot_graph(m):
    x_dot = []
    y_dot = []
    for i, row in enumerate(m):
        for j, el in enumerate(row):
           if np.abs(0 - float(el)) > 1.0e-15:
                y_dot.append(len(m) - i)
                x_dot.append(j + 1)
    
    s = [math.ceil(5000/len(x_dot))] * len(x_dot) 
 
    plt.scatter(x_dot, y_dot, s=s) #, markersize=2)
    plt.show()

