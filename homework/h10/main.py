import derivatives as der   # fwd, bck, cnt, fin_dif implementation
import numpy as np
import matplotlib.pyplot as plt

# f(x)
def fun(x):
    return np.sin(4.8*np.pi*x)

# f'(x)
def dfun(x):
    return 4.8*np.pi*np.cos(4.8*np.pi*x)

def estimate(x=0.2, f=fun, k_min=5, k_max=30):
    h = np.power(2., -np.arange(k_min, k_max))
    e_f = np.zeros(np.size(h))
    e_b = np.zeros(np.size(h))
    e_c = np.zeros(np.size(h))
    x_truth = dfun(x)
    
    for k in range(len(h)):
        # fwd diff
        fwd = der.fwd_diff(f, x, h[k])
        e_f[k] = np.fabs(x_truth - fwd) / np.fabs(x_truth)

        # bck diff
        bck = der.bck_diff(f, x, h[k])
        e_b[k] = np.fabs(x_truth - bck) / np.fabs(x_truth)

        # cnt diff
        cnt = der.cnt_diff(f, x, h[k])
        e_c[k] = np.fabs(x_truth - cnt) / np.fabs(x_truth)

    return h, e_f, e_b, e_c

def fin_diff(x=0.2, f=fun, k_min=5, k_max=30):
    h = np.power(2., -np.arange(k_min, k_max))
    e = np.zeros(np.size(h))
    x_truth = dfun(x)

    for k in range(len(h)):
        # finite difference approximation
        appx = der.fin_dif_appx(f, x, h[k])
        e[k] = np.fabs(x_truth - appx) / np.fabs(x_truth)

    return h, e

def plot_error(h, e, title):
    plt.figure()
    plt.loglog(h, e, 'bo-')
    plt.grid(True)
    plt.xlabel('h')
    plt.ylabel('relative error')
    plt.title(title + ': d/dx sin(4.8 pi x) @ x=0.2')
    plt.show()

def main():
    h, e_f, e_b, e_c = estimate()
    plot_error(h, e_f, 'Forward Diff Error')
    plot_error(h, e_b, 'Backward Diff Error')
    plot_error(h, e_c, 'Central Diff Error')

    h, e = fin_diff()
    plot_error(h, e, 'Finite Difference Approximation Error')

if __name__ == "__main__":
    main()
