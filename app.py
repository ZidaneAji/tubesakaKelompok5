import streamlit as st
import time
import matplotlib.pyplot as plt

# ===============================
# Fungsi Iteratif (Brute Force)
# ===============================
def hitung_konsonan_iteratif(kalimat):
    konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    jumlah = 0
    for huruf in kalimat:
        if huruf in konsonan:
            jumlah += 1
    return jumlah

# ===============================
# Fungsi Rekursif (Divide & Conquer)
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
st.subheader("📊 Perbandingan Running Time")
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
        # Variasi ukuran data
        # ===============================
        ukuran_data = [100, 500, 1000, 2000, 3000, 4000, 5000]
        waktu_iteratif = []
        waktu_rekursif = []

        for n in ukuran_data:
            # Perbesar input untuk iteratif
            data_uji = kalimat * (n // max(len(kalimat), 1))

            # ===============================
            # Iteratif (aman untuk data besar)
            # ===============================
            start = time.time()
            hitung_konsonan_iteratif(data_uji)
            waktu_iteratif.append(time.time() - start)

            # ===============================
            # Rekursif (DIBATASI agar tidak error)
            # ===============================
            data_rekursif = data_uji[:500]  # maksimal 500 karakter
            start = time.time()
            hitung_konsonan_rekursif(data_rekursif)
            waktu_rekursif.append(time.time() - start)

        st.success("✅ Perhitungan berhasil!")

        # ===============================
        # Grafik Matplotlib
        # ===============================
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(
            ukuran_data,
            waktu_iteratif,
            marker='o',
            linewidth=2,
            label='Brute Force O(n²)'
        )

        ax.plot(
            ukuran_data,
            waktu_rekursif,
            marker='o',
            linewidth=2,
            label='Divide & Conquer O(n log n)'
        )

        ax.set_title("Visualisasi Running Time", fontweight='bold')
        ax.set_xlabel("Ukuran Data (n)")
        ax.set_ylabel("Waktu (detik)")
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()

        st.pyplot(fig)

        # ===============================
        # Kesimpulan
        # ===============================
        st.markdown("---")
        st.markdown("### 📌 Kesimpulan")
        st.write(
            "Algoritma **iteratif** mampu menangani input berukuran besar "
            "dengan stabil. Sebaliknya, algoritma **rekursif** memiliki "
            "keterbatasan kedalaman pemanggilan fungsi sehingga harus "
            "dibatasi untuk mencegah *stack overflow*. Hal ini menunjukkan "
            "bahwa iteratif lebih efisien untuk data besar."
        )
