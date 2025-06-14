import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def Analytics(Bike_data):
    
    st.markdown("<h1 style='text-align: center;'> 2011 and 2012 Analytics </h1>", unsafe_allow_html=True)

    df_test_1=Bike_data[['mnth','cnt']]
    BD_2012_Months=df_test_1.groupby(['mnth'], as_index=False)['cnt'].mean()

    col1,col2=st.columns(2)

    df_test_2=Bike_data[['season','cnt']]
    Season_v_Cnt=df_test_2.groupby(['season'], as_index=False)['cnt'].mean()

    df_test_3=Bike_data[['weathersit','cnt']]
    Weather_v_Cnt=df_test_3.groupby(['weathersit'], as_index=False)['cnt'].mean()

    with col1:
        fig=plt.figure(figsize=(16, 11))
        sns.barplot(x='mnth', y='cnt', data=BD_2012_Months)
        plt.xlabel('Months')
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes rented for 2011-2012 (Figure 1)')
        st.pyplot(fig)

    with col2:
        fig2=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Winter','Spring','Summer','Fall'], y='cnt', data=Season_v_Cnt)
        plt.xlabel('Seasons')
        plt.xticks(rotation=45)
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes Rented Per Season for 2011-2012 (Figure 2)')
        st.pyplot(fig2)

    col3,col4=st.columns(2)
    with col3:
        fig3=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Clear','Cloudy','Bad Weather'], y='cnt', data=Weather_v_Cnt)
        plt.xlabel('Weather Conditions')
        plt.xticks(rotation=45)  
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes rented for 2011-2012 (Figure 3)')
        st.pyplot(fig3)
    
    with col4:
        fig4=plt.figure(figsize=(16, 12))
        plt.scatter(Bike_data['temp'],Bike_data['cnt'], color="#0f0", marker="o" ,s=100)
        plt.title("Temp vs Bike Rentals for 2011-2012 (Figure 4)", fontsize=30, fontname="Calibri")
        plt.xlabel("Temperature") 
        plt.ylabel("Total Bike Rentals")
        st.pyplot(fig4)
    
    with st.expander("📊 Review Chart Explanations"):
    # Dropdown to pick which chart explanation to show
        choice = st.selectbox("Select a chart to review explanation:", 
                          ["Figure 1 : Average Bikes rented for 2011-2012","Figure 2 : Average Bikes Rented Per Season for 2011-2012", 
                           "Figure 3 : Weather vs Total Bike Rentals 2011-2012", "Figure 4 : Temp vs Bike Rentals for 2011-2012"])

    # Show explanation based on choice
    if choice == "Figure 1 : Average Bikes rented for 2011-2012":
        st.write("""The average amount of bikes rented were the highest between June and Septemeber. 
                 This is likely due to Summer beginning in June and ending in September.""")

    elif choice == "Figure 2 : Average Bikes Rented Per Season for 2011-2012":
        st.write(""" Winter had the lowest amount of rentals, while Summer had the highest. 
                 People tend to stay inside more during colder weather, but venture out during warmer weather.""")

    elif choice == "Figure 3 : Weather vs Total Bike Rentals 2011-2012":
        st.write(""" Clear weather has the most bikes rented in both years, while inclement weather having substantially lower in comparison.""")

    elif choice == "Figure 4 : Temp vs Bike Rentals for 2011-2012":
        st.write("""Warm to hot weather leads to more bikes being rented. Further evidence of this observation can be seen in Figure 2""")