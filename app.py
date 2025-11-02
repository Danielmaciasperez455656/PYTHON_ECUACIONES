# app.py
# Simulador de Modelos Exponenciales (Enfocado en Ley de Enfriamiento de Newton)
# -------------------------------------------------------------------------------------

import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import sys # Importar sys para st.stop() o manejo de errores si es necesario

# --- IMPORTACIÓN CLAVE ---
# Importamos las funciones de cálculo desde tu otro archivo
try:
    from Ley_Enfriamiento import (
        calcular_temperatura_final,
        calcular_temperatura_inicial,
        calcular_temperatura_ambiente,
        calcular_tiempo,
        calcular_constante_k
    )
except ImportError:
    st.error("Error Crítico: No se pudo encontrar el archivo 'Ley_Enfriamiento.py'. Asegúrate de que esté en la misma carpeta que 'app.py'.")
    st.stop()


# --- Constantes y Parámetros Globales ---
COLOR_PRIMARIO = "#58A6FF"
COLOR_EXITO = "#3FB972"
COLOR_FONDO = "#0D1117"
COLOR_SECUNDARIO = "#161B22"

# ----------------------------------------------------------------
# CONFIGURACIÓN GENERAL Y CSS (Se mantiene tu estilo)
# ----------------------------------------------------------------
st.set_page_config(
    page_title="Ley de Enfriamiento", 
    page_icon="🌡️",
    layout="wide"
)

