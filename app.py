import streamlit as st
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(3000)

# ===============================
# Fungsi Iteratif
# ===============================
def hitung_konsonan_iteratif(kalimat):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jumlah = 0
    for huruf in kalimat:
        if huruf in konsonan:
            jumlah += 1
    return jumlah

# ===============================
# Fungsi Rekursif
# ===============================
def hitung_konsonan_rekursif(kalimat, index=0):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    if index == len(kalimat):
        return 0

    if kalimat[index] in konsonan:
        return 1 + hitung_konsonan_rekursif(kalimat, index + 1)
    else:
        return hitung_konsonan_rekursif(kalimat, index + 1)

# ===============================
# UI STREAMLIT
# ===============================
st.title("📊 Analisis Algoritma Iteratif vs Rekursif")
st.subheader("Perbandingan Running Time")

st.write("""
Aplikasi ini membandingkan **algoritma iteratif dan rekursif**
dalam menghitung jumlah huruf konsonan,
serta menampilkan **grafik perbandingan running time**.
""")

kalimat = st.text_area("Masukkan kalimat:")

if st.button("Hitung & Tampilkan Grafik"):
    if kalimat.strip() == "":
        st.warning("Kalimat tidak boleh kosong.")
    else:
        # ===============================
        # Variasi ukuran input
        # ===============================
        ukuran_data = [100, 500, 1000, 2000, 3000]
        waktu_iteratif = []
        waktu_rekursif = []

        for n in ukuran_data:
            data_uji = kalimat * (n // max(len(kalimat), 1))

            # Iteratif
            start = time.time()
            hitung_konsonan_iteratif(data_uji)
            waktu_iteratif.append(time.time() - start)

            # Rekursif (dibatasi agar aman)
            data_rekursif = data_uji[:500]
            start = time.time()
            hitung_konsonan_rekursif(data_rekursif)
            waktu_rekursif.append(time.time() - start)

        st.success("Perhitungan berhasil!")

        # ===============================
        # Grafik 2 Garis
        # ===============================
        fig, ax = plt.subplots(figsize=(9, 5))

        ax.plot(
            ukuran_data,
            waktu_iteratif,
            marker='o',
            linewidth=2,
            label='Iteratif'
        )

        ax.plot(
            ukuran_data,
            waktu_rekursif,
            marker='o',
            linewidth=2,
            label='Rekursif'
        )

        ax.set_title("Perbandingan Running Time", fontweight='bold')
        ax.set_xlabel("Ukuran Data (n)")
        ax.set_ylabel("Waktu Eksekusi (detik)")
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        st.pyplot(fig)

        # ===============================
        # Analisis
        # ===============================
        st.markdown("---")
        st.markdown("### 📌 Analisis")
        st.write("""
- Kedua algoritma memiliki kompleksitas waktu **O(n)**
- Algoritma iteratif lebih stabil untuk data besar
- Algoritma rekursif dibatasi untuk mencegah *stack overflow*
- Grafik menunjukkan iteratif lebih konsisten untuk input besar
""")
