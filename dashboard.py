import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
                #st.image(poke["sprite_url"], width=200)
                st.image(poke["sprite_url"], width='stretch')
                st.subheader(f"#{poke['id']} {poke['name'].capitalize()}")
                st.write(f"**Tipos:** {poke['type_1']} / {poke['type_2'] or ''}")            
                
            with col2:
                # Mostramos las mètcicas en una fila
                m1, m2, m3, m4, m5, m6 = st.columns(6)
                m1.metric("HP", poke["hp"])
                m2.metric("Atk", poke["attack"])
                m3.metric("Def", poke["defense"])
                m4.metric("Sp. Atk", poke["special_attack"])
                m5.metric("Sp. Def", poke["special_defense"])
                m6.metric("Speed", poke["speed"])

                # Colores
                type_colros = {
                    "fire": "#FF4422", "water": "#3399FF", "grass": "#77CC55",
                    "electric": "#FFCC33", "psychic": "#FF5599", "rock": "#BBAA66",
                    "poison": "#AA5599", "ground": "#DDBB55", "normal": "#AAAA99"
                }

                main_color = type_colros.get(poke['type_1'], "FF4B4B")

                # Datos para el grafico
                categories = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
                values = [poke['hp'], poke['attack'], poke['defense'], poke['special_attack'], poke['special_defense'], poke['speed']]
                fig = go.Figure()


                # Area del poke 
                fig.add_trace(go.Scatterpolar(
                    r=values + [values[0]],
                    theta = categories + [categories[0]],
                    fill = 'toself',
                    name=poke['name'].capitalize(),
                    line_color = main_color,
                    fillcolor = main_color,
                    opacity= 0.6
                ))

                # Ajuste del disño
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True, 
                            range=[0,160], 
                            gridcolor="#444", 
                            showticklabels=False
                        ),
                        angularaxis=dict(
                            gridcolor="#444",
                            tickfont=dict(size=12, color="white")
                            )
                    ),
                    showlegend=False,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=40, r=40, t=40, b=40)
                )

                st.plotly_chart(fig, width='stretch')

        else:
            st.warning("Poke no encontrado en la base ni el API.")
    except Exception as e:
        st.error(f"Error de conexión: {e}")

st.divider()