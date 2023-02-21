import numpy as np

"""the functions as in the lecture"""

def poly_dm(x,m):
    """
    Generate a desing matrix with monomial basis functions.
    
    Parameters
    ----------
    x : array_like
        1-D input array.
    m : int
        degree of the monomial used for the last column.
    
    Returns
    -------
    phi : ndarray
        Design matrix.
        The columns are ``x^0, x^1, ..., x^m``.
    """
    ϕ = np.ones((len(x), m+1))
    for i in range(1, m+1):
        ϕ[:, i] = x**i
    return ϕ

def pseudoinverse(A):
    """
    Compute the (Moore-Penrose) pseudo-inverse of a matrix.
    
    Parameters
    ----------
    A : (M, N) array_like
      Matrix to be pseudo-inverted.
      
    Returns
    -------
    A_pinverse : (N, M) ndarray
      The pseudo-inverse of `a`.
    """
    return np.dot( np.linalg.inv( np.dot(A.T, A)), A.T)

def poly_regress(x, y, deg):
    """
    Least squares polynomial fit.
    
    Parameters
    ----------
    x : array, shape (M,)
        x-coordinates of the M sample points.

    y : array, shape (M,)
        y-coordinates of the sample points.
    
    deg : int
        Degree of the fitting polynomial.
    
    Returns
    -------
    w : array, shape (deg+1,)
        Polynomial coefficients, highest power last.
    """
    ϕ = poly_dm(x, deg)
    pseudo = pseudoinverse(ϕ)
    return np.dot(pseudo,y)

def polynom(x, w):
    """ Evaluate a polynomial.
    
    Parameters
    ----------
    x : 1d array
        Points to evaluate.
    
    w : 1d array
        Coefficients of the monomials.
    
    Returns
    -------
    y : 1d array
        Polynomial evaluated for each cell of x.
    """
    y = 0
    for i in range(len(w)):
        y += w[i]*(x**i)        
    return y

def poly_value(x,y,deg):
    """Passes data array through polynomial rgression to calculate y values for a given polynomial in a specific interval.
    
    Parameters
    ----------
    x : array, shape (M,)
        x-coordinates of the M sample points.

    y : array, shape (M,)
        y-coordinates of the sample points.
    
    deg : int
        Degree of the fitting polynomial.
    
    Returns
    -------
    y : 1d array
        Polynomial evaluated for each cell of x.
    """
    w=poly_regress(x,y,deg)
    y1=polynom(np.linspace(0,10,100),w)
    return y1
    