import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Oscilador Forzado", layout="centered")

st.title("Oscilador Forzado")

# Descripción breve
st.write("""
Esta aplicación permite visualizar la amplitud de un oscilador forzado con distintos parámetros:
- ($F_0$): Magnitud de la fuerza externa.
- (m): Masa del oscilador.
- (b): Coeficiente de amortiguamiento.
- ($\omega_0$): Frecuencia natural del oscilador.
- ($\omega$): Frecuencia de excitación.
""")

# Barra lateral para configurar parámetros
st.sidebar.title("Parámetros del sistema")

F0 = st.sidebar.slider("F0 (magnitud de la fuerza)", 0.1, 10.0, 1.0, step=0.1)
m = st.sidebar.slider("m (masa)", 0.1, 10.0, 1.0, step=0.1)
b = st.sidebar.slider("b (amortiguamiento)", 0.0, 5.0, 0.2, step=0.1)
omega0 = st.sidebar.slider("ω₀ (frecuencia natural)", 0.1, 5.0, 1.0, step=0.1)

#st.sidebar.title("Rango de Frecuencias de Excitación (ω)")
omega_min = 0 #st.sidebar.slider("ω mínimo", 0.0, 5.0, 0.0, step=0.1)
omega_max = 3 #st.sidebar.slider("ω máximo", 0.1, 20.0, 3.0, step=0.1)
N = 1000 # st.sidebar.slider("Número de puntos", 100, 5000, 1000, step=100)

# Función de amplitud
def A(omega, F0, m, b, omega0):
    return (F0 / m) / np.sqrt((omega**2 - omega0**2)**2 + ((b * omega) / m)**2)

# Generamos el vector de frecuencias y calculamos la amplitud
omega = np.linspace(omega_min, omega_max, N)
A_values = A(omega, F0, m, b, omega0)

# Graficamos usando matplotlib
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(omega, A_values, label="A(ω)", color='blue')
ax.set_title("Amplitud de un oscilador forzado")
ax.set_xlabel("Frecuencia de excitación (ω)")
ax.set_ylabel("Amplitud A(ω)")
ax.grid(True)
ax.legend()

# Mostramos la figura en la app
st.pyplot(fig)
