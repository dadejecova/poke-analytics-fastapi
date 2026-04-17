import streamlit as st
import requests
import plotly.graph_objects as go

# 1. CONFIGURACIÓN Y ESTILO (Para el scroll automático)
st.set_page_config(page_title="Poke-analytics", layout="wide")

# Truco de CSS para que el navegador siempre intente subir al inicio al recargar
st.markdown("""
    <style>
    html { scroll-behavior: smooth; }
    </style>
    <div id="top"></div>
""", unsafe_allow_html=True)

st.title("Poke Dashboard")
st.markdown("Poke Analysis 4 fun.")

# 2. SIDEBAR
st.sidebar.header("Config")
api_url = st.sidebar.text_input("URL de la API", "http://127.0.0.1:8000")

if st.sidebar.button("Verify Connection"):
    try:
        response = requests.get(f"{api_url}/")
        if response.status_code == 200:
            st.sidebar.success("Connected Successfully")
    except:
        st.sidebar.error("Connection failed")

# 3. LÓGICA DE BÚSQUEDA (Simplificada)
# Leemos directamente de la URL. Si no hay nada, es ""
current_poke = st.query_params.get("pokemon", "")

st.header("Search Poke")
# El buscador ahora solo obedece a la URL
poke_name = st.text_input("Search Pokémon:", value=current_poke).lower()

if poke_name:
    try:
        res = requests.get(f"{api_url}/pokemon/{poke_name}")
        if res.status_code == 200:
            poke = res.json()
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(poke["sprite_url"], width='stretch')
                st.subheader(f"#{poke['id']} {poke['name'].capitalize()}")
                st.write(f"**Types:** {poke['type_1']} / {poke['type_2'] or ''}")            
                
            with col2:
                # Metrics
                m1, m2, m3, m4, m5, m6 = st.columns(6)
                m1.metric("HP", poke["hp"])
                m2.metric("Atk", poke["attack"])
                m3.metric("Def", poke["defense"])
                m4.metric("Sp. Atk", poke["special_attack"])
                m5.metric("Sp. Def", poke["special_defense"])
                m6.metric("Speed", poke["speed"])

                # Radar Chart (Simplificado para el ejemplo)
                categories = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
                values = [poke['hp'], poke['attack'], poke['defense'], poke['special_attack'], poke['special_defense'], poke['speed']]
                
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=values + [values[0]],
                    theta=categories + [categories[0]],
                    fill='toself',
                    name=poke['name'].capitalize(),
                    line_color="#FF4B4B",
                    fillcolor="#FF4B4B",
                    opacity=0.6
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 160])),
                    showlegend=False,
                    margin=dict(l=40, r=40, t=40, b=40),
                    paper_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, width='stretch')

                st.subheader("Main Moves")
                ataques = poke['moves'].split(", ")
                st.write(" ".join([f"`{a.capitalize()}`" for a in ataques]))
        else:
            st.warning("Poke not found.")
    except Exception as e:
        st.error(f"Error: {e}")

# 4. LOCAL DEX (Galería)
st.divider()
st.header("Local Dex")

try:
    res_all = requests.get(f"{api_url}/pokemon/all")
    if res_all.status_code == 200:
        all_pokes = res_all.json()
        if all_pokes:
            cols = st.columns(5)
            for idx, p in enumerate(all_pokes):
                with cols[idx % 5]:
                    st.image(p["sprite_url"], width=80)
                    # AL HACER CLIC:
                    if st.button(p['name'].capitalize(), key=f"btn_{p['id']}"):
                        # Actualizamos la URL (Esto es lo que provoca el "salto" al inicio)
                        st.query_params["pokemon"] = p['name']
                        st.rerun()
        else:
            st.info("No pokes found in local dex.")
except Exception as e:
    st.error(f"Gallery Error: {e}")