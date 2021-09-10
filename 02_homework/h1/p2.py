import matplotlib.pyplot as plt
import numpy as np

# create domain
x = np.linspace(1.92, 2.08, 8000)

# create range for y1
y1 = []
for i in x:
    y1.append((i-2)**9)

# create range for y2
y2 = []
a = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]
for i in x:
    p = a[0]
    for k in range(1, 10):
        p = p*i + a[k]

    y2.append(p)

plt.plot(x,y1)
plt.show()
plt.plot(x,y2, marker='.', markersize=2)
plt.show();
