# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:29:34 2023

@author: DELL
"""

import streamlit as st
import numpy as np
import pickle
Regressor= pickle.load(open('Students_Mark_predictor_model.pkl','rb'))

def predict_student_study_hours(input_data):
   inputa = np.asarray(input_data)
   smt = inputa.reshape(1,-1)
   Prediction = Regressor.predict(smt)[0][0]
   Prediction = (Prediction%10)
   Prediction = Prediction.round(2)
   return Prediction

def main():
    st.title("Student Study Hours Prediction Using Machine Learning")
    html_temp ="""
    <div style="background-color:tomato; padding: 10px">
    <h2 style="color:Blue; text-align:center;">Student Study Hours Prediction</h2>
    </div>
    """
    marks = st.text_input("Enter Your Marks : ","")
    result = ""
    if (st.button("Predict")):
        result = predict_student_study_hours([int(marks)])
    st.success('Student Studies  {}  Hours in a Day'.format(result))
    if st.button("About Me"):
        st.text("Created by Vedant Gujarathi")
        
if __name__ == '__main__':
    main()