import streamlit as st
import joblib
import numpy as np

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> House Price Prediction</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('house_joblib')
    
    p1 = st.slider('Avg. Area Income',17000,200000)
    
    p2 = st.slider("Avg. Area House Age",2,30)
        
    p3 = st.slider("Avg. Area Number Of Rooms",2,20)
    
    
    
    p4 = st.slider("Enter number of bedrooms",2,8)
    
    
    p5 = st.number_input("Enter area population")
    
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5]])
        
        st.balloons()
        st.success('Your House Price is {}'.format(round(pred[0],2)))
        
    
    
        
    
    
    
if __name__ == '__main__':
    main()
