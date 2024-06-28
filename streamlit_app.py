import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid
import matplotlib.animation as animation
from PIL import Image, UnidentifiedImageError
from io import BytesIO

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
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

if __name__ == '__main__' :
  main()

# Fungsi untuk mengupdate plot
def update_plot(frame, img, implot):
    implot.set_array(np.rot90(img, frame))
    return [implot]

# URL yang ingin Anda gunakan
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/320px-Example.jpg'

try:
    # Headers dengan User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Mengunduh gambar dari URL dengan headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Memeriksa jika respons sukses

    # Membaca gambar menggunakan PIL
    img = Image.open(BytesIO(response.content))
    img = np.array(img)

    # Membuat figure dan axis
    fig, ax = plt.subplots()
    implot = ax.imshow(img)

    # Membuat animasi
    ani = animation.FuncAnimation(fig, update_plot, frames=range(4), fargs=(img, implot), interval=200)

    # Menyimpan animasi sebagai file HTML
    ani.save('animation.html', writer='html')

    # Membaca file HTML dan menampilkannya di Streamlit
    html_file = open('animation.html', 'r').read()
    st.components.v1.html(html_file, height=300, width=300)

except requests.exceptions.RequestException as e:
    st.error(f"Error during request: {e}")

except UnidentifiedImageError as e:
    st.error(f"Error identifying image: {e}")

except Exception as e:
    st.error(f"An error occurred: {e}")

