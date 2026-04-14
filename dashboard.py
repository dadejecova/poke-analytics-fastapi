import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Pag config
st.set_page_config(page_title="Poke-analytics", layout="wide")

st.title("Poke-Analytics Dashboard")
#st.markdown("Bienvenido al sistema de análisis de Pokémon de **Daniel Coello**.")
st.markdown("Sistema de análisis de Pokémon.")

# Sidebar para los controles
st.sidebar.header("Configuración")
api_url = st.sidebar.text_input("URL de la API", "http://127.0.0.1:8000")

# Probar conexión
if st.sidebar.button("verificar conexión"):
    try:
        response = requests.get(f"{api_url}/")
        if response.status_code == 200:
            st.sidebar.success("Conectado con éxito")
    except:
        st.sidebar.error("No se pudo conectar con la API")


# Busqueda
st.header("Consultar el Poke")
poke_name = st.text_input("Escribe el nombre del poke que quieres buscar").lower()

if poke_name:
    try:
        # Toca llamar la api
        res = requests.get(f"{api_url}/pokemon/{poke_name}")
        if res.status_code == 200:
            poke = res.json()

            # Ponemos columnas para que no se vea feo
            col1, col2 = st.columns([1,2])

            with col1:
                st.image(poke["sprite_url"], width=200)
            
            with col2:
                st.subheader(f"Nombre: {poke['name'].capitalize()}")
                st.write(f"**Tipo 1:** {poke['type_1']} | **Tipo 2:** {poke['type_2'] or 'N/A'}")
                st.metric("Puntos de vida (HP)", poke["hp"])
                st.progress(poke["attack"] / 150, text=f"Ataque: {poke['attack']}")
        else:
            st.warning("Poke no encontrado en la base ni el API.")
    except Exception as e:
        st.error(f"Error de conexión: {e}")

st.divider()

# Analitica parte
st.header("Análisis de poder por tipo")
if st.button("Generar gráfico de ataque"):
    try:
        res_analysis = requests.get(f"{api_url}/analytics/atack-by-type")
        if res_analysis.status_code == 200:
            data_dict = res_analysis.json()

            # Se conveirte el json a un dataframe
            df_plot = pd.DataFrame(list(data_dict.items()), columns=['Tipo', 'Ataque Promedio'])

            # Grafico con plotly
            fig = px.bar(df_plot, x='Tipo', y='Ataque Promedio',
                         color='Ataque Promedio', title="Ranking por tipo de Ataque",
                         color_continuous_scale='Reds')

            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error("Error al obtener los datos análiticos")