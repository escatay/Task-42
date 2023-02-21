#import libraries
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
#import file for regression
import regression
import math


class Model42:
    def mse(self, yhat,y):
            MSE = np.square(np.subtract(yhat,y)).mean()
            RMSE = math.sqrt(MSE)
            return RMSE

    #initialize model with given dataframe
    def __init__ (self, data):
        """Creates an instance of the model the scattered sample points and one for each basis function.
    
    Parameters
    ----------
    data : 2d array
           the sample points.
    deg : int
        Degree of the fitting polynomial.
    
    Returns
    -------
    self : an interactive model consisting of a plotly figure. Each dropdown option displays different basis functions.
    """
        self.data = data
        X,Y = data
        X, Y = zip(*sorted(zip(X, Y)))
        data = zip(X,Y)
        self.scatter = px.scatter(data, x=self.data[0, :], y=self.data[1, :])
        self.fig = go.Figure(data = self.scatter)
        #set polynomial degree to 4 for testing, guess it's obsolete and can go with the better regression function lol
        
        #create the different regression plots:  
        #knot at one
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.cspl(self.data, deg = 4),
                name = 'knot 1-> RMSE: ' +"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 1), y = Y),
                visible = True
            )
        )
        
        #pknot at 2,4,6
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.cspl(self.data, deg = 2),
                name = 'knot(2,4,6) -> RMSE: ' +"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 5), y = Y),
                visible = True
            )
        )
        '''
        #gausian
        self.fig.add_trace(
            go.Scatter(
                 x = np.linspace(0,10,100),
                y = regression.cspl(self.data, deg = 3),
                name = 'knot (1,3,5)  -> RMSE: '+"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 10), y = Y),
                visible = True
            )
        )
        
        #gausian
        self.fig.add_trace(
            go.Scatter(
                 x = np.linspace(0,10,100),
                y = regression.cspl(self.data, deg = 20),
                name = 'knot 20  -> RMSE: ' +"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 20), y = Y),
                visible = True
            )
        )
       '''

      
        
        #the dropdown menu
        self.fig.update_layout(
            dict(
            updatemenus =[
                dict(
                    buttons = list([
                        dict(
                            args=[{'visible': [True, True, True, True, True]}],
                            method = "update"
                        ),
                        dict(
                            args=[{'visible': [True, True, False, False, False]}], 
                            label = "degree 3",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, True, False, False]}], 
                            label = "degree 4",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, False, True, False]}], 
                            label = "degree 5",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, False, False, False, True]}], 
                            label = "degree 6",
                            method = "update"
                        ),
                     
                    ]),
                    #place menu
                    direction="down",
                    showactive=True,
                    x=0.0,
                    xanchor="left",
                    y=1.1,
                    yanchor="top"
                ),
            ]
            )
        )
        
        #add anotation to menu
        self.fig.update_layout(
            annotations=[
                dict(text="Basis function ", showarrow= False,
                     x = 0, y = 1.25, yref = "paper", align = "left")
            ]
        )
        self.fig.show()
    