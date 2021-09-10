import csv
import matplotlib.pyplot as plt

# part 1
x = []
y = []
with open('data.txt', newline='\n') as data_file:
    lines = list(csv.reader(data_file))
    for line in lines:
        x.append(line[0])
        y.append(line[1])

# part 2
plt.plot(x, y)
plt.show()
