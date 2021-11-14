import matplotlib.pyplot as plt
import numpy as np

def eprint(e, title):
    x = np.linspace(0, len(e), len(e))

    plt.plot(x,e)
    plt.title(title)
    plt.show()
