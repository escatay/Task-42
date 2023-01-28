#imported libraries
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
#imported files for regression
import polynomial
#add other files here


def polyreg(data, deg = None):
    
    """Calls the polynomial basis function.
    
    Parameters
    ----------
    data : 2d array
           the sample points.
    deg : int
        Degree of the fitting polynomial.
    
    Returns
    -------
    y : 1d array
        Polynomial evaluated for each cell of x.
    """        
    X = data[0, :]
    Y = data[1, :]
    y= polynomial.poly_value(X,Y,deg)
    return y

#add other basis functions here
        


        
        