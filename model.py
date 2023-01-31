#import libraries
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
#import file for regression
import regression

class Model42:
 

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
        self.scatter = px.scatter(data, x=self.data[0, :], y=self.data[1, :])
        self.fig = go.Figure(data = self.scatter)
        #set polynomial degree to 4 for testing, guess it's obsolete and can go with the better regression function lol
        self.deg = 4
        
        #create the different regression plots:  
        #polynomial
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.polyreg(self.data, deg = self.deg),
                name = 'polynomial',
                visible = False
            )
        )
        #periodical
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.sin_f(self.data),
                name = 'periodical',
                visible = False
            )
        )
        #gausian
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.gaus(self.data),
                name = 'gaussian',
                visible = False
            )
        )
        
         #sigmoidial
        self.fig.add_trace(
            go.Scatter(
                x = np.linspace(0,10,100),
                y = regression.sig(self.data),
                name = 'sigmoidal',
                visible = False
            )
        )
        
        #the dropdown menu
        self.fig.update_layout(
            dict(
            updatemenus =[
                dict(
                    buttons = list([
                        dict(
                            args=[{'visible': [True, False]}],#this line decides which curves are visible and has to be changed to the number of traces added before. 1st is the data points, the others are the regression curves in the order they were added
                            label = "none",
                            method = "update"
                        ),
                        dict(
                            args=[{'visible': [True, True, False, False, False]}], #add traces for other basis functions
                            label = "polynomial",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, True, False, False]}], #add traces for other basis functions
                            label = "gaussian",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, False, True, False]}], #add traces for other basis functions
                            label = "sigmoidal",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, False, False, False, True]}], #add traces for other basis functions
                            label = "periodical",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, True, True, True, True]}], #add traces for other basis functions
                            label = "all",
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
    