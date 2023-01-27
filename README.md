# Task-42

*To do: First Steps*

- Introduction: #Emad
     - why do we use different basic functions and how do they work
     - how to use model
     - how to evaluate fit

Basis functions are a powerful tool in modeling and understanding complex phenomena. They allow us to represent a function as a linear combination of simpler functions, making it easier to estimate and understand. There are several types of basis functions, each with its own unique properties and advantages. Polynomial, Gaussian, Sigmoidal, Periodical, B-Splines, and Cubic Spline are some examples of commonly used basis functions. As we increase the number of basis functions, our model becomes more accurate, but there is a risk of overfitting if we use too many. This is why the process of model selection is crucial and involves finding the appropriate number of basis functions and the appropriate value for the regularization parameter λ. Our goal is to find the ‘best’ model, which is the one that generalizes well on future data. To evaluate the performance of our model, we use metrics such as R-squared, Akaike Information Criterion (AIC), or Bayesian Information Criterion (BIC) on a test dataset. This allows us to determine the model with the lowest generalization error, which is the performance of the model on unseen data. Additionally, to prevent overfitting, it is important to divide our training dataset into three parts: training, validation, and test datasets. Using the training dataset to train our model, the validation dataset for model selection and the test dataset for final evaluation, we can ensure that our model has the lowest generalization error.
       
- Basic Functions: 
    - how do they look? #Kim
    - when to use? #Kim
    - implement in .py #Judith
        - Polynomial
        - Gaussian
        - Sigmoidal
        - Periodical
        - (B-Splines)
        - (Cubic Spline)
    
- for the model: #Lea
    - dropdown menu?
    - dataset?
    - .py for regression, RMSE
