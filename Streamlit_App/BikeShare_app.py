import streamlit as st
import pandas as pd
from Intro import Intro
from year_2011 import Analytics_2011
from year_2012 import Analytics_2012
from Both_Years import Analytics
from Important_Features import The_Features
from Demand_Predictor import Predictor
from Model_V_Forest import comparator
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bike Demand Predictor",layout="wide")

df = pd.read_csv("Streamlit_App/data/day.csv")

# THe following will exclusively be used in the Model_V_Forest function
df_2 = df.drop(['dteday','casual','registered'],axis=1)
X = df_2.drop('cnt',axis=1)
Y = df_2['cnt']

st.sidebar.title("🚲 Navigation")
selected_page = st.sidebar.selectbox("Choose a page:", ["About", "Bike Demand Prediction","2011 Analytics", "2012 Analytics",
                                                        "Analytics for both years","Important Features", "Custom Model Metrics" ])

if selected_page == "About":
    Intro()
elif selected_page == "Bike Demand Prediction":
    Predictor()
elif selected_page == "2011 Analytics":
    Analytics_2011(df)
elif selected_page == "2012 Analytics":
    Analytics_2012(df)
elif selected_page == "Analytics for both years":
    Analytics(df)
elif selected_page == "Important Features":
    The_Features(df)
elif selected_page == "Custom Model Metrics":
    comparator(X,Y)
