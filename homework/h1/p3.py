import numpy as np
from prettytable import PrettyTable

def f1(x):
    return ((1-np.cos(x)/((np.sin(x)**2))))

def f2(x):
    return ((1)/(1+np.cos(x)))

x = []
for i in range(13):
    x.append(10**(-1*i))

y1 = []
y2 = []
for i in x:
    y1.append(f1(i))
    y2.append(f2(i))

k = PrettyTable()
k.field_names = ["x", "f1(x)", "f2(x)"]
for i, x_i in enumerate(x): 
    k.add_row([x_i, y1[i], y2[i]])

print(k)
