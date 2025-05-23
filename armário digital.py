import streamlit as st
import pandas as pd

st.write("# Seu armário digital\nHey, *cutie!*\nVamos escolher o outfit de hoje!") 
st.image("https://github.com/raquelsantos81/ecmi-2025/blob/main/HJL66---Playset-Barbie-com-Boneca---O-Closet-Perfeito-1.webp?raw=true", caption="Barbie Armário")

ocasiao = st.selectbox(
    'Escolha sua ocasião:',
    ['', 'Almoço', 'Passeio de dia', 'Balada', 'Barzinho', 'Cinema', 'Date', 'Brunch', 'Churrasco', 'Academia', 'Museu']
)

if ocasiao:
    st.write(f"Vamos montar um look para: **{ocasiao}**")


