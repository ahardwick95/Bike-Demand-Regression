import streamlit as st
def Intro():

    st.markdown("<h1 style='text-align: center;'> 🚴‍♂️ Bike Demand Predictor \n</h1>", unsafe_allow_html=True)

    st.markdown("""  Welcome to the Bike Demand Predictor application!""")
    st.markdown("This software uses real-world factors such as seasons and temparature to predict the daily bikes rented from Capital BikeShare system for a given day.")
        
    
    st.markdown("This application was built with *scikit-learn's Random Forest Model*  and compared with my *custom regression model* for accuracy and performcne insights.")
    st.markdown(" You can cycle through other pages in the application with Navigation sidebar on the left. ")



    st.image("Bike_pic.jpg",use_container_width=True)