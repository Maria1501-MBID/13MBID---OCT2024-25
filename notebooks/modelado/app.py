import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Lectura de datos

df=pd.read_csv("../../../data/final/datos_finales.csv")

#Configuración de la página
st.set_page_config(
    page_title="Herramienta de visualización de datos - 13MBID",
    page_icon="📊"
    layout="wide"
)

#Titulo de la aplicacion
st.title("Herramienta de Visualización de Datos - 13MBID")
st.write("Esta aplicación permite explorar y visualizar los datos del proyecto en curso")

st.wirte("Desarrollado por: María Caballero Saborido")

st.markdown('----')

#Graficos
st.header("Graficos")
st.subheader("Caracterización de los créditos otorgados")

# Cantidad de créditos por objetivo del mismo

creditos_x_objetivo = px.histogram(df, x='objetivo_credito', 
                                   title='Conteo de créditos por objetivo')
creditos_x_objetivo.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')

#Visuaizacion
st.plotly_chart(creditos_x_objetivo, use_container_width=True)

