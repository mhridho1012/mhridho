import streamlit as st
import pandas as pd
import requests
from st_aggrid import AgGrid
import matplotlib.animation as animation
from PIL import Image

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

# Membaca gambar
img = Image.open('your_image.png')  # Ganti dengan path ke gambar Anda
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




