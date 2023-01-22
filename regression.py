import polynomial
import numpy as np
import matplotlib.pyplot as plt

def regress(data, basis_func, deg = None):
    # importing the same data, store in X and Y
    X = data[0, :]
    Y = data[1, :]
    model, ax = plt.subplots(nrows = 1, ncols = 1)
    if basis_func == "polynomial":
        y= polynomial.poly_value(X,Y,deg)
        ax.plot(np.linspace(1,10,100), y, label = ("polynomial regression, degree = ", deg))
    else:
        plt.text(x = 0.25, y = 0.5, s = "Not implemented yet")
        
        
        