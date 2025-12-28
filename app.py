import streamlit as st
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(3000)

# =========================
# Fungsi Iteratif
# =========================
def hitung_konsonan_iteratif(kalimat):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jumlah = 0
    for huruf in kalimat:
        if huruf in konsonan:
            jumlah += 1
    return jumlah


# =========================
# Fungsi Rekursif
# =========================
def hitung_konsonan_rekursif(kalimat, index=0):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    if index == len(kalimat):
        return 0

    if kalimat[index] in konsonan:
        return 1 + hitung_konsonan_rekursif(kalimat, index + 1)
    else:
        return hitung_konsonan_rekursif(kalimat, index + 1)


# Tampilan Streamlit
st.title(
    "Analisis Perbandingan Algoritma Iteratif dan Rekursif "
    "dalam Menghitung Huruf Konsonan"
)
st.subheader("Running Time & Kompleksitas Berbasis Input User")

st.write("""
Aplikasi ini membandingkan algoritma **iteratif** dan **rekursif**
dalam menghitung jumlah huruf konsonan, serta menganalisis
**waktu eksekusi dan kompleksitas algoritma berdasarkan input user**.
""")

kalimat = st.text_area("Masukkan kalimat:")

# Proses Utama
if st.button("Hitung & Analisis"):
    if kalimat.strip() == "":
        st.warning("Kalimat tidak boleh kosong.")
    else:
        # Panjang input user
        jumlah_huruf = len(kalimat)

        # Hitung Konsonan + Waktu
        start_i = time.time()
        hasil_i = hitung_konsonan_iteratif(kalimat)
        waktu_i = time.time() - start_i

        start_r = time.time()
        hasil_r = hitung_konsonan_rekursif(kalimat)
        waktu_r = time.time() - start_r

        # Estimasi Jumlah Langkah
        langkah_iteratif = jumlah_huruf
        langkah_rekursif = jumlah_huruf

        # Grafik Running Time perbandingan iteratif dan rekursif
        ukuran_data = [100, 500, 1000, 2000, 3000]
        waktu_iteratif = []
        waktu_rekursif = []

        for n in ukuran_data:
            data_uji = kalimat * (n // max(len(kalimat), 1))

            start = time.time()
            hitung_konsonan_iteratif(data_uji)
            waktu_iteratif.append(time.time() - start)

            start = time.time()
            hitung_konsonan_rekursif(data_uji[:500])
            waktu_rekursif.append(time.time() - start)

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.plot(ukuran_data, waktu_iteratif, marker='o', label='Iteratif')
        ax.plot(ukuran_data, waktu_rekursif, marker='o', label='Rekursif')
        ax.set_title("Perbandingan Running Time")
        ax.set_xlabel("Ukuran Data (n)")
        ax.set_ylabel("Waktu Eksekusi (detik)")
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        st.pyplot(fig)

        # Hasil Perhitungan
        st.markdown("## 📌 Hasil Perhitungan")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔁 Iteratif")
            st.write(f"Jumlah karakter (n): **{jumlah_huruf}**")
            st.write(f"Jumlah konsonan: **{hasil_i}**")
            st.write(f"Waktu eksekusi: **{waktu_i:.8f} detik**")

        with col2:
            st.markdown("### 🔂 Rekursif")
            st.write(f"Jumlah karakter (n): **{jumlah_huruf}**")
            st.write(f"Jumlah konsonan: **{hasil_r}**")
            st.write(f"Waktu eksekusi: **{waktu_r:.8f} detik**")

        # Kompleksitas Algoritma (DINAMIS)
        st.markdown("---")
        st.markdown("## 🧠 Kompleksitas Algoritma (Berdasarkan Input User)")

        st.write(f"""
Kalimat yang dimasukkan user memiliki **{jumlah_huruf} karakter**, sehingga:

### 🔹 Kompleksitas Waktu
- **Iteratif**  
  Melakukan **{langkah_iteratif} kali pengecekan karakter**  
  Kompleksitas waktu: **O(n)** dengan n = {jumlah_huruf}

- **Rekursif**  
  Melakukan **{langkah_rekursif} kali pemanggilan fungsi**  
  Kompleksitas waktu: **O(n)** dengan n = {jumlah_huruf}

### 🔹 Kompleksitas Ruang
- **Iteratif** : **O(1)**  
  Tidak menggunakan memori tambahan selain variabel penghitung

- **Rekursif** : **O(n)**  
  Menggunakan stack memori sebanyak **{jumlah_huruf} pemanggilan fungsi**
""")

        st.success("Analisis selesai ")
