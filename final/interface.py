import plotly.graph_objects as go
import plotly.express as px
import models

class Model:
    
    def __init__(self, data):
        self.data = data
        self.compare = models.Model42(data=data, bf = None).fig
        self.compare.show()
        self.polynomial = models.Model42(data=data, bf = "polynomial").fig
        self.gaussian = models.Model42(data=data, bf = "gaussian").fig
        self.sigmoidal = models.Model42(data=data, bf = "sigmoidal").fig
        self.periodical= models.Model42(data=data, bf = "periodical").fig
        self.bspline = models.Model42(data=data, bf = "bspline").fig
        self.cubicspline= models.Model42(data=data, bf = "cubicspline").fig
        #self.figures = [self.compare.to_dict(), self.polynomial.to_dict(), self.gaussian.to_dict(), self.sigmoidal.to_dict(), self.periodical.to_dict(), self.bspline.to_dict(), self.cubicspline.to_dict()]
        

        
        