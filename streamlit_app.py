import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def main() :
  st.write('Minimal Example')
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

if __name__ == '__main__' :
  main()



# Membuat data animasi
x = np.linspace(0, 2 * np.pi, 100)
frames = [go.Frame(data=[go.Scatter(x=x, y=np.sin(x + phase))]) for phase in np.linspace(0, 2 * np.pi, 30)]

# Membuat figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=np.sin(x), mode="lines")],
    layout=go.Layout(
        updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])]),
    frames=frames
)

# Menampilkan animasi di Streamlit
st.plotly_chart(fig)

