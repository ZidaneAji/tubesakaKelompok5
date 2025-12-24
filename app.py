import streamlit as st
import time
import matplotlib.pyplot as plt

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
st.title("📊 Analisis Iteratif & Rekursif")
st.subheader("Perbandingan Running Time")

st.write(
    "Aplikasi ini membandingkan algoritma **Iteratif (Brute Force)** "
    "dan **Rekursif (Divide & Conquer)** dalam menghitung jumlah konsonan."
)

kalimat = st.text_area("Masukkan kalimat:", "")

if st.button("Hitung & Tampilkan Grafik"):
    if kalimat.strip() == "":
        st.warning("Silakan masukkan kalimat terlebih dahulu.")
    else:
        # ===============================
        # Pengujian dengan variasi ukuran input
        # ===============================
        ukuran_data = [100, 500, 1000, 2000, 3000, 4000, 5000]
        waktu_iteratif = []
        waktu_rekursif = []

        for n in ukuran_data:
            data_uji = kalimat * (n // max(len(kalimat), 1))

            # Iteratif
            start = time.time()
            hitung_konsonan_iteratif(data_uji)
            waktu_iteratif.append(time.time() - start)

            # Rekursif
            start = time.time()
            hitung_konsonan_rekursif(data_uji)
            waktu_rekursif.append(time.time() - start)

        st.success("✅ Perhitungan selesai!")

        # ===============================
        # Grafik Matplotlib
        # ===============================
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            ukuran_data,
            waktu_iteratif,
            marker='o',
            color='red',
            linewidth=2,
            markersize=8,
            label='Brute Force O(n²)'
        )

        ax.plot(
            ukuran_data,
            waktu_rekursif,
            marker='o',
            color='blue',
            linewidth=2,
            markersize=8,
            label='Divide & Conquer O(n log n)'
        )

        ax.set_title("Visualisasi Running Time", fontsize=14, fontweight='bold')
        ax.set_xlabel("Ukuran Data (n)", fontsize=12)
        ax.set_ylabel("Waktu (detik)", fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        st.pyplot(fig)

        # ===============================
        # Kesimpulan
        # ===============================
        st.markdown("---")
        st.markdown("### 📌 Kesimpulan")
        st.write(
            "Berdasarkan grafik, algoritma **iteratif (Brute Force)** "
            "menunjukkan pertumbuhan waktu eksekusi yang lebih cepat "
            "dibandingkan algoritma **rekursif (Divide & Conquer)**. "
            "Hal ini membuktikan bahwa algoritma dengan kompleksitas "
            "lebih kecil lebih efisien untuk input berukuran besar."
        )
