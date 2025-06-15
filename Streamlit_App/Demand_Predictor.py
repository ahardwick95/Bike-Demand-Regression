import  streamlit as st
from joblib import dump,load
import pandas as pd
import numpy as np




def Predictor():
    The_Forest=load("Forest_Regressor.joblib")
    
    st.markdown("<h1 style='text-align: center;'>  Bike Rentel Predictor \n</h1>", unsafe_allow_html=True)
    st.markdown(" Please input data the following data to predict total amount of bikes rented : ")
    Instant = st.number_input("Give a specific day, day 1 is 01/01/2011 , day 731 is 12/31/2012 ", value=0, step=1)
    Season = st.number_input(" What season is it?  Winter : 1  Spring : 2  Summer : 3  Fall : 4",min_value=1, max_value=4, value=1, step=1)
    Year = st.number_input(" What's the year ?,  0 is 2011 , 1 is 2012?", min_value=0, max_value=1,value=0, step=1)
    Month = st.number_input(" What's the month ?,  values go from 1-12, 1 is January, 12 is December",min_value=1, max_value=12, value=1, step=1)
    Holiday = st.number_input(" Is this day a holiday ?, 0 for No, 1 for Yes?", min_value=0, max_value=1,value=0, step=1)
    Weekday = st.number_input(" What's the day of the week ?, 0 is Sunday , 6 is Saturday", value=0, step=1)
    Workday = st.number_input(" Is the day a workday ?, 0 is No , 1 is Yes", value=0, step=1)
    Weather_Conditions = st.number_input(" What's the weather Like ?, 0 is Clear , 1 is Cloudy , 2 is Bad Weather", min_value=0, max_value=2,value=0, step=1)
    Temparature = st.number_input("Enter Temparature(Celsius), values are nomaralized.", min_value=0.000000, max_value=1.000000, value=0.0, step=0.000001)
    A_Temparature = st.number_input("What temperature do you think it is?, values are nomaralized.", min_value=0.000000, max_value=1.000000, value=0.0, step=0.000001)
    Humidity = st.number_input("Enter the Humidity, values are nomaralized.", min_value=0.000000, max_value=1.000000, value=0.0, step=0.000001)
    Windspeed = st.number_input("Enter the Windspeed, values are nomaralized.", min_value=0.000000, max_value=1.000000, value=0.0, step=0.000001)
    The_Values = pd.DataFrame([Instant,Season,Year,Month,Holiday,Weekday,Workday,Weather_Conditions,Temparature,A_Temparature,Humidity,Windspeed])
    st.write(f"The prediciton for total amount of Bikes rented is {The_Forest.predict(The_Values.T)}")
    
