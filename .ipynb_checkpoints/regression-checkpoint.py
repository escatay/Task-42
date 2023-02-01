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
from scipy.interpolate import BSpline, splrep, splev
#imports for cubic splines
from patsy import dmatrix
import statsmodels.api as sm
import statsmodels.formula.api as smf



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
    #y= polynomial.poly_value(X,Y,deg)
    xfit = np.linspace(0, 10, 100)
    poly_model = make_pipeline(PolynomialFeatures(deg),LinearRegression())
    poly_model.fit(X[:, np.newaxis], Y)
    yfit = poly_model.predict(xfit[:, np.newaxis])
    return yfit
 
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
def gaus(data, deg = 4):
    X = data[0, :]
    Y = data[1, :]
    gauss_model = make_pipeline(GaussianFeatures(deg),LinearRegression())
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

from scipy.interpolate import BSpline, splrep, splev
def bspl(data):
    X,Y = data
    X, Y = zip(*sorted(zip(X, Y)))
    np.random.seed(0)
    n = 300
    ts = X
    ys = Y
    # Fit
    n_interior_knots = 3
    qs = np.linspace(0, 1, n_interior_knots+2)[1:-1]
    knots = np.quantile(ts, qs)
    tck = splrep(ts, ys, t=knots, k=3)
    ys_smooth = splev(ts, tck)
    return ys_smooth
#cubic spline

def cspl(data):
    X,Y = data
    X, Y = zip(*sorted(zip(X, Y)))

    # Generating cubic spline with 3 knots at 25, 40 and 60
    transformed_x = dmatrix("bs(train, knots=(1,3,5), degree=3, include_intercept=False)", {"train": X},return_type='dataframe')

    # Fitting Generalised linear model on transformed dataset
    fit1 = sm.GLM(Y, transformed_x).fit()

    # Predictions on both splines
    xp = np.linspace(0,10,100)
    # Make some predictions
    pred1 = fit1.predict(dmatrix("bs(xp, knots=(1,3,5), include_intercept=False)", {"xp": xp}, return_type='dataframe'))

    return pred1
        