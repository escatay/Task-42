#import libraries
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
#import file for regression
import regression
import math


class Model42:
    def mse(self, yhat,y):
            MSE = np.square(np.subtract(np.array(yhat),np.array(y))).mean()
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

        #create the different regression plots for each degree:  
        #1
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 1),
                name = 'degree 5 -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 5)), y = Y),
                visible = True
            )
        )
        #2
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 2),
                name = 'degree 5 -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 5)), y = Y),
                visible = True
            )
        )
        #3
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 3),
                name = 'degree 5 -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 5)), y = Y),
                visible = True
            )
        )
        #4
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 4),
                name = 'degree 5 -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 5)), y = Y),
                visible = True
            )
        )
        #polynomial
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 5),
                name = 'degree 5 -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 5)), y = Y),
                visible = True
            )
        )
        #periodical
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 6),
                name = 'degree 6 -> RMSE: ' + "%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 6)), y = Y),
                visible = True
            )
        )
        #gausian
        self.fig.add_trace(
            go.Scatter(
                 x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 7),
                name = 'degree 7 -> RMSE: '+ "%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = 7)), y = Y),
                visible = True
            )
        )
        #gausian
        self.fig.add_trace(
            go.Scatter(
                 x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 8),
                name = 'degree 8 -> RMSE: ' +"%.3f" %self.mse(yhat = regression.polyreg(self.data, deg = 8), y =Y),
                visible = True
            )
        )
                #gausian
        self.fig.add_trace(
            go.Scatter(
                 x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = 9),
                name = 'degree 9 -> RMSE: ' +"%.3f" %self.mse(yhat = regression.polyreg(self.data, deg = 9), y =Y),
                visible = True
            )
        )

        
        
        #the dropdown menu
        self.fig.update_layout(
            dict(
            updatemenus =[
                dict(
                    buttons = list([
                        dict(
                            args=[{'visible': [True, True, True, True, True, True]}],#this line decides which curves are visible and has to be changed to the number of traces added before. 1st is the data points, the others are the regression curves in the order they were added
                            label = "all ",
                            method = "update"
                        ),
                        dict(
                            args=[{'visible': [True, True, False, False, False, False]}], #add traces for other basis functions
                            label = "degree 5",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, True, False, False, False]}], #add traces for other basis functions
                            label = "degree 6",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, False, True, False, False]}], #add traces for other basis functions
                            label = "degree 7",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, False, False, False, True, False]}], #add traces for other basis functions
                            label = "degree 8",
                            method = "update"
                        ),
                                             dict (
                            args = [{'visible': [True, False, False, False, False, True]}], #add traces for other basis functions
                            label = "degree 9",
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
    