import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Lectura de datos

df=pd.read_csv("../../../data/final/datos_finales.csv", sep=";")

#Configuración de la página
st.set_page_config(
    page_title="Herramienta de visualización de datos - 13MBID",
    page_icon="📊",
    layout="wide")

#Titulo de la aplicacion
st.title("Herramienta de Visualización de Datos - 13MBID")
st.write("Esta aplicación permite explorar y visualizar los datos del proyecto en curso")

st.write("Desarrollado por: María Caballero Saborido")

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

# Histograma de los importes de créditos otorgados

histograma_importes = px.histogram(df, x='importe_solicitado', nbins=10, title='Importes solicitados en créditos')
histograma_importes.update_layout(xaxis_title='Importe solicitado', yaxis_title='Cantidad')
st.plotly_chart(histograma_importes, use_container_width=True)

#Se agrega un selector para el tipo de creditos y se apliva en los graficos siguientes
tipo_credito=st.selectbox("Selecciona el tipo de crédito",
                          df['objetivo_credito'].unique(),
                          )
st.write("Tipo de credito seleccionado:", tipo_credito)

#Filtrar el DataFrame según el tipo de crédito seleccionado
df_filtrado=df[df['objetivo_credito']==tipo_credito]

# Gráfico de barras apiladas: Comparar la distribución de créditos por estado y objetivo
col1,col2=st.columns(2)
with col1:
    barras_apiladas = px.histogram(df_filtrado, x='objetivo_credito', color='estado_credito_N', 
                               title='Distribución de créditos por estado y objetivo',
                               barmode='stack')
    barras_apiladas.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')
    st.plotly_chart(barras_apiladas, use_container_width=True)
with col2:
    falta_pago_counts = df_filtrado['falta_pago'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=falta_pago_counts.index, values=falta_pago_counts)])
    fig.update_layout(title_text='Distribución de créditos en función de registro de mora')
    st.plotly_chart(fig, use_container_width=True)


# Conteo de ocurrencias por estado
estado_credito_counts = df['estado_credito_N'].value_counts()

# Gráfico de torta de estos valores
fig = go.Figure(data=[go.Pie(labels=estado_credito_counts.index, values=estado_credito_counts)])
fig.update_layout(title_text='Distribución de créditos por estado registrado')
st.plotly_chart(fig, use_container_width=True)

# Definir el orden personalizado
orden_antiguedad = ['menor_2y', '2y_a_4y', 'mayor_4y']

# Ordenar los datos según el orden personalizado
df_ordenado = df.groupby('antiguedad_cliente')['importe_solicitado'].mean().reset_index()
df_ordenado['antiguedad_cliente'] = pd.Categorical(df_ordenado['antiguedad_cliente'], categories=orden_antiguedad, ordered=True)
df_ordenado = df_ordenado.sort_values('antiguedad_cliente')

# Crear el gráfico de líneas
lineas_importes_antiguedad = px.line(df_ordenado, x='antiguedad_cliente', y='importe_solicitado',
                                     title='Evolución de los importes solicitados por antigüedad del cliente')
lineas_importes_antiguedad.update_layout(xaxis_title='Antigüedad del cliente', yaxis_title='Importe solicitado promedio')
st.plotly_chart(lineas_importes_antiguedad, use_container_width=True)




