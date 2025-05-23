import streamlit as st
import pandas as pd

st.write("""
# Seu armário digital 

Hey, *cute*
vamos escolher o outfit de hoje!
""")
st.image("https://github.com/raquelsantos81/ecmi-armario-digital/blob/main/barbie_armario.png?raw=true", caption="Barbie Armário")

ocasiao = st.selectbox(
    'Escolha sua ocasião:',
    ['', 'Almoço', 'Passeio de dia', 'Balada', 'Barzinho']
)

if ocasião:
    st.write(f"Vamos montar um look para: **{ocasião}**")

