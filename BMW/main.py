import streamlit as st
import numpy as np 
import pandas as pd 

st.title("Kalkulator Sederhana Streamlit")
st.write("Operasi matematika dari dua input")
st.sidebar.header("Operasi Matematika")
num1 = st.number_input("Angka Pertama")
num2 = st.number_input("Angka Kedua")

if st.sidebar.button("Tambah") : 
    st.write("Hasil ="+str(num1+num2))
if st.sidebar.button("kurang"):
    st.write("Hasil ="+str(num1-num2))
if st.sidebar.button("kali"):
    st.write("Hasil ="+str(num1*num2))
if st.sidebar.button("Bagi"):
    st.write("Hasil = " +str(num1/num2))
