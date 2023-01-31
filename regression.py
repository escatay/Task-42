#imported libraries
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from scipy.optimize import curve_fit
import math
#imported files for regression
import polynomial
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


#add other files here
#periodical
x = np.linspace(0,10,100)

def sin_function(x,A,b,phi,c):
    y = A*np.sin(b*x+phi)+c
    return y

def sin_f(data):
    X = data[0, :]
    Y = data[1, :]
    sin, pcov = curve_fit(sin_function, X, Y)
    x = np.linspace(0,10,100)

    y = sin_function(x, sin[0],sin[1],sin[2],sin[3])
    return y 

#polynomial
def polyreg(data, deg = None):   
    X = data[0, :]
    Y = data[1, :]
    y= polynomial.poly_value(X,Y,deg)
    return y
 
#gausian
class GaussianFeatures(BaseEstimator, TransformerMixin):
    """Uniformly spaced Gaussian features for one-dimensional input"""
    
    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor
    
    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))
        
    def fit(self, X, y=None):
        # create N centers spread along the data range
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self
        
    def transform(self, X):
        return self._gauss_basis(X[:, :, np.newaxis], self.centers_,
                                 self.width_, axis=1)
def gaus(data):
    X = data[0, :]
    Y = data[1, :]
    gauss_model = make_pipeline(GaussianFeatures(4),LinearRegression())
    gauss_model.fit(X[:, np.newaxis], Y)
    yfit = gauss_model.predict(x[:, np.newaxis])
    return yfit

 #sigmoidial 
def sigmoidal(x, a, b):
    return 1/(1+np.exp(-((x-a)/b)))

def sig(data):
    X = data[0, :]
    Y = data[1, :]
    sig, pcov = curve_fit(sigmoidal, X, Y)
    x = np.linspace(0,10,100)
    y = sigmoidal(x, sig[0],sig[1])
    return y 
        
        