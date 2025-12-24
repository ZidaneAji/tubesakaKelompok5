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
st.subheader("Menghitung Jumlah Huruf Konsonan")

st.write("""
Aplikasi ini membandingkan **algoritma iteratif dan rekursif**
dalam menghitung jumlah huruf konsonan,
serta menampilkan **waktu eksekusi dan kompleksitas algoritma**.
""")

kalimat = st.text_area("Masukkan kalimat:")

if st.button("Hitung"):
    if kalimat.strip() == "":
        st.warning("Kalimat tidak boleh kosong.")
    else:
        n = len(kalimat)

        # ===============================
        # Hitung waktu eksekusi
        # ===============================
        start_i = time.time()
        hasil_i = hitung_konsonan_iteratif(kalimat)
        waktu_i = time.time() - start_i

        start_r = time.time()
        hasil_r = hitung_konsonan_rekursif(kalimat)
        waktu_r = time.time() - start_r

        st.success("Perhitungan berhasil")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔁 Algoritma Iteratif")
            st.write(f"Jumlah konsonan: **{hasil_i}**")
            st.write(f"Waktu eksekusi: **{waktu_i:.8f} detik**")
            st.markdown("**Kompleksitas Waktu:** O(n)")
            st.markdown("**Kompleksitas Ruang:** O(1)")

        with col2:
            st.markdown("### 🔂 Algoritma Rekursif")
            st.write(f"Jumlah konsonan: **{hasil_r}**")
            st.write(f"Waktu eksekusi: **{waktu_r:.8f} detik**")
            st.markdown("**Kompleksitas Waktu:** O(n)")
            st.markdown("**Kompleksitas Ruang:** O(n)")

        # ===============================
        # GRAFIK (seperti contoh sebelumnya)
        # ===============================
        st.markdown("---")
        st.markdown("### 📈 Grafik Perbandingan Waktu Eksekusi")

        algoritma = ["Iteratif", "Rekursif"]
        waktu = [waktu_i, waktu_r]

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.plot(
            algoritma,
            waktu,
            marker='o',
            linewidth=2
        )

        ax.set_title("Visualisasi Running Time", fontweight='bold')
        ax.set_ylabel("Waktu (detik)")
        ax.grid(True, linestyle='--', alpha=0.6)

        st.pyplot(fig)

        # ===============================
        # Analisis Kompleksitas
        # ===============================
        st.markdown("---")
        st.markdown("### 📌 Analisis Kompleksitas")
        st.write(f"""
Jumlah karakter (n): **{n}**

- Kedua algoritma melakukan pengecekan setiap karakter → **O(n)**
- Algoritma iteratif lebih hemat memori karena tidak menggunakan stack
- Algoritma rekursif membutuhkan memori tambahan → **O(n)**
- Untuk input besar, iteratif lebih direkomendasikan
""")
