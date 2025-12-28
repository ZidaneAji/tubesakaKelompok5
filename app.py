import streamlit as st
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(3000)

# =========================
# Utility: Ambil huruf saja
# =========================
def ambil_huruf_saja(kalimat):
    # Hanya huruf alfabet (a-z, A-Z)
    return [c for c in kalimat if c.isalpha()]


# =========================
# Fungsi Iteratif
# =========================
def hitung_konsonan_iteratif(data):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jumlah = 0
    for huruf in data:
        if huruf in konsonan:
            jumlah += 1
    return jumlah


# =========================
# Fungsi Rekursif
# =========================
def hitung_konsonan_rekursif(data, index=0):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    if index == len(data):
        return 0

    if data[index] in konsonan:
        return 1 + hitung_konsonan_rekursif(data, index + 1)
    else:
        return hitung_konsonan_rekursif(data, index + 1)


# =========================
# Tampilan Streamlit
# =========================
st.title(
    "Analisis Perbandingan Algoritma Iteratif dan Rekursif "
    "dalam Menghitung Huruf Konsonan"
)
st.subheader("Running Time & Kompleksitas Berbasis Input User")

st.write("""
Aplikasi ini menghitung jumlah huruf konsonan menggunakan algoritma
**iteratif** dan **rekursif**, serta menganalisis **running time dan
kompleksitas algoritma berdasarkan jumlah huruf alfabet saja**.
Spasi, angka, dan simbol tidak dihitung sebagai input algoritma.
""")

kalimat = st.text_area("Masukkan kalimat:")

# =========================
# Proses Utama
# =========================
if st.button("Hitung & Analisis"):
    if kalimat.strip() == "":
        st.warning("Kalimat tidak boleh kosong.")
    else:
        # Ambil hanya huruf
        huruf_valid = ambil_huruf_saja(kalimat)
        jumlah_huruf = len(huruf_valid)

        if jumlah_huruf == 0:
            st.warning("Kalimat tidak mengandung huruf alfabet.")
        else:
            # =========================
            # Hitung Konsonan + Waktu
            # =========================
            start_i = time.time()
            hasil_i = hitung_konsonan_iteratif(huruf_valid)
            waktu_i = time.time() - start_i

            start_r = time.time()
            hasil_r = hitung_konsonan_rekursif(huruf_valid)
            waktu_r = time.time() - start_r

            # Estimasi jumlah langkah (berdasarkan input user)
            langkah_iteratif = jumlah_huruf
            langkah_rekursif = jumlah_huruf

            # =========================
            # Grafik Running Time
            # =========================
            ukuran_data = [100, 500, 1000, 2000, 3000]
            waktu_iteratif = []
            waktu_rekursif = []

            for n in ukuran_data:
                data_uji = huruf_valid * (n // max(len(huruf_valid), 1))

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

            # =========================
            # Hasil Perhitungan
            # =========================
            st.markdown("## 📌 Hasil Perhitungan")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 🔁 Iteratif")
                st.write(f"Jumlah huruf (n): **{jumlah_huruf}**")
                st.write(f"Jumlah konsonan: **{hasil_i}**")
                st.write(f"Waktu eksekusi: **{waktu_i:.8f} detik**")

            with col2:
                st.markdown("### 🔂 Rekursif")
                st.write(f"Jumlah huruf (n): **{jumlah_huruf}**")
                st.write(f"Jumlah konsonan: **{hasil_r}**")
                st.write(f"Waktu eksekusi: **{waktu_r:.8f} detik**")

            # =========================
            # Kompleksitas Algoritma
            # =========================
            st.markdown("---")
            st.markdown("## 🧠 Kompleksitas Algoritma (Berdasarkan Input User)")

            st.write(f"""
Input user mengandung **{jumlah_huruf} huruf alfabet** (n).

### 🔹 Kompleksitas Waktu
- **Iteratif**  
  Melakukan **{langkah_iteratif} kali pengecekan huruf**  
  Kompleksitas waktu: **O(n)** dengan n = {jumlah_huruf}

- **Rekursif**  
  Melakukan **{langkah_rekursif} kali pemanggilan fungsi**  
  Kompleksitas waktu: **O(n)** dengan n = {jumlah_huruf}

### 🔹 Kompleksitas Ruang
- **Iteratif** : **O(1)**  
  Menggunakan variabel tetap

- **Rekursif** : **O(n)**  
  Menggunakan stack pemanggilan fungsi sebanyak **{jumlah_huruf}**
""")

            st.success("Analisis selesai ✅")
