# Web app to capture a photo using device camera and convert
# the captured image to greyscale

import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # Open camera in browser
    camera_img = st.camera_input(label='Camera', key='image')

if camera_img:
    # Create Pillow image object
    pil_img = Image.open(camera_img)

    # convert to greyscale (L mode for greyscale)
    greyscale = pil_img.convert("L")

    # Render the converted image on web page
    st.image(greyscale)
