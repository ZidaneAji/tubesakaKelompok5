import streamlit as st
import time

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

        # Hasil
        st.success("✅ Perhitungan selesai!")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔁 Algoritma Iteratif")
            st.write(f"Jumlah konsonan: **{hasil_iteratif}**")
            st.write(f"Waktu eksekusi: **{end_iteratif - start_iteratif:.8f} detik**")

        with col2:
            st.markdown("### 🔂 Algoritma Rekursif")
            st.write(f"Jumlah konsonan: **{hasil_rekursif}**")
            st.write(f"Waktu eksekusi: **{end_rekursif - start_rekursif:.8f} detik**")

        st.markdown("---")
        st.markdown("### 📌 Kesimpulan Singkat")
        st.write(
            "Algoritma iteratif umumnya lebih efisien dalam penggunaan memori, "
            "sedangkan algoritma rekursif lebih mudah dipahami secara konsep "
            "namun berisiko stack overflow untuk input yang sangat panjang."
        )