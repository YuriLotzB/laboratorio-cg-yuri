import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira")
bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:4, :] = (0, 0, 0)
bandeira[4:8, :] = (221, 0, 0)
bandeira[8:12, :] = (255, 206, 0)

st.image(ampliar(bandeira))
st.write("Matriz da bandeira:")
st.write(bandeira)
