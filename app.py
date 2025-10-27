# Simulador de Modelos Exponenciales (Decaimiento Radiactivo y Ley de Enfriamiento de Newton)
# Versión: FINAL Y LIMPIA (Funcionalidad 100% Garantizada con Input Manual)
# -------------------------------------------------------------------------------------

import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from typing import Optional, List

# --- Constantes y Parámetros Globales ---
COLOR_PRIMARIO = "#58A6FF"
COLOR_EXITO = "#3FB972"
COLOR_FONDO = "#0D1117"
COLOR_SECUNDARIO = "#161B22"

# ----------------------------------------------------------------
# CONFIGURACIÓN GENERAL Y CSS (Máxima Expansión de Estilo)
# ----------------------------------------------------------------
st.set_page_config(
    page_title="Modelos Exponenciales", 
    page_icon="🌌",
    layout="wide"
)

# Estilos CSS detallados y extensos para asegurar la estética
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
# FUNCIÓN DE CÁLCULO Y GRÁFICA 
# ----------------------------------------------------------------

def plot_model(t_max: float, values: List[float], xlabel: str, ylabel: str, title: str, T_ambiente: Optional[float] = None, T_inicial: Optional[float] = None):
    """Genera y muestra la gráfica del modelo exponencial con estilo avanzado."""
    if t_max <= 0:
        st.error("El tiempo de predicción debe ser mayor que cero para generar la gráfica.")
        return

    tiempo = np.linspace(0, t_max * 1.2, 500) 

    if T_ambiente is not None:
        if len(values) < 3: return
        T0, Ta, k = values[0], values[1], values[2]
        fig_values = T_ambiente + (T0 - T_ambiente) * np.exp(-k * tiempo)
        line_color, point_color = COLOR_EXITO, COLOR_PRIMARIO
    else:
        if len(values) < 2: return
        N0, k = values[0], values[1]
        fig_values = N0 * np.exp(-k * tiempo)
        line_color, point_color = COLOR_PRIMARIO, COLOR_EXITO

    # Configuración de Matplotlib para el tema oscuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=COLOR_FONDO) 
    ax.plot(tiempo, fig_values, color=line_color, linewidth=3.5, label="Función N(t) o T(t)")
    
    final_val_at_t = fig_values[np.abs(tiempo - t_max).argmin()] 
    ax.scatter(t_max, final_val_at_t, color=point_color, zorder=5, s=180, edgecolors='#C9D1D9', linewidths=2.5, label=f"Predicción en $t={t_max}$")
    
    ax.axvline(t_max, color=point_color, linestyle='--', alpha=0.5, linewidth=1)
    ax.axhline(final_val_at_t, color=point_color, linestyle='--', alpha=0.5, linewidth=1)
    
    ax.set_xlabel(xlabel, color="#C9D1D9", fontsize=12)
    ax.set_ylabel(ylabel, color="#C9D1D9", fontsize=12)
    ax.set_title(title, color="#C9D1D9", fontsize=16)
    ax.tick_params(colors="#C9D1D9")
    ax.spines['left'].set_color('#30363D')
    ax.spines['bottom'].set_color('#30363D')
    ax.grid(color="#30363D", linestyle='--', alpha=0.6)
    ax.set_facecolor("#161B22") 
    ax.legend(facecolor="#161B22", edgecolor="#161B22", labelcolor="#C9D1D9", loc='upper right')
    
    st.pyplot(fig)
    plt.close(fig)

# ----------------------------------------------------------------
# CABECERA Y MENÚ PRINCIPAL (Flujo Vertical) - AJUSTADO
# ----------------------------------------------------------------
st.title("Simulador de Modelos Exponenciales")
st.markdown("---")

# --- AJUSTE DE ESPACIO PARA EL SELECTBOX (Centrado) ---
# Usamos columnas para limitar el ancho efectivo y centrar el selectbox
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    menu = st.selectbox("Selecciona el modelo de simulación:", [
        "— Seleccionar Modelo —",
        "Descomposición Radiactiva",
        "Ley de Enfriamiento de Newton"
    ], key="main_menu_select_centered")

st.markdown("---") 

