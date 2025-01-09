import streamlit as st
import pandas as pd
import pickle
import os

file_path = 'hutanrimba.pkl'

# Cek keberadaan file
if os.path.exists(file_path):
    alibi = pickle.load(open(file_path, mode='rb'))
    model_loaded = True
else:
    st.error(f"File model `{file_path}` tidak ditemukan.")
    model_loaded = False

# Judul aplikasi
st.title("Aplikasi Hutan untuk Prediksi Nama Buah")

# Input pengguna
diameter = st.number_input("Diameter", min_value=0.0, step=0.1)
weight = st.number_input("Berat (weight)", min_value=0.0, step=0.1)
red = st.number_input("Nilai Merah (red)", min_value=0.0, step=0.1)
green = st.number_input("Nilai Hijau (green)", min_value=0.0, step=0.1)
blue = st.number_input("Nilai Biru (blue)", min_value=0.0, step=0.1)

# Tombol prediksi
if st.button("Prediksi"):
    if model_loaded:
        try:
            prediction = alibi.predict([[diameter, weight, red, green, blue]])
            st.success(f'Prediksi Nama Buah: {prediction[0]}')
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
    else:
        st.error("Model tidak tersedia. Pastikan file `hutanrimba.pkl` ada di direktori.")
