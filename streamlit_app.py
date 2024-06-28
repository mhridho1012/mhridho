import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid

# Baca dataframe dari file CSV
house = pd.read_csv('house_clean.csv')

def main() :
  st.write('Minimal Example')
  st.header('Halaman Streamlit Muhammad Hadiyan Ridho')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  st.write('Contoh dataframe')
  st.dataframe(house)

if __name__ == '__main__' :
  main()




