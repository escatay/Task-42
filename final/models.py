#import libraries
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import math
#import file for regression
import regression



class Model42:
    
    def mse(self, yhat,y):
            MSE = np.square(np.subtract(np.array(yhat),np.array(y))).mean()
            RMSE = math.sqrt(MSE)
            return RMSE

    #initialize a model to compare different degrees of polynomials
    def __init__ (self, data, bf):
        
        self.__name__ = Model42
        #the data points
        self.data = data
        X,Y = data
        X, Y = zip(*sorted(zip(X, Y)))
        data = zip(X,Y)
        self.scatter = px.scatter(data, x=self.data[0, :], y=self.data[1, :])
        self.fig = go.Figure(data = self.scatter)
        self.bf = bf
        self.update(self.bf)
        
    def update(self, bf):
        #clear_output()
        self.fig = go.Figure(data = self.scatter)
        self.bf = bf
        X,Y = self.data
        X, Y = zip(*sorted(zip(X, Y)))
        data = zip(X,Y)
        if self.bf == "polynomial":
            #traces for regression plots of different degrees
            for deg in range(1,11):
                self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.polyreg(self.data, deg),
                    name = 'degree' + str(deg) + ' -> RMSE: ' +"%.3f" %self.mse(yhat = np.array(regression.polyreg(self.data, deg = deg)), y = Y),
                    visible = False
                    )
                )
            #the slider 
            steps = []
            for i in range(len(self.fig.data)):
                step = dict(
                    method="update",
                    args=[{"visible": [False] * len(self.fig.data)},
                          {"title": "degree: " + str(i)}],  # layout attribute
                )
                step["args"][0]["visible"][0] = True 
                step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
                steps.append(step)

            sliders = [dict(
                active=10,
                currentvalue={"prefix": "Degree: "},
                pad={"t": 50},
                steps=steps
            )]

            self.fig.update_layout(
                sliders=sliders,
                title=go.layout.Title(text="Polynomial Basis Functions", x = 0.5),
                annotations=[
                    dict(text="Formula: ϕ(x)=xj", showarrow= False,
                         x = 1, y = 1.2, yref = "paper", align = "right"),
                    
                ],
            )

            self.fig.show()
        
        elif self.bf == "gaussian":

            #traces for different degrees
            for deg in range (3,11):
                self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.gaus(self.data, deg = deg),
                    name = 'degree ' + str(deg) + ' -> RMSE: ' + "%.2f" % self.mse(yhat = regression.gaus(self.data, deg = deg), y = Y),
                    visible = False
                    )
                )
            #the slider 
            steps = []
            for i in range(len(self.fig.data)):
                step = dict(
                    method="update",
                    args=[{"visible": [False] * len(self.fig.data)},
                          {"title": "degree: " + str(i)}],  # layout attribute
                )
                step["args"][0]["visible"][0] = True 
                step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
                steps.append(step)

            sliders = [dict(
                active=10,
                currentvalue={"prefix": "Degree: "},
                pad={"t": 50},
                steps=steps
            )]

            self.fig.update_layout(
                sliders=sliders,
                title=go.layout.Title(text="Gaussian Basis Functions", x = 0.5),
                annotations=[
                    dict(text="Formula: ϕj(x)=exp{−(x−μj)22s2}", showarrow= False,
                         x = 1, y = 1.2, yref = "paper", align = "right"),
                    
                ],
            )

            self.fig.show()
            
        #initialize a model to compare different degrees of sigmoidals
        elif self.bf == "sigmoidal":
            
            #traces for different degrees
            for deg in range (1,11):
                self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.sig(self.data, deg),
                    name = 'degree ' + str(deg) + ' -> RMSE: ' +"%.2f" % self.mse(yhat = regression.sig(self.data, deg = deg), y = Y),
                    visible = False
                    )
                )
            #the slider 
            steps = []
            for i in range(len(self.fig.data)):
                step = dict(
                    method="update",
                    args=[{"visible": [False] * len(self.fig.data)},
                          {"title": "degree: " + str(i)}],  # layout attribute
                )
                step["args"][0]["visible"][0] = True 
                step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
                steps.append(step)

            sliders = [dict(
                active=10,
                currentvalue={"prefix": "Degree: "},
                pad={"t": 50},
                steps=steps
            )]

            self.fig.update_layout(
                sliders=sliders,
                title=go.layout.Title(text="Sigmoidal Basis Functions", x = 0.5),
                annotations=[
                    dict(text="Formula: ϕj(x)=σ(x−μjs) where σ(a)=11+exp(−a)", showarrow= False,
                         x = 1, y = 1.2, yref = "paper", align = "right"),
                    
                ],
            )

            self.fig.show()     
            
        #initialize a model to compare different periodicals
        elif self.bf == "periodical":

            #traces for different degrees
            buttons_d = []
            buttons_f = []
            for deg in range (1,3):
                for freq in range (1,3):
                    self.fig.add_trace(
                        go.Scatter(
                            x = np.linspace(0,10,100),
                            y = regression.sin_f(self.data, deg, freq),
                            name = 'degree ' + str(deg) + ' , ferquency = ' + str(freq) + ' -> RMSE: ' +"%.2f" % self.mse(yhat = regression.sin_f(self.data, deg = deg, ks =freq), y = Y),
                            visible = False
                        )
                    )
            #dropdown
            self.fig.update_layout(
            dict(
            updatemenus =[
                dict(
                    buttons = list([
                        dict(
                            args=[{'visible': [True, False, False, False, False]}],
                            label = "none",
                            method = "update"
                        ),
                        dict(
                            args=[{'visible': [True, True, False, False, False]}], 
                            label = "deg=1, freq=1",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, True, False, False]}], 
                            label = "deg=1, freq=2",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, False, True, False]}], 
                            label = "deg=2, freq=1",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, False, False, False, True]}],
                            label = "deg=2, freq=2",
                            method = "update"
                        ),
                    ]),
                    #place menu
                    direction="down",
                    showactive=True,
                    x=0.0,
                    xanchor="left",
                    y=1.1,
                    yanchor="top" ,
                ),
            ])
            )
            #add anotation to menu
            self.fig.update_layout(
                annotations=[
                    dict(text="Parameters ", showarrow= False,
                         x = -0.5, y = 1.2, yref = "paper", align = "left"),
                    dict(text="Formula: f(x)=f(x+nk),k∈N", showarrow= False,
                         x = 1, y = 1.2, yref = "paper", align = "right"),
                    
                ],
                title=go.layout.Title(text="Periodical Basis Functions", x = 0.5)
            )
            self.fig.show()
            
            #initialize a model to compare different b-splines
        elif self.bf == "bspline":
            #create the different regression number of knots:  
            #1
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.bspl(self.data, deg = 1),
                    name = 'knot 1-> RMSE: ' +"%.2f" % self.mse(yhat = regression.bspl(self.data, deg = 1), y = Y),
                    visible = False
                )
            )

            #5
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.bspl(self.data, deg = 5),
                    name = 'knot 5 -> RMSE: ' +"%.2f" % self.mse(yhat = regression.bspl(self.data, deg = 5), y = Y),
                    visible = False
                )
            )
            #10
            self.fig.add_trace(
                go.Scatter(
                     x = np.linspace(0,10,100),
                    y = regression.bspl(self.data, deg = 10),
                    name = 'knot 10  -> RMSE: '+"%.2f" % self.mse(yhat = regression.bspl(self.data, deg = 10), y = Y),
                    visible = False
                )
            )

            #20
            self.fig.add_trace(
                go.Scatter(
                     x = np.linspace(0,10,100),
                    y = regression.bspl(self.data, deg = 20),
                    name = 'knot 20  -> RMSE: ' +"%.2f" % self.mse(yhat = regression.bspl(self.data, deg = 20), y = Y),
                    visible = False
                )
            )
            #dropdown
            self.fig.update_layout(
            dict(
            updatemenus =[
                dict(
                    buttons = list([
                        dict(
                            args=[{'visible': [True, False, False, False, False]}],
                            label = "none",
                            method = "update"
                        ),
                        dict(
                            args=[{'visible': [True, True, False, False, False]}], 
                            label = "Knot 1",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, True, False, False]}], 
                            label = "Knot 5",
                            method = "update"
                        ),
                        dict(
                            args = [{'visible': [True, False, False, True, False]}], 
                            label = "Knot 10",
                            method = "update"
                        ),
                        dict (
                            args = [{'visible': [True, False, False, False, True]}],
                            label = "Knot 20",
                            method = "update"
                        ),
                    ]),
                    #place menu
                    direction="down",
                    showactive=True,
                    x=0.0,
                    xanchor="left",
                    y=1.1,
                    yanchor="top" ,
                ),
            ])
            )
            #add anotation to menu
            self.fig.update_layout(
                annotations=[
                    dict(text="Knots ", showarrow= False,
                         x = -0.5, y = 1.2, yref = "paper", align = "left")
                ],
                title=go.layout.Title(text="B-Spline", x = 0.5)
            )
            self.fig.show()
        elif self.bf == "cubicspline":
            #create the different regression plots:  
            #knot at one
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.cspl(self.data, deg = 4),
                    name = 'knot 1-> RMSE: ' +"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 1), y = Y),
                    visible = False
                )
            )

            #pknot at 2,4,6
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.cspl(self.data, deg = 2),
                    name = 'knot(2,4,6) -> RMSE: ' +"%.2f" % self.mse(yhat = regression.cspl(self.data, deg = 5), y = Y),
                    visible = False
                )
            )
            #dropdown 
            self.fig.update_layout(
                dict(
                updatemenus =[
                    dict(
                        buttons = list([
                            dict(
                                args=[{'visible': [True, False, False]}],
                                label= "none",
                                method = "update"
                            ),
                            dict(
                                args=[{'visible': [True, True, False]}], 
                                label = "knot 1",
                                method = "update"
                            ),
                            dict(
                                args = [{'visible': [True, False, True]}], 
                                label = "knot(2,4,6)",
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
                         x = -0.5, y = 1.2, yref = "paper", align = "left")
                ],
                title=go.layout.Title(text="Cubic Spline", x = 0.5)
            )
            self.fig.show()
            
        else:

            #create the different regression plots:  
            #polynomial
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.polyreg(self.data, deg = 4),
                    name = 'polynomial - RMSE: ' +"%.2f" %self.mse(yhat = regression.polyreg(self.data, deg = 4), y =Y),
                    visible = False
                )
            )
            #periodical
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.sin_f(self.data),
                    name = 'periodical - RMSE: ' +"%.2f" %self.mse(yhat = regression.sin_f(self.data), y = Y),
                    visible = False
                )
            )
            #gausian
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.gaus(self.data),
                    name = 'gaussian - RMSE: ' +"%.2f" %self.mse(yhat = regression.gaus(self.data), y = Y),
                    visible = False
                )
            )

             #sigmoidial
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.sig(self.data),
                    name = 'sigmoidal - RMSE: ' +"%.2f" %self.mse(y = Y, yhat = regression.sig(self.data)),
                    visible = False
                )
            )

            #bspline bspl
            self.fig.add_trace(
                go.Scatter(
                    x = sorted(X),
                    y = regression.bspl(self.data),
                    name = 'b-spline - RMSE: ' +"%.2f" %self.mse(yhat = regression.bspl(self.data), y = Y),
                    visible = False
                )
            )
            #cubic spline 
            self.fig.add_trace(
                go.Scatter(
                    x = np.linspace(0,10,100),
                    y = regression.cspl(self.data),
                    name = 'Cubic-spline - RMSE:' +"%.2f" %self.mse(yhat = regression.cspl(self.data), y = Y),
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
                                args=[{'visible': [True, False, False, False, False, False, False]}],
                                label = "none",
                                method = "update"
                            ),
                            dict(
                                args=[{'visible': [True, True, False, False, False, False, False]}], 
                                label = "polynomial",
                                method = "update"
                            ),
                            dict(
                                args = [{'visible': [True, False, True, False, False, False, False]}], 
                                label = "periodical",
                                method = "update"
                            ),
                            dict(
                                args = [{'visible': [True, False, False, True, False, False, False]}], 
                                label = "gaussian",
                                method = "update"
                            ),
                            dict (
                                args = [{'visible': [True, False, False, False, True, False, False]}], 
                                label = "sigmoidal",
                                method = "update"
                            ),
                            dict (
                                args = [{'visible': [True, False, False, False, False, True, False]}], 
                                label = "b-spline",
                                method = "update"
                            ),
                             dict (
                                args = [{'visible': [True, False, False, False, False, False, True]}], 
                                label = "Cubic-spline",
                                method = "update"
                            ),
                            dict (
                                args = [{'visible': [True, True, True, True, True, True, True]}], 
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
                         x = -0.5, y = 1.2, yref = "paper", align = "left")
                ],
                title=go.layout.Title(text="Different Basis Functions", x = 0.5)
            )
            #self.fig.show()

    
    def __call__(self, *args, **kwargs):
        return self.fig
    
    def fig(self):
        return self.fig
        

        

                

                


    
            
            