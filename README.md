# Task-42

*To do: First Steps*

- Introduction: #Emad
     - why do we use different basic functions and how do they work
     - how to use model
     - how to evaluate fit

Slide 1:Basis functions are a powerful tool in modeling and understanding complex phenomena. They allow us to represent a function as a linear combination of simpler functions, making it easier to estimate and understand. 

Slide 2: There are several types of basis functions, each with its own unique properties and advantages. Polynomial, Gaussian, Sigmoidal, Periodical, B-Splines, and Cubic Spline are some examples of commonly used basis functions. 
Polynomial basis functions are used for modelling simple relationships between predictors and targets.
Gaussian basis functions use the Gaussian probability density function as a basis function. Because they can model non-linear relationships very well they are for example used for supervised learning problems with non-linear relationships between predictor and target. They are local basis functions, which is useful because of its faster computation.
Sigmoidal basis functions are also used for non-linear relationships in the data. An example of its field of use is in the learning of neuronal networks and the discovery of  functions which suit well for the resolving in supervised learning.
Periodical basis functions are used for phenomena that happen periodically. For example: oscillations, clustering or time series analysis.
B-splines can be used to approximate splines over a set of points. They are also used to approximate nonlinear functions and non-periodic data. They can f.e. be used for computer aided geometry design programs.
Cubic splines are piecewise cubic functions presented as a smooth curve with a given set of points. So it is used for situations where smooth curves have to be modeled. It is an efficient method for data interpolation and is used by f.e. engineering for curve fitting.
 
Slide 3: As we increase the number of parameters, our model becomes more accurate, but there is a risk of overfitting if we use too many. Here you can see a graphical example for underfitting, a good fit to the data and overfitting .This is why the process of model selection is crucial and involves finding the appropriate choice of basis functions and the appropriate value for the regularization parameter λ. Our goal is to find the ‘best’ model, which is the one that generalizes well on future data.
To evaluate the performance of our model, we use metrics such as root mean-squared error, Akaike Information Criterion (AIC), or Bayesian Information Criterion (BIC) on a test dataset. This allows us to determine the model with the lowest generalization error, which is the performance of the model on unseen data. Here you can see how rmse indicates how well the chosen basis function approximate. Additionally, to prevent overfitting, it is important to divide our training dataset into three parts: training, validation, and test datasets. Using the training dataset to train our model, the validation dataset for model selection and the test dataset for final evaluation, we can ensure that our model has the lowest generalization error.

source:
     - https://machinelearningmastery.com/probabilistic-model-selection-measures/
     - https://towardsdatascience.com/model-selection-in-machine-learning-813fe2e63ec6
     - https://towardsdatascience.com/how-to-improve-your-linear-regression-with-basis-functions-and-regularization-8a6fcebdc11c
     - https://www.theanalysisfactor.com/assessing-the-fit-of-regression-models/
     - https://www.dbs.ifi.lmu.de/Lehre/MaschLernen/SS2016/Skript/BasisFunctions2016.pdf
     - Neuroinfo lectures 7-10
       
- Basic Functions: 
    - how do they look? #Kim
    -     Images in the 10.presentation    
    - when to use? #Kim
    - 
    - implement in .py #Judith
        - Polynomial
        - Are used for modelling simple relationships between predictors             and targets.
        - Gaussian
        - The Gaussian basis function uses the Gaussian probability               density function as a basis function. Because it can model               non-linear relationships very well it is for example used for           supervised learning problems with non-linear relationships               between predictor and target. It is a local basis function,              which is useful because of its faster computation.
        - Sigmoidal
        - The Sigmoidal basis function is also used for non-linear                 relationships in the date. An example of its field of use is             in the learning of neuronal networks and the discovery of               functions which suit well for the resolving in supervised               learning.
        - Periodical
        - The Periodical basis function is used for phenomena that                  happen periodically. For example: oscillations, clustering or            time series analysis.
        - (B-Splines)
          B-splines can be used to approximate splines over a set of               points. They are also used to approximate nonlinear functions             and non-periodic data. They can f.e. be used for computer                 aided geometry design programs.
        - (Cubic Spline)
          A cubic spline is a piecewise cubic function presented as a               smooth curve with a given set of points. So it is used for               situations where smooth curves have to be modeled. It is an               efficient methods for data interpolation and is used by f.e.             engineering for curve fitting.
    
- for the model: #Lea
    - dropdown menu?
    - dataset?
    - .py for regression, RMSE
    
    
    
References:
The Chemical Statistican, https://chemicalstatistician.wordpress.com/tag/gaussian-basis-function-models/, last accessed: 30.01.23
Machine Learning Mastery, A Gentle Introduction To Sigmoid Function - MachineLearningMastery.com, last accessed 30.01.23
Pages.mtu.edu, https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/B-spline/bspline-basis.html, last accessed 30.01.23
Skript by Antonia WItttmers and Maria Gensel, Modellierung von Kurven und Flächen mittels B-Splines, http://www.inf.fu-berlin.de/lehre/SS06/Computergraphik/skript/vorlesung4.pdf , last accessed 01.02.23
Computational Nuclear Engineering and Radiological Science Using Python Chapter 10 by Ryan G McClarren(2018), https://www.sciencedirect.com/science/article/pii/B9780128122532000121, last accessed 01.02.23
Cubic spline interpolation for petroleum engineering data, ResearchGate(2014) https://www.researchgate.net/publication/287245396_Cubic_spline_interpolation_for_petroleum_engineering_da, last accessed 01.02.23

