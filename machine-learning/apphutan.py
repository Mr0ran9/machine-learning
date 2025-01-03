import streamlit as st
import pandas as pd
import pickle
import os
import pickle

file_path = 'hutanrimba.pkl'
if os.path.exists(file_path):
    alibi = pickle.load(open(file_path, mode='rb'))
else:
    print(f"File {file_path} tidak ditemukan.")

# Judul aplikasi
st.title("Aplikasi hutan untuk Prediksi Nama Buah")

# Input pengguna
diameter = st.number_input("Diameter", min_value=0.0, step=0.1)
weight = st.number_input("Berat (weight)", min_value=0.0, step=0.1)
red = st.number_input("Nilai Merah (red)", min_value=0.0, step=0.1)
green = st.number_input("Nilai Hijau (green)", min_value=0.0, step=0.1)
blue = st.number_input("Nilai Biru (blue)", min_value=0.0, step=0.1)

# Tombol prediksi
if st.button("Prediksi"):
    prediction = alibi.predict([[diameter, weight, red, green, blue]])
    st.success(f'Prediksi Nama Buah: {prediction[0]}')  # Gunakan f-string untuk menampilkan hasil prediksi
