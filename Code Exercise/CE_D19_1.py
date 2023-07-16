# You need to add a feature to that program that allows users to upload
# an image from their computer files. Then, the app converts the uploaded
# image to grayscale and displays it.

import streamlit as st
from PIL import Image


def convert_to_greyscale(image):
    pil_img = Image.open(image)
    gray_camera_img = pil_img.convert('L')
    st.image(gray_camera_img)


st.subheader("Color to Grayscale Converter")

uploaded_img = st.file_uploader(label='Upload', key='uploaded_img', label_visibility='hidden')

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    convert_to_greyscale(camera_image)
if uploaded_img:
    convert_to_greyscale(uploaded_img)