# ----------------------------------------------------------------
# ☢️ DESCOMPOSICIÓN RADIACTIVA (CALCULADORA MANUAL)
# ----------------------------------------------------------------
if menu == "Descomposición Radiactiva":
    st.header("Modelo de Descomposición Radiactiva")
    st.markdown("Calcula la cantidad restante (N(t)) de una sustancia con desintegración exponencial. **Fórmula:** $N(t) = N_0 e^{-k t}$")

    with st.container(border=True): 
        st.subheader("Parámetros del Modelo")
        col1, col2, col3 = st.columns(3)
        N0 = col1.number_input("Cantidad Inicial (N_0):", min_value=0.0, value=800.0, key="N0_manual", help="Masa o unidades al inicio (t=0).")
        k = col2.number_input("Constante de Descomposición (k):", min_value=0.0001, value=0.015, format="%.4f", key="k_manual", help="Tasa de desintegración (k > 0).")
        t = col3.number_input("Tiempo de Predicción (t):", min_value=0.0, value=50.0, key="t_manual", help="Tiempo transcurrido hasta el punto de cálculo.")

        st.markdown("---")
        submitted = st.button("Calcular Descomposición", key="btn_decay")

    if submitted:
        if N0 is None or k is None or t is None or k <= 0:
            st.error("Por favor, ingrese valores válidos y positivos para N₀ y k.")
            st.stop()

        try:
            exp_val = -k * t
            decay_factor = math.exp(exp_val)
            Nf = N0 * decay_factor

            st.markdown(f'<div class="result-card"><h4>Cantidad Remanente N({t:.2f})</h4><div class="result-value">{Nf:.4f} unidades</div></div>', unsafe_allow_html=True)

            st.markdown("### Proceso de Cálculo Detallado")
            st.markdown("#### 1️⃣ Paso 1: Exponente")
            st.latex(f"(-k \\cdot t) = (-({k:.4f}) \\cdot {t:.2f}) = {exp_val:.4f}") # CORRECCIÓN: Usar la variable 'k'
            
            st.markdown("#### 2️⃣ Paso 2: Factor de Decaimiento")
            st.latex(f"e^{{{exp_val:.4f}}} \\approx {decay_factor:.6f}")

            st.markdown("#### 3️⃣ Paso 3: Cálculo Final")
            st.latex(f"N(t) = {N0:.2f} \\cdot {decay_factor:.6f} \\approx {Nf:.4f}")
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, [N0, k], "Tiempo (t)", "Cantidad Remanente N(t)", "Gráfica de la Descomposición Radiactiva")
                
        except Exception as e:
            st.error(f"Error interno en el cálculo: {e}")

# ----------------------------------------------------------------
# 🌡️ LEY DE ENFRIAMIENTO (CALCULADORA MANUAL)
# ----------------------------------------------------------------
elif menu == "Ley de Enfriamiento de Newton":
    st.header("Modelo: Ley de Enfriamiento de Newton")
    st.markdown("Predice la temperatura (T(t)) de un objeto que se enfría en un ambiente constante. **Fórmula:** T(t) = T_a + (T_0 - T_a)e^{-k t}")

    with st.container(border=True): 
        st.subheader("Parámetros del Modelo")
        col1, col2, col3, col4 = st.columns(4)
        Ta = col1.number_input("Temp. Ambiente (T_a):", value=25.0, key="Ta_manual", help="Temperatura constante del entorno (°C).")
        T0 = col2.number_input("Temp. Inicial (T_0):", value=100.0, key="T0_manual", help="Temperatura del objeto al inicio (t=0).")
        k = col3.number_input("Constante de Enfriamiento (k):", min_value=0.0001, value=0.1, format="%.4f", key="k_enf_manual", help="Tasa de intercambio térmico (k > 0).")
        t = col4.number_input("Tiempo de Predicción (t):", min_value=0.0, value=10.0, key="t_enf_manual", help="Tiempo transcurrido (en la unidad de k).")

        st.markdown("---")
        submitted = st.button("Calcular Enfriamiento", key="btn_cool")

    if submitted:
        if Ta is None or T0 is None or k is None or t is None or k <= 0:
            st.error("Por favor, ingrese valores válidos y positivos para k.")
            st.stop()

        try:
            Tdiff = T0 - Ta
            exp_val = -k * t
            decay_factor = math.exp(exp_val)
            Tf = Ta + Tdiff * decay_factor

            st.markdown(f'<div class="result-card"><h4>Temperatura Final T({t:.2f})</h4><div class="result-value">{Tf:.2f} °C</div></div>', unsafe_allow_html=True)

            st.markdown("### Proceso de Cálculo Detallado")
            st.markdown("#### 1️⃣ Paso 1: Diferencia Inicial")
            st.latex(f"\\Delta T_0 = T_0 - T_a = {T0:.2f} - {Ta:.2f} = {Tdiff:.2f} \\; \\text{{°C}}") 

            st.markdown("#### 2️⃣ Paso 2: Exponente")
            # --- LÍNEA CORREGIDA A CONTINUACIÓN ---
            st.latex(f"(-k \\cdot t) = (-({k:.4f}) \\cdot {t:.2f}) = {exp_val:.4f}")
            # --- FIN DE LÍNEA CORREGIDA ---

            st.markdown('3. **Factor de Decaimiento:**')
            st.latex(f"e^{{{exp_val:.4f}}} \\approx {decay_factor:.6f}")
            
            st.markdown('4. **Resultado Final:**')
            st.latex(f"T(t) = {Ta:.2f} + {Tdiff:.2f} \\cdot {decay_factor:.6f} \\approx {Tf:.2f} \\; \\text{{°C}}") 
            
            st.markdown("### Visualización de la Tendencia")
            plot_model(t, [T0, Ta, k], "Tiempo (t)", "Temperatura (°C)", "Gráfica del Enfriamiento de Newton", T_inicial=T0, T_ambiente=Ta)
                
        except Exception as e:
            st.error(f"Error interno en el cálculo: {e}")

# ----------------------------------------------------------------
# MENSAJE INICIAL (Pantalla de Bienvenida)
# ----------------------------------------------------------------
elif menu == "— Seleccionar Modelo —":
    st.info("Utiliza el menú superior para elegir el modelo que deseas simular. Este simulador te ayudará a entender las dinámicas de crecimiento y descomposición exponencial.")