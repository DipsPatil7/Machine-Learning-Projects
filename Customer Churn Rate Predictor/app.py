# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:08:46 2023

@author: Deepak
"""

import streamlit as st
import pickle


load = open('random_forest.pkl', 'rb')
model = pickle.load(load)

st.title(' Telecommunication Company Churn Prediction')
# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("churn-prediction.jpg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=700)

def predict(intl_plan, day_mins, customer_calls, voice_messages, day_charge):
    pred= model.predict([[intl_plan, day_mins, customer_calls, voice_messages, day_charge]])
    return pred

def start():
    intl_plan = st.selectbox('Do you have intl plan',('yes', 'no'))
    intl_plan_encoded = 1 if intl_plan.lower() == 'yes' else 0
    day_mins = st.number_input('how many day mins calls')
    customer_calls = st.number_input('customer calls')
    voice_messages= st.number_input('number of voice messages')
    day_charge = st.number_input('charges paid for day')
    
    if st.button('Predict'):
        result = predict(intl_plan, day_mins, customer_calls, voice_messages, day_charge)
        st.success('will customer churn? {}'.format(result))
        
if __name__=='__main__':
    start()
    
    
    
    
    
    

