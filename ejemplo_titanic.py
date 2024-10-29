import streamlit as st
import pandas as pd

st.title("Universidad San Sebastian")

st.sidebar.title("Barra lateral")
st.sidebar.header("Hola")
st.sidebar.write("Esto es mi barra lateral")

st.image("https://www.uss.cl/wp-content/uploads/2021/03/Isotipo_USS-Color.svg")

if st.sidebar.button("Haz echo cick pero en la barra lateral"):
    st.sidebar.write("Haz echo click en el botón de la barra lateral")

user_input = st.sidebar.text_input("Escribe algo en la barra: ")
st.sidebar.write(f"Has escrito: {user_input}")
