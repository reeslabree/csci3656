def fwd_diff(f, x, h):
    return (f(x+h) - f(x)) / h

def bck_diff(f, x, h):
    return (f(x) - f(x-h)) / h

def cnt_diff(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def fin_dif_appx(f, x, h):
    return (1/(6*h)) * ((2*f(x+h)) + (3*f(x)) - (6*f(x-h)) + f(x-(2*h)))
