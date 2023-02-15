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



#add other files here
#periodical
def periodic_basis(x, mu, k, phi=-np.pi/2):
    return np.column_stack((np.cos(k * (x - mu)), np.sin(k * (x - mu) + phi)))

def sin_f(data, deg = 10, ks=1):
    # Generate some random data
    X = np.array(data[0, :])
    Y = np.array(data[1, :])

    # Define number of basis functions and range of means
    num_basis_functions = deg
    mu_range = np.linspace(0, 10, num_basis_functions)

    # Define frequency of the periodic function
    k = ks
    # Compute design matrix
    design_matrix = np.zeros((X.shape[0], num_basis_functions*2))
    for i in range(num_basis_functions):
        design_matrix[:, 2*i:2*(i+1)] = periodic_basis(X, mu_range[i], k)

    # Fit linear regression model
    regressor = LinearRegression()
    regressor.fit(design_matrix, Y)

    # Generate predictions for plotting
    x_range = np.linspace(0, 10, 100)
    basis_functions = np.zeros((x_range.shape[0], num_basis_functions*2))
    for i in range(num_basis_functions):
        basis_functions[:, 2*i:2*(i+1)] = periodic_basis(x_range, mu_range[i], k)
    y_pred = np.dot(basis_functions, regressor.coef_.T)
    return  y_pred

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
def sigmoid_basis(x, mu, s):
    return 1 / (1 + np.exp(-(x - mu) / s))
def sig(data, deg = 10):
    X = data[0, :]
    Y = data[1, :]
    X = np.array(X)
    Y = np.array(Y)

    # Define number of basis functions and range of means
    num_basis_functions = deg
    mu_range = np.linspace(0, 10, num_basis_functions)

    # Compute design matrix
    design_matrix = np.zeros((X.shape[0], num_basis_functions + 1))
    for i in range(num_basis_functions):
        design_matrix[:, i] = sigmoid_basis(X, mu_range[i], s=1)
    design_matrix[:, -1] = 1  # add bias term

    # Fit linear regression model
    regressor = LinearRegression()
    regressor.fit(design_matrix, Y)

    # Generate predictions for plotting
    x_range = np.linspace(0, 10, 100)
    basis_functions = np.zeros((x_range.shape[0], num_basis_functions + 1))
    for i in range(num_basis_functions):
         basis_functions[:, i] = sigmoid_basis(x_range, mu_range[i], s=1)
    basis_functions[:, -1] = 1  # add bias term
    y_pred = np.dot(basis_functions, regressor.coef_.T)
    mean = np.mean(Y)-np.mean(y_pred)
    y_pred = y_pred + mean
    return y_pred



from scipy.interpolate import BSpline, splrep, splev
def bspl(data, deg = 3):
    X,Y = data
    X, Y = zip(*sorted(zip(X, Y)))
    np.random.seed(0)
    n = 300
    ts = X
    ys = Y
    # Fit
    n_interior_knots = deg
    qs = np.linspace(0, 1, n_interior_knots+2)[1:-1]
    knots = np.quantile(ts, qs)
    tck = splrep(ts, ys, t=knots, k=3)
    ys_smooth = splev(ts, tck)
    return ys_smooth
#cubic spline
from patsy import dmatrix
import statsmodels.api as sm
import statsmodels.formula.api as smf

def cspl(data, deg =3):
    
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
    if(deg ==2):
        # Generating cubic spline with 3 knots at 25, 40 and 60
        transformed_x = dmatrix("bs(train, knots=(2,4,6), degree=3, include_intercept=False)", {"train": X},return_type='dataframe')

        # Fitting Generalised linear model on transformed dataset
        fit1 = sm.GLM(Y, transformed_x).fit()

        # Predictions on both splines
        xp = np.linspace(0,10,100)
        # Make some predictions
        pred1 = fit1.predict(dmatrix("bs(xp, knots=(2,4,6), include_intercept=False)", {"xp": xp}, return_type='dataframe'))
    if(deg  ==4):
            # Generating cubic spline with 3 knots at 25, 40 and 60
        transformed_x = dmatrix("bs(train, knots=(1,5,8), degree=3, include_intercept=False)", {"train": X},return_type='dataframe')

        # Fitting Generalised linear model on transformed dataset
        fit1 = sm.GLM(Y, transformed_x).fit()

        # Predictions on both splines
        xp = np.linspace(0,10,100)
        # Make some predictions
        pred1 = fit1.predict(dmatrix("bs(xp, knots=(1,5,8), include_intercept=False)", {"xp": xp}, return_type='dataframe'))

    return pred1
        