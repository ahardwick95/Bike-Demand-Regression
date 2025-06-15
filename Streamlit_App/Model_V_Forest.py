import  streamlit as st
from joblib import dump,load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


The_Forest=load("Forest_Regressor.joblib")
MyModel=load('My_Model.joblib')
def comparator(X,Y):
    st.markdown("<h1 style='text-align: center;'> My Model (blue) Vs Random Forest (red) </h1>", unsafe_allow_html=True)
    Reg_MSE=MyModel.MSE(X,Y)
    Reg_RMSE=MyModel.RMSE(X,Y)
    Reg_MAE=MyModel.MAE(X,Y)
    Reg_R_2=MyModel.R_2(X,Y)

    MyModel_Scores=[Reg_RMSE,Reg_MAE]

    Random_Tree_test_Pred=The_Forest.predict(X)

    Random_Tree_MSE=mean_squared_error(Y,Random_Tree_test_Pred)
    Random_Tree_RMSE=np.sqrt(Random_Tree_MSE)
    Random_Tree_MAE=mean_absolute_error(Y,Random_Tree_test_Pred)
    Random_Tree_R_2=r2_score(Y,Random_Tree_test_Pred)

    Forest_Scores=[Random_Tree_RMSE,Random_Tree_MAE]
    Categories=['RMSE','MAE']

    col1,col2=st.columns(2)

    with col1:
        fig=plt.figure(figsize=(16, 11))
        sns.barplot(x=Categories, y=MyModel_Scores)
        plt.xlabel('Metrics')
        plt.ylabel('Scores')
        plt.title(' Metrics for My Model ')
        st.pyplot(fig)
        

    with col2:
        fig2=plt.figure(figsize=(16, 11))
        sns.barplot(x=Categories, y=Forest_Scores, color='red')
        plt.xlabel('Metrics')
        plt.ylabel('Scores')
        plt.title(' Metrics for Random Forest Model')
        st.pyplot(fig2)
    
  

    with col1:
        fig=plt.figure(figsize=(12, 11))
        sns.barplot(x=['R2'], y=Reg_R_2)
        plt.xlabel('R2')
        plt.ylabel('value')
        plt.title(' R2 value for My Model ')
        st.pyplot(fig)
        

    with col2:
        fig2=plt.figure(figsize=(12, 11))
        sns.barplot(x=['R2'], y=Random_Tree_R_2,color='red')
        plt.xlabel('R2')
        plt.ylabel('value')
        plt.title(' R2 value for Random Forest Model')
        st.pyplot(fig2)

    with st.expander("Click for more details"):
        st.write(""" As we can see, the performance of my current Regression model is abysmal in comparison to scikit-learn's Random Forest Model.\n My model's
                  scores for RMSE and MAE is far larger than those for the Randdom Forest Model. 
                 Based on the R2 values, scikit-learn's model is a far better fit for the data than my model.\n  """)
        st.write("All in all, I have gained valuable insight from failures of my model and plan to tinker with new features to improve it's performance.\n")
        
        st.write(" The following are the future enhancements that I will add to my model:\n")
        st.write(" 1. Normal equation implementation, if the datset isn't too large, this would be an efficient means to help fit the data.\n")
        st.write(""" 2. Lasso and Ridge regression options, the methods will allow my model to 
                 learn the important features faster and also more robust to large values.\n""")
        st.write(" 3. Stochastic and mini-batch Gradient-descent variations, this will help my model learn faster and interact better with large datasets.\n")
        st.write(" Note: MSE was left out of metrics comparison because the value  overshadowed the others and would prevent accurate comparisons.")
