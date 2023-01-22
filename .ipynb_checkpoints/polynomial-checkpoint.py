import numpy as np


def poly_dm(x,m):
    ϕ = np.ones((len(x), m+1))
    for i in range(1, m+1):
        ϕ[:, i] = x**i
    return ϕ

def pseudoinverse(A):
    return np.dot( np.linalg.inv( np.dot(A.T, A)), A.T)

def poly_regress(x, y, deg):
    ϕ = poly_dm(x, deg)
    pseudo = pseudoinverse(ϕ)
    return np.dot(pseudo,y)

def polynom(x, w):
    y = 0
    for i in range(len(w)):
        y += w[i]*(x**i)        
    return y

def poly_value(x,y,deg):
    w=poly_regress(x,y,deg)
    y=polynom(np.linspace(0,10,100),w)
    return y
    