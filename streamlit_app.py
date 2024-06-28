import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid
import matplotlib.animation as animation
from PIL import Image
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

  #Fungsi untuk mengupdate plot
def update_plot(frame, img, implot):
    implot.set_array(np.rot90(img, frame))
    return [implot]

# Mengunduh gambar dari URL
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/320px-Example.jpg'  # Ganti dengan URL gambar yang diinginkan
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img = np.array(img)

# Membuat figure dan axis
fig, ax = plt.subplots()
implot = ax.imshow(img)

# Membuat animasi
ani = animation.FuncAnimation(fig, update_plot, frames=range(4), fargs=(img, implot), interval=200)



