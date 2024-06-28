import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid
# Baca dataframe dari file CSV
titanic = pd.read_csv('https://raw.githubusercontent.com/mofdac/-materi-das/main/01.%20Python%20for%20DA/titanic.csv')

# Read JSON file dari data covid dengan penanganan kesalahan
try:
    response = requests.post('https://forecastpassengerapi.herokuapp.com/forecast_timeseries', json={
        "month_limit": "2020-01-01",
        "window_size": 12
    })
    response.raise_for_status()  # Memeriksa status kode HTTP
    flight_passanger_api = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Error during HTTP request: {e}")
    flight_passanger_api = {}
except ValueError as e:
    st.error(f"Error parsing JSON: {e}")
    flight_passanger_api = {}

def main() :
  st.write('Minimal Example')
  st.header('Halaman Streamlit Muhammad Hadiyan Ridho')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  st.write('Contoh dataframe')
  st.dataframe(titanic)
  st.write('Contoh JSON')
  st.json(flight_passanger_api)
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  st.write('Menampilkan Dataframe dengan St AgGrid')
  AgGrid(titanic)
  st.table([x for x in range(1,5)])

if __name__ == '__main__' :
  main()




