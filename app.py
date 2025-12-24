import streamlit as st
import time
import pandas as pd

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
# Tampilan Streamlit
# ===============================
st.title("📊 Analisis Iteratif vs Rekursif")
st.subheader("Menghitung Jumlah Huruf Konsonan")

st.write(
    "Aplikasi ini membandingkan algoritma **iteratif** dan **rekursif** "
    "dalam menghitung jumlah huruf konsonan pada sebuah kalimat."
)

kalimat = st.text_area("Masukkan kalimat:", "")

if st.button("Hitung Konsonan"):
    if kalimat.strip() == "":
        st.warning("Silakan masukkan kalimat terlebih dahulu.")
    else:
        # Iteratif
        start_iteratif = time.time()
        hasil_iteratif = hitung_konsonan_iteratif(kalimat)
        end_iteratif = time.time()

        # Rekursif
        start_rekursif = time.time()
        hasil_rekursif = hitung_konsonan_rekursif(kalimat)
        end_rekursif = time.time()

        waktu_iteratif = end_iteratif - start_iteratif
        waktu_rekursif = end_rekursif - start_rekursif

        st.success("✅ Perhitungan selesai!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔁 Algoritma Iteratif")
            st.write(f"Jumlah konsonan: **{hasil_iteratif}**")
            st.write(f"Waktu eksekusi: **{waktu_iteratif:.8f} detik**")

        with col2:
            st.markdown("### 🔂 Algoritma Rekursif")
            st.write(f"Jumlah konsonan: **{hasil_rekursif}**")
            st.write(f"Waktu eksekusi: **{waktu_rekursif:.8f} detik**")

        # ===============================
        # Grafik Perbandingan
        # ===============================
        st.markdown("---")
        st.markdown("### 📈 Grafik Perbandingan Waktu Eksekusi")

        data = {
            "Algoritma": ["Iteratif", "Rekursif"],
            "Waktu Eksekusi (detik)": [waktu_iteratif, waktu_rekursif]
        }

        df = pd.DataFrame(data).set_index("Algoritma")
        st.bar_chart(df)

        st.markdown("---")
        st.markdown("### 📌 Kesimpulan Singkat")
        st.write(
            "Berdasarkan grafik, algoritma **iteratif** umumnya memiliki waktu "
            "eksekusi yang lebih cepat dan penggunaan memori lebih efisien. "
            "Sementara itu, algoritma **rekursif** lebih mudah dipahami secara konsep "
            "namun kurang optimal untuk input yang panjang."
        )
