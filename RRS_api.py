# -*- coding: utf-8 -*-
 
import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("lg2.pkl","rb")
lg2=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(gender,location_number,latitude_x,longitude_x):
    prediction=lg2.predict([[gender,location_number,latitude_x,longitude_x]])
    print(prediction)
    return prediction

def main():
    st.title("Restaurent Recommandation System")
    html_temp = """
   <div style="background-color:tomato;padding:10px">
   <h2 style="color:white;text-align:center;">Streamlit Restaurent Recommandation ML App </h2>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender= st.text_input("gender", "type here")
    location_number= st.text_input("location_number", "type here")
    latitude_x=st.text_input("latitude_x", "type here")
    longitude_x=st.text_input("longitude_x", "type here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(gender,location_number,latitude_x,longitude_x)
    st.success('The output is {}'.format(result))
        
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
    
if __name__=='__main__':
    main()
    