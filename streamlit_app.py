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
  
  # Judul aplikasi
  st.title('Logistic Regression Model')

  # Function to display model intercept and coefficients
  def display_model_params(model):
    st.subheader('Model Intercept:')
    st.write(model.intercept_)

    st.subheader('Model Coefficients:')
    coef_data = {'Feature': X.columns, 'Coefficient': model.coef_}
    coef_df = pd.DataFrame(coef_data)
    st.write(coef_df)


  # Displaying model parameters using Streamlit
  st.title('Linear Regression Model Parameters')
  display_model_params(model_lr)

if __name__ == '__main__' :
  main()

