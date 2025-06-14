import numpy as np
import pandas as pd


class Regression_Model:
    def __init__(self):
        self.w = None  # Initialize weights for each feature
        self.b = None  # Initialize bias

    def H_Function(self, X): # hypothesis function
        return np.dot(X, self.w) + self.b

 #------Metrics used to evaluate the model--------------
    
    def MSE(self, X, Y):  # Mean Square Error
        Y_pred = self.Predict(X)
        error = np.mean((Y - Y_pred) ** 2)
        return error

    def RMSE(self, X, Y):  # Root Mean Square Error
        Y_pred = self.Predict(X)
        error = np.mean((Y - Y_pred) ** 2)
        RMSE=np.sqrt(error)
        return RMSE

    def MAE(self, X, Y):  # Mean Absolute Error
        Y_pred = self.Predict(X)
        error = np.mean(np.abs(Y - Y_pred))
        return error

    def R_2(self, X, Y):  # Coefficient of Determination
        Y_pred = self.Predict(X)
        Y_Mean=np.mean(Y)
        Sum_Resid=np.sum((Y - Y_pred)**2)
        Sum_Squares=np.sum((Y - Y_Mean)**2)
        R_2=1-(Sum_Resid/Sum_Squares)
        return R_2
#------------------------------------------------------
    
    # Gradient will help the model find the optimal solution by adjusting the weights and baises with the learning rate and error computation
    
    def Gradient(self, X, Y, a):  # batch gradient for MSE
        m = X.shape[0]
        predictions = self.Predict(X)  # Predictions based on current weights and biases
        errors = predictions - Y  # (y_prediction - Y_target) for entire dataset
        gradient_w = (1 / m) * np.dot(X.T, errors) # Computes the gradient for the weights
        gradient_b = (1 / m) * np.sum(errors) # Computes the gradient for the bias
        self.w -= a * gradient_w #
        self.b -= a * gradient_b

    # The fit function will run the gradient function several times based on the number of given of iterations, n
    def fit(self, X, Y, a, n):  # Gradient Descent w.r.t MSE
        # Initialize both the weights and bias to 0
        self.w = np.zeros(X.shape[1])
        self.b = 0
        for i in range(n):
            self.Gradient(X, Y, a)

    
    def Predict(self, X): # gives a array of predicted values based on the adjsuted weights and bias from training, used in the metric functions
        return self.H_Function(X)
