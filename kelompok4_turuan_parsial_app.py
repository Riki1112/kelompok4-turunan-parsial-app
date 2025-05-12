import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Analisis Biaya dengan Turunan Parsial")
st.write("""
Aplikasi ini menghitung turunan parsial dari fungsi biaya produksi terhadap jumlah produk A dan B.
""")

# Input fungsi biaya dari user
fungsi_input = st.text_input("Masukkan fungsi biaya C(x, y):", "5*x**2 + 3*x*y + 4*y**2 + 10*x + 8*y + 100")

# Input titik evaluasi
x0 = st.number_input("Masukkan jumlah produk A (x₀):", value=1.0)
y0 = st.number_input("Masukkan jumlah produk B (y₀):", value=1.0)

# Variabel simbolik
x, y = sp.symbols('x y')

# Evaluasi fungsi
try:
    C = eval(fungsi_input)
    
    # Turunan parsial
    dC_dx = sp.diff(C, x)
    dC_dy = sp.diff(C, y)

    # Evaluasi turunan di titik (x₀, y₀)
    dC_dx_val = dC_dx.evalf(subs={x: x0, y: y0})
    dC_dy_val = dC_dy.evalf(subs={x: x0, y: y0})

    # Tampilkan hasil
    st.subheader("Hasil Turunan Parsial:")
    st.write(f"∂C/∂x = {dC_dx} ⇒ Nilai di (x₀, y₀) = {dC_dx_val}")
    st.write(f"∂C/∂y = {dC_dy} ⇒ Nilai di (x₀, y₀) = {dC_dy_val}")

    st.subheader("Interpretasi:")
    st.write(f"""
    - Ketika memproduksi {x0} unit produk A dan {y0} unit produk B:
    - Biaya tambahan jika menambah 1 unit produk A (∂C/∂x) sekitar {dC_dx_val:.2f} juta rupiah.
    - Biaya tambahan jika menambah 1 unit produk B (∂C/∂y) sekitar {dC_dy_val:.2f} juta rupiah.
    """)

    # Visualisasi 3D fungsi biaya
    st.subheader("Visualisasi Fungsi Biaya:")
    x_vals = np.linspace(x0-5, x0+5, 50)
    y_vals = np.linspace(y0-5, y0+5, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = eval(fungsi_input.replace('x', 'X').replace('y', 'Y'))

    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('Produk A (x)')
    ax.set_ylabel('Produk B (y)')
    ax.set_zlabel('Biaya C(x, y)')
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan dalam evaluasi fungsi: {e}")
