from joblib import dump,load
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def The_Features(df):
    st.markdown("<h1 style='text-align: center;'> Feature Importance Chart \n </h1>", unsafe_allow_html=True)
    #Construct the Feature dataset
    X=df.drop(['casual','registered','cnt','dteday'],axis=1)

    # Load up the Random Forest model we trained
    Forest_Model=load('Forest_Regressor.joblib')
    
    # stores how important each feature is to determing the target variable
    F_Importances=Forest_Model.feature_importances_

    # Compare the value of each feature with a bar graph, display it for the user
    fig=plt.figure(figsize=(16, 9))
    plt.bar(X.columns,F_Importances, color="red")
    plt.xlabel("Features")
    plt.ylabel("Importance Values")
    plt.xticks(rotation=45)  
    plt.tight_layout() 
    st.pyplot(fig)

    with st.expander("Click for more details"):
        st.write(""" The feature with the most value or information in predicting 
        total bike rentals is the day itself. \n As evidenced from the 2011-2012 analytics,
                  there is a noticeable trend with the seasosns throughout the year that help forecast bike rental count. \n Also how a person feels about the weather (i.e. atemp feature) seems to determine if they will rent a bike for that day.""")
    