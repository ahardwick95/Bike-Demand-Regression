import numpy as np
import pandas as pd


class Regression_Model:
    def __init__(self):
        self.w = None  # Initialize weights for each feature
        self.b = None  # Initialize bias

    def H_Function(self, X):
        return np.dot(X, self.w) + self.b

    
    def MSE(self, X, Y):  # Mean Square Error
        Y_pred = self.Predict(X)
        error = np.mean((Y - Y_pred) ** 2)
        return error

    def RMSE(self, X, Y):  # Mean Square Error
        Y_pred = self.Predict(X)
        error = np.mean((Y - Y_pred) ** 2)
        RMSE=np.sqrt(error)
        return RMSE

    def MAE(self, X, Y):  # Mean Absolute Error
        Y_pred = self.Predict(X)
        error = np.mean(np.abs(Y - Y_pred))
        return error

    def R_2(self, X, Y):  # R-squared
        Y_pred = self.Predict(X)
        Y_Mean=np.mean(Y)
        Sum_Resid=np.sum((Y - Y_pred)**2)
        Sum_Squares=np.sum((Y - Y_Mean)**2)
        R_2=1-(Sum_Resid/Sum_Squares)
        return R_2

    def Gradient(self, X, Y, a):  # batch gradient for MSE
        m = X.shape[0]
        predictions = self.Predict(X)  # Predictions based on current weights and biases
        errors = predictions - Y  # (y_prediction - Y_target) for entire dataset
        gradient_w = (1 / m) * np.dot(X.T, errors)
        gradient_b = (1 / m) * np.sum(errors)
        self.w -= a * gradient_w
        self.b -= a * gradient_b

    def fit(self, X, Y, a, n):  # Gradient Descent w.r.t MSE
        self.w = np.zeros(X.shape[1])
        self.b = 0
        for i in range(n):
            self.Gradient(X, Y, a)

    def Predict(self, X):
        return self.H_Function(X)
