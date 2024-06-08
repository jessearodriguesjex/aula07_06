import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
page_title="Empresa 1",
)

st.header("Dados da Empresa 1")

arquivo = "https://raw.githubusercontent.com/jessearodriguesjex/aula07_06/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe)

fig, ax = plt.subplots()
dfe.plot()
st.pyplot(fig)
#para figuras tem que incluir na primeira linha: fig, ax = plt.subplots() e na ultima linha: st.pyplot(fig)

fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional')
st.pyplot(fig)

fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")
st.write(dfe.groupby('Ano').mean())

#Aqui só incluir st.write na frente
