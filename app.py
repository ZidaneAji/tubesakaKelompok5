import streamlit as st
import time
import sys

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

        # Iteratif
        start_i = time.time()
        hasil_i = hitung_konsonan_iteratif(kalimat)
        end_i = time.time()

        # Rekursif
        start_r = time.time()
        hasil_r = hitung_konsonan_rekursif(kalimat)
        end_r = time.time()

        st.success("Perhitungan berhasil")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔁 Algoritma Iteratif")
            st.write(f"Jumlah konsonan: **{hasil_i}**")
            st.write(f"Waktu eksekusi: **{end_i - start_i:.8f} detik**")
            st.markdown("**Kompleksitas Waktu:** O(n)")
            st.markdown("**Kompleksitas Ruang:** O(1)")

        with col2:
            st.markdown("### 🔂 Algoritma Rekursif")
            st.write(f"Jumlah konsonan: **{hasil_r}**")
            st.write(f"Waktu eksekusi: **{end_r - start_r:.8f} detik**")
            st.markdown("**Kompleksitas Waktu:** O(n)")
            st.markdown("**Kompleksitas Ruang:** O(n)")

        st.markdown("---")
        st.markdown("### 📌 Analisis Kompleksitas")
        st.write(f"""
Jumlah karakter (n): **{n}**

- Kedua algoritma melakukan pengecekan terhadap setiap karakter → **O(n)**
- Algoritma iteratif lebih efisien memori karena tidak menggunakan stack rekursi
- Algoritma rekursif berisiko **stack overflow** jika input sangat panjang
""")