# Estilos CSS (Se mantienen tus estilos exactos)
st.markdown(f"""
    <style>
    /* 1. Estilos Base y App Container */
    .stApp {{ 
        background-color: {COLOR_FONDO}; 
        color: #C9D1D9; 
        font-family: 'Segoe UI', 'Roboto', sans-serif; 
        min-height: 100vh;
    }}
    
    /* 2. Estilos de Títulos y Headers */
    h1 {{ 
        color: {COLOR_PRIMARIO}; 
        font-weight: 900; 
        text-align: center; 
        padding-top: 1.5rem;
        padding-bottom: 0.8rem; 
        margin-bottom: 2.0rem;
        border-bottom: 3px double {COLOR_PRIMARIO}50; 
    }}
    h2, h3, h4 {{ 
        color: #C9D1D9; 
        font-weight: 600;
        margin-top: 1.8rem;
        padding-left: 0.5rem;
        padding-bottom: 0.4rem;
        border-left: 5px solid {COLOR_EXITO}; 
        border-bottom: 1px solid {COLOR_SECUNDARIO};
    }}
    .block-container {{ padding-top: 2rem; padding-bottom: 3rem; }}
    
    /* 3. Estilos de la Tarjeta de Resultado Final */
    .result-card {{
        background-color: #21262D; 
        padding: 2.0rem;
        border-radius: 12px;
        border: 3px solid {COLOR_EXITO}; 
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
        text-align: center;
        transform: scale(1.02); 
    }}
    .result-card h4 {{
        color: {COLOR_EXITO};
        border-bottom: none;
        margin-top: 0;
        padding-bottom: 0.5rem;
        font-size: 1.3rem;
    }}
    .result-value {{
        font-size: 3.0rem; 
        font-weight: 900;
        color: {COLOR_EXITO}; 
        text-shadow: 0 0 10px rgba(63, 185, 114, 0.5); 
        letter-spacing: 1px;
    }}
    
    /* 4. Estilos para Botones */
    .stButton>button {{
        background-color: {COLOR_PRIMARIO}; 
        color: {COLOR_FONDO}; 
        border: none;
        border-radius: 10px;
        padding: 0.9rem 1.8rem;
        font-size: 1.1rem;
        font-weight: 800;
        transition: 0.3s ease;
        box-shadow: 0 4px 15px rgba(88, 166, 255, 0.4);
    }}
    .stButton>button:hover {{
        background-color: #79C0FF; 
        box-shadow: 0 8px 25px rgba(88, 166, 255, 0.6);
        transform: translateY(-3px);
    }}

    /* 5. Estilos para inputs */
    .stNumberInput input {{
        background-color: #161B22;
        border: 1px solid #30363D;
        color: #C9D1D9;
        border-radius: 6px;
        padding: 0.5rem;
    }}
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------
# FUNCIÓN DE CÁLCULO Y GRÁFICA (Simplificada para Newton)
# ----------------------------------------------------------------

def plot_model(t_highlight: float, Tf_highlight: float, Ta: float, T0: float, k: float, xlabel: str, ylabel: str, title: str):
    """
    Genera la gráfica del modelo de Newton.
    Destaca el punto (t_highlight, Tf_highlight) que fue calculado o usado como dato.
    """
    if k <= 0 or T0 == Ta:
        st.warning("La gráfica no se puede generar con k=0 o T0=Ta.")
        return

    # Asegura que el tiempo de ploteo sea suficiente para ver el punto destacado
    t_max_plot = t_highlight * 1.5 + 1.0 # Añade un 50% extra + 1 para margen
    tiempo = np.linspace(0, t_max_plot, 500) 

    # Calcula la curva completa
    fig_values = Ta + (T0 - Ta) * np.exp(-k * tiempo)
    line_color, point_color = COLOR_EXITO, COLOR_PRIMARIO

    # Configuración de Matplotlib para el tema oscuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=COLOR_FONDO) 
    ax.plot(tiempo, fig_values, color=line_color, linewidth=3.5, label=f"Función T(t) (k={k:.4f})")
    
    # Destaca el punto de interés (calculado o dato)
    ax.scatter(t_highlight, Tf_highlight, color=point_color, zorder=5, s=180, edgecolors='#C9D1D9', linewidths=2.5, label=f"Punto de Interés (t={t_highlight:.2f}, T={Tf_highlight:.2f})")
    
    ax.axvline(t_highlight, color=point_color, linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(Tf_highlight, color=point_color, linestyle='--', alpha=0.5, linewidth=1)
    
    # Línea de la Temperatura Ambiente
    ax.axhline(Ta, color="#C9D1D9", linestyle=':', alpha=0.7, linewidth=2, label=f"Temp. Ambiente (Ta={Ta:.2f})")

    ax.set_xlabel(xlabel, color="#C9D1D9", fontsize=12)
    ax.set_ylabel(ylabel, color="#C9D1D9", fontsize=12)
    ax.set_title(title, color="#C9D1D9", fontsize=16)
    ax.tick_params(colors="#C9D1D9")
    ax.spines['left'].set_color('#30363D')
    ax.spines['bottom'].set_color('#30363D')
    ax.grid(color="#30363D", linestyle='--', alpha=0.6)
    ax.set_facecolor("#161B22") 
    ax.legend(facecolor="#161B22", edgecolor="#161B22", labelcolor="#C9D1D9", loc='best')
    
    st.pyplot(fig)
    plt.close(fig)

# ----------------------------------------------------------------
# CABECERA Y MENÚ PRINCIPAL (Flujo Vertical) - MODIFICADO
# ----------------------------------------------------------------
st.title("🌡️ Calculadora: Ley de Enfriamiento de Newton")
st.markdown("---")

# --- NUEVO MENÚ SELECTBOX ---
# Usamos columnas para limitar el ancho efectivo y centrar el selectbox
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    variable_a_calcular = st.selectbox(
        "**¿Qué variable deseas hallar?**", 
        [
            "— Seleccionar Variable —",
            "Temperatura Final (T(t))",
            "Temperatura Inicial (T0)",
            "Temperatura Ambiente (Ta)",
            "Constante de Enfriamiento (k)",
            "Tiempo (t)"
        ], 
        key="main_menu_select_centered"
    )

st.markdown("---") 

# Contenedor para los inputs
inputs_container = st.container(border=True)


# ----------------------------------------------------------------
# LÓGICA DE CÁLCULO CONDICIONAL (El nuevo núcleo de la app)
# ----------------------------------------------------------------

# CASO 1: CALCULAR TEMPERATURA FINAL (T(t))
if variable_a_calcular == "Temperatura Final (T(t))":
    with inputs_container:
        st.subheader("Parámetros para hallar: T(t)")
        st.markdown("Fórmula: $T(t) = T_a + (T_0 - T_a)e^{-k t}$")
        col1, col2, col3, col4 = st.columns(4)
        Ta = col1.number_input("Temp. Ambiente (T_a):", value=25.0, key="Ta_in")
        T0 = col2.number_input("Temp. Inicial (T_0):", value=100.0, key="T0_in")
        k = col3.number_input("Constante (k):", min_value=0.0001, value=0.1, format="%.4f", key="k_in")
        t = col4.number_input("Tiempo (t):", min_value=0.0, value=10.0, key="t_in")
        
        st.markdown("---")
        submitted = st.button("Calcular Temperatura Final", key="btn_calc_tf")

    if submitted:
        try:
            # Llama a la función importada
            Tf_calculada = calcular_temperatura_final(Ta, T0, k, t)
            
            # Muestra la tarjeta de resultado
            st.markdown(f'<div class="result-card"><h4>Temperatura Final T({t:.2f})</h4><div class="result-value">{Tf_calculada:.4f} °C</div></div>', unsafe_allow_html=True)
            
            # Muestra la gráfica
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, Tf_calculada, Ta, T0, k, "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento")

        except (ValueError, ZeroDivisionError) as e:
            st.error(f"❌ Error en el cálculo: {e}")

# CASO 2: CALCULAR TEMPERATURA INICIAL (T0)
elif variable_a_calcular == "Temperatura Inicial (T0)":
    with inputs_container:
        st.subheader("Parámetros para hallar: T_0")
        st.markdown("Fórmula: $T_0 = T_a + (T(t) - T_a)e^{k t}$")
        col1, col2, col3, col4 = st.columns(4)
        Ta = col1.number_input("Temp. Ambiente (T_a):", value=25.0, key="Ta_in")
        Tf = col2.number_input("Temp. Final (T(t)):", value=50.0, key="Tf_in")
        k = col3.number_input("Constante (k):", min_value=0.0001, value=0.1, format="%.4f", key="k_in")
        t = col4.number_input("Tiempo (t):", min_value=0.0, value=10.0, key="t_in")

        st.markdown("---")
        submitted = st.button("Calcular Temperatura Inicial", key="btn_calc_t0")

    if submitted:
        try:
            # Llama a la función importada
            T0_calculada = calcular_temperatura_inicial(Ta, Tf, k, t)
            
            st.markdown(f'<div class="result-card"><h4>Temperatura Inicial T_0</h4><div class="result-value">{T0_calculada:.4f} °C</div></div>', unsafe_allow_html=True)
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, Tf, Ta, T0_calculada, k, "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento (T0 Calculado)")

        except (ValueError, ZeroDivisionError) as e:
            st.error(f"❌ Error en el cálculo: {e}")

# CASO 3: CALCULAR TEMPERATURA AMBIENTE (Ta)
elif variable_a_calcular == "Temperatura Ambiente (Ta)":
    with inputs_container:
        st.subheader("Parámetros para hallar: T_a")
        st.markdown("Fórmula: $T_a = (T(t) - T_0 e^{-k t}) / (1 - e^{-k t})$")
        col1, col2, col3, col4 = st.columns(4)
        Tf = col1.number_input("Temp. Final (T(t)):", value=50.0, key="Tf_in")
        T0 = col2.number_input("Temp. Inicial (T_0):", value=100.0, key="T0_in")
        k = col3.number_input("Constante (k):", min_value=0.0001, value=0.1, format="%.4f", key="k_in")
        t = col4.number_input("Tiempo (t):", min_value=0.0, value=10.0, key="t_in")
        
        st.markdown("---")
        submitted = st.button("Calcular Temperatura Ambiente", key="btn_calc_ta")

    if submitted:
        try:
            # Llama a la función importada
            Ta_calculada = calcular_temperatura_ambiente(Tf, T0, k, t)
            
            st.markdown(f'<div class="result-card"><h4>Temperatura Ambiente T_a</h4><div class="result-value">{Ta_calculada:.4f} °C</div></div>', unsafe_allow_html=True)
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, Tf, Ta_calculada, T0, k, "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento (Ta Calculada)")

        except (ValueError, ZeroDivisionError) as e:
            st.error(f"❌ Error en el cálculo: {e}")

# CASO 4: CALCULAR CONSTANTE DE ENFRIAMIENTO (k)
elif variable_a_calcular == "Constante de Enfriamiento (k)":
    with inputs_container:
        st.subheader("Parámetros para hallar: k")
        st.markdown("Fórmula: $k = (-1/t) \cdot \ln((T(t) - T_a) / (T_0 - T_a))$")
        col1, col2, col3, col4 = st.columns(4)
        Ta = col1.number_input("Temp. Ambiente (T_a):", value=25.0, key="Ta_in")
        T0 = col2.number_input("Temp. Inicial (T_0):", value=100.0, key="T0_in")
        Tf = col3.number_input("Temp. Final (T(t)):", value=50.0, key="Tf_in")
        t = col4.number_input("Tiempo (t):", min_value=0.0001, value=10.0, key="t_in")
        
        st.markdown("---")
        submitted = st.button("Calcular Constante (k)", key="btn_calc_k")

    if submitted:
        try:
            # Llama a la función importada
            k_calculada = calcular_constante_k(Ta, T0, Tf, t)
            
            st.markdown(f'<div class="result-card"><h4>Constante de Enfriamiento (k)</h4><div class="result-value">{k_calculada:.6f}</div></div>', unsafe_allow_html=True)
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, Tf, Ta, T0, k_calculada, "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento (k Calculada)")

        except (ValueError, ZeroDivisionError) as e:
            st.error(f"❌ Error en el cálculo: {e}")

# CASO 5: CALCULAR TIEMPO (t)
elif variable_a_calcular == "Tiempo (t)":
    with inputs_container:
        st.subheader("Parámetros para hallar: t")
        st.markdown("Fórmula: $t = (-1/k) \cdot \ln((T(t) - T_a) / (T_0 - T_a))$")
        col1, col2, col3, col4 = st.columns(4)
        Ta = col1.number_input("Temp. Ambiente (T_a):", value=25.0, key="Ta_in")
        T0 = col2.number_input("Temp. Inicial (T_0):", value=100.0, key="T0_in")
        Tf = col3.number_input("Temp. Final (T(t)):", value=50.0, key="Tf_in")
        k = col4.number_input("Constante (k):", min_value=0.0001, value=0.1, format="%.4f", key="k_in")
        
        st.markdown("---")
        submitted = st.button("Calcular Tiempo (t)", key="btn_calc_t")

    if submitted:
        try:
            # Llama a la función importada
            t_calculado = calcular_tiempo(Ta, T0, Tf, k)
            
            st.markdown(f'<div class="result-card"><h4>Tiempo Transcurrido (t)</h4><div class="result-value">{t_calculado:.4f}</div></div>', unsafe_allow_html=True)
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t_calculado, Tf, Ta, T0, k, "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento (t Calculado)")

        except (ValueError, ZeroDivisionError) as e:
            st.error(f"❌ Error en el cálculo: {e}")

# ----------------------------------------------------------------
# MENSAJE INICIAL (Pantalla de Bienvenida)
# ----------------------------------------------------------------
elif variable_a_calcular == "— Seleccionar Variable —":
    st.info("Utiliza el menú superior para elegir la variable que deseas calcular. La aplicación te pedirá solo los datos necesarios.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Newtons_law_of_cooling.svg/600px-Newtons_law_of_cooling.svg.png",
             caption="Gráfica de la Ley de Enfriamiento de Newton. La temperatura del objeto (T) se acerca asintóticamente a la temperatura ambiente (Ta).",
             use_column_width=True)