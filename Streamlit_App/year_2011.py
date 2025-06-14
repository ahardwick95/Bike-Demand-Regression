import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd


def Analytics_2011(Bike_data):

    st.markdown("<h1 style='text-align: center;'> 2011 Analytics </h1>", unsafe_allow_html=True)
    Bike_data_2011 = Bike_data[Bike_data['yr'] == 0]
    

    df_test_1=Bike_data_2011[['mnth','cnt']]
    BD_2011_Months=df_test_1.groupby(['mnth'], as_index=False)['cnt'].mean()

    col1,col2=st.columns(2)

    df_test_2=Bike_data_2011[['season','cnt']]
    Season_v_Cnt=df_test_2.groupby(['season'], as_index=False)['cnt'].mean()

    df_test_3=Bike_data_2011[['weathersit','cnt']]
    Weather_v_Cnt=df_test_3.groupby(['weathersit'], as_index=False)['cnt'].mean()

    

    with col1:
        fig=plt.figure(figsize=(16, 11))
        sns.barplot(x='mnth', y='cnt', data=BD_2011_Months)
        plt.xlabel('Months')
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes rented for 2011 (Figure 1)')
        st.pyplot(fig)
        

    with col2:
        fig2=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Winter','Spring','Summer','Fall'], y='cnt', data=Season_v_Cnt)
        plt.xlabel('Seasons')
        plt.xticks(rotation=45)
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes Rented Per Season for 2011 (Figure 2)')
        st.pyplot(fig2)

    col3,col4=st.columns(2)
    with col3:
        fig3=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Clear','Cloudy','Bad Weather'], y='cnt', data=Weather_v_Cnt)
        plt.xlabel('Weather Conditions')
        plt.xticks(rotation=45)  
        plt.ylabel('Average Bikes Rented')
        plt.title('Weather vs Total Bike Rentals 2011 (Figure 3)')
        st.pyplot(fig3)
    
    with col4:
        fig4=plt.figure(figsize=(16, 11))
        plt.scatter(Bike_data_2011['temp'],Bike_data_2011['cnt'], color="#0f0", marker="o" ,s=100)
        plt.title("Temp vs Bike Rentals for 2011 (Figure 4)", fontsize=30, fontname="Calibri")
        plt.xlabel("Temperature") 
        plt.ylabel("Total Bike Rentals")
        st.pyplot(fig4)


    with st.expander("📊 Review Chart Explanations"):
    # Dropdown to pick which chart explanation to show
        choice = st.selectbox("Select a chart to review explanation:", 
                          ["Figure 1 : Average Bikes rented for 2011","Figure 2 : Average Bikes Rented Per Season for 2011", 
                           "Figure 3 : Weather vs Total Bike Rentals 2011", "Figure 4 : Temp vs Bike Rentals for 2011"])

    # Show explanation based on choice
    if choice == "Figure 1 : Average Bikes rented for 2011":
        st.write("""There was a noticeabale spike in the amount of bikes rented from January to June, 
                 with the June having the highest amount of bikes rented in 2011. After June, there was a steady then somewhat sharp decline in Decemeber.""")

    elif choice == "Figure 2 : Average Bikes Rented Per Season for 2011":
        st.write(""" Winter exhibited the lowest amount of bikes rented, while summer experienced the highest. 
                 This indicates that season and temperature play a significant role in determining the total amount of bikes rented for a particular day. """)

    elif choice == "Figure 3 : Weather vs Total Bike Rentals 2011":
        st.write(""" When the weather is clear, consumers tend to rent more bikes as opposed to when the weather condition is less than ideal or horrible. """)

    elif choice == "Figure 4 : Temp vs Bike Rentals for 2011":
        st.write(""" The warmer the weather the more likely people are to rent bikes, furthered evidenced by summer being the month with most bikes rented (i.e. Figure 2) .""")