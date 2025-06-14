import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression


class The_Test:
    def __init__(self,S,F,I,N,Seed,Model):
        self.Samples = S    # Number of samples
        self.Features = F   # Number of features (predictors)
        self.Info = I       # Number of features used to generate y
        self.Noise = N      # Add Gaussian noise to the output, ehlps to similuate real-wolrd data
        self.Seed = Seed    # Seed for reproducibility


        # Generates synthetic regression data for testing
        x_data, y_data =  make_regression(n_samples=self.Samples, n_features=self.Features, n_informative=self.Info, noise=self.Noise, random_state=self.Seed )


        # %60 training set, 20% validation set, 20% test set
        x_train, val_x, y_train, val_y = train_test_split(x_data, y_data, random_state=104, test_size=0.4, shuffle=True)  # 60-40 split
        X_temp, test_X, y_temp, test_Y = train_test_split(val_x, val_y, random_state=104, test_size=0.5, shuffle=True)  # Further 50-50 split

        #-------- Model training and evaluation------------------------
        Model.fit(x_train, y_train, 0.85,150)

        # Evalutation results for validation data
        Reg_MSE_val = Model.MSE(val_x,val_y)
        Reg_RMSE_val = Model.RMSE(val_x,val_y)
        Reg_MAE_val = Model.MAE(val_x,val_y)
        Reg_R_2_val = Model.R_2(val_x,val_y)

        print(f'The MSE validation error of the model is {Reg_MSE_val}')
        print(f'The RMSE validation error of the model is {Reg_RMSE_val}')
        print(f'The MAE validation error of the model is {Reg_MAE_val}')
        print(f'The R2 value of the model on the validation set is {Reg_R_2_val}\n')
   
  
        # Evalutation results for test data
        Reg_MSE_Test = Model.MSE(test_X,test_Y)
        Reg_RMSE_Test = Model.RMSE(test_X,test_Y)
        Reg_MAE_Test = Model.MAE(test_X,test_Y)
        Reg_R_2_Test = Model.R_2(test_X,test_Y)

        print(f'The MSE error of the model is {Reg_MSE_Test}')
        print(f'The RMSE error of the model is {Reg_RMSE_Test}')
        print(f'The MAE error of the model is {Reg_MAE_Test}')
        print(f'The R2 value of the model is {Reg_R_2_Test}\n')

        # If the number of features is one, (i.e. y=mx+b), best fitted line will be plotted and displayed
        if (self.Features==1):
            y_pred=Model.Predict(x_data)
            plt.scatter(x_data,y_data, marker='o')
            plt.plot(x_data, y_pred, color='red')
            plt.title("Line of Best Fit For Random Data")
            plt.show()
