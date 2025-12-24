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
st.title("📊 Analisis Algoritma Iteratif & Rekursif")
st.subheader("Perbandingan Running Time & Kompleksitas")

st.write("""
Aplikasi ini membandingkan **algoritma iteratif dan rekursif**
dalam menghitung jumlah huruf konsonan serta menganalisis
**waktu eksekusi dan kompleksitas algoritma**.
""")

kalimat = st.text_area("Masukkan kalimat:")

if st.button("Hitung & Analisis"):
    if kalimat.strip() == "":
        st.warning("Kalimat tidak boleh kosong.")
    else:
        # ===============================
        # Data dasar
        # ===============================
        jumlah_huruf = len(kalimat)

        # ===============================
        # Hitung konsonan & waktu eksekusi
        # ===============================
        start_i = time.time()
        hasil_i = hitung_konsonan_iteratif(kalimat)
        waktu_i = time.time() - start_i

        start_r = time.time()
        hasil_r = hitung_konsonan_rekursif(kalimat)
        waktu_r = time.time() - start_r

        # ===============================
        # Grafik Running Time (2 garis)
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

            # Rekursif (dibatasi)
            start = time.time()
            hitung_konsonan_rekursif(data_uji[:500])
            waktu_rekursif.append(time.time() - start)

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
        # Informasi di BAWAH grafik
        # ===============================
        st.markdown("## 📋 Hasil Perhitungan")

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

        # ===============================
        # Kompleksitas
        # ===============================
        st.markdown("---")
        st.markdown("## 📌 Kompleksitas Algoritma")

        st.write("""
**Kompleksitas Waktu:**
- Iteratif : **O(n)** → mengecek setiap karakter satu kali
- Rekursif : **O(n)** → setiap pemanggilan memproses satu karakter

**Kompleksitas Ruang:**
- Iteratif : **O(1)** → tidak menggunakan memori tambahan
- Rekursif : **O(n)** → menggunakan stack pemanggilan fungsi
""")

        st.success("Analisis selesai ✔️")
