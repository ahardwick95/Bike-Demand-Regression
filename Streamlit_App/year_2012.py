import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

def Analytics_2012(Bike_data):

    st.markdown("<h1 style='text-align: center;'> 2012 Analytics \n</h1>", unsafe_allow_html=True)

    Bike_data_2012 = Bike_data[Bike_data['yr'] == 1]
    

    df_test_1=Bike_data_2012[['mnth','cnt']]
    BD_2012_Months=df_test_1.groupby(['mnth'], as_index=False)['cnt'].mean()

    col1,col2=st.columns(2)

    df_test_2=Bike_data_2012[['season','cnt']]
    Season_v_Cnt=df_test_2.groupby(['season'], as_index=False)['cnt'].mean()

    df_test_3=Bike_data_2012[['weathersit','cnt']]
    Weather_v_Cnt=df_test_3.groupby(['weathersit'], as_index=False)['cnt'].mean()

    with col1:
        fig=plt.figure(figsize=(16, 11))
        sns.barplot(x='mnth', y='cnt', data=BD_2012_Months)
        plt.xlabel('Months')
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes rented for 2012 (Figure 1)')
        st.pyplot(fig)

    with col2:
        fig2=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Winter','Spring','Summer','Fall'], y='cnt', data=Season_v_Cnt)
        plt.xlabel('Seasons')
        plt.xticks(rotation=45)
        plt.ylabel('Average Bikes Rented')
        plt.title('Average Bikes Rented Per Season for 2012 (Figure 2)')
        st.pyplot(fig2)

    col3,col4=st.columns(2)
    with col3:
        fig3=plt.figure(figsize=(16, 11))
        sns.barplot(x=['Clear','Cloudy','Bad Weather'], y='cnt', data=Weather_v_Cnt)
        plt.xlabel('Weather Conditions')
        plt.xticks(rotation=45)  
        plt.ylabel('Average Bikes Rented')
        plt.title(' Weather vs Total Bikes Rented for 2012 (Figure 3)')
        st.pyplot(fig3)
    
    with col4:
        fig4=plt.figure(figsize=(16, 12))
        plt.scatter(Bike_data_2012['temp'],Bike_data_2012['cnt'], color="#0f0", marker="o" ,s=100)
        plt.title("Temp vs Bike Rentals for 2012 (Figure 4)", fontsize=30, fontname="Calibri")
        plt.xlabel("Temperature") 
        plt.ylabel("Total Bike Rentals")
        st.pyplot(fig4)


    with st.expander("📊 Review Chart Explanations"):
    # Dropdown to pick which chart explanation to show
        choice = st.selectbox("Select a chart to review explanation:", 
                          ["Figure 1 : Average Bikes rented for 2012","Figure 2 : Average Bikes Rented Per Season for 2012", 
                           "Figure 3 : Weather vs Total Bike Rentals 2012", "Figure 4 : Temp vs Bike Rentals for 2012"])

    # Show explanation based on choice
    if choice == "Figure 1 : Average Bikes rented for 2012":
        st.write("""The average amount of bikes rented for each month considerably higher when compared to each month in 2011. 
                 This time around, September experienced the highest amount of bikes rented.  """)

    elif choice == "Figure 2 : Average Bikes Rented Per Season for 2012":
        st.write(""" Winter again exhibited the lowest amount of bikes rented, while summer experienced the highest. This establishes that there is a trend with the time of the year
                 that can help forecast how many bikes consumers will rent in the future.""")

    elif choice == "Figure 3 : Weather vs Total Bike Rentals 2012":
        st.write(""" The trend is more or less the same when compared to 2011. 
                 However in this case, the average of amount of bikes is still higher in comparison as well. 
                 The most likely explanation would be that the CBS ( Capital Bikeshare System) has been more widely assimilated into society at this point in time.""")

    elif choice == "Figure 4 : Temp vs Bike Rentals for 2012":
        st.write(""" Same trend as 2011 but with a higher amount of bikes rented.""")