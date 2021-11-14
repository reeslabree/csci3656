from prettytable import PrettyTable
import numpy as np

def make_table(x, y):
    t = PrettyTable()

    t.field_names = ['initial guess','root']

    for i, x_i in enumerate(x):
        t.add_row([np.round(x_i,4), y[i]])

    print(t)
