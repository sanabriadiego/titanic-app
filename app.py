import streamlit as st
import numpy as np
from prediction import predict

st.write("Hello World")

pclass = st.selectbox('What was your passenger class?', [1,2,3])
sex = st.selectbox('What is your sex?', [1, 0])
sibsp = st.selectbox('Number of siblings aboard', [0,1,2,3])
parch = st.selectbox('Number of parentsa aboard', [0,1,2])

X = np.array([[pclass, sex, sibsp, parch]])

if st.button('Titanic!'):
    result = predict(X)
    st.text(result[0])
