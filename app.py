import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título con efecto neón rojo
st.markdown("""
<h1 style='text-align: center; 
            color: #ff0000; 
            text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000;
            font-family: Arial, sans-serif;
            font-weight: bold;
            margin-bottom: 30px;'>
    Tablero Increíble
</h1>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("Propiedades del Tablero")
    drawing_mode = st.sidebar.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = '#000000'  # Fondo negro para mejor contraste

# Componente de canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=300,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas"
)
