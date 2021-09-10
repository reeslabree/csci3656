import numpy as np
import matplotlib.pyplot as plt


# part 1
x = np.linspace(0,1,11)
y = []

# part 2
for i in x:
    y.append((i**2)-(0.5*i)+(0.1625))

# part 4
sum_y = np.sum(y)
max_y = np.max(y)
sum_y_half = sum_y**(.5)

print("sum_y: ", sum_y, "\nmax_y: ", max_y, "\nsum_y_half: ", sum_y_half)

# part 5
print("\nI used the numpy linspace function to create the evenly spaced 11 values of x between 0 and 1. For each x value I plug it into the equation for y and append it to the y vector. Using matplotlib I plot x against y. Finally, using some built in numpy functions I calculate the values described in the write up and print them.")

# part 3
plt.plot(x,y)
plt.show()
