import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid

# Baca dataframe dari file CSV
house = pd.read_csv('house_clean.csv')

def main() :
  # Judul aplikasi
  st.title('Logistic Regression Model')

  # Deskripsi atau instruksi
  st.write('Masukkan nilai-nilai untuk melakukan prediksi menggunakan model Logistic Regression.')

  # Contoh input untuk fitur-fitur yang ingin diprediksi
  feature1 = st.number_input('Masukkan nilai fitur 1')
  feature2 = st.number_input('Masukkan nilai fitur 2')

if __name__ == '__main__' :
  main()

