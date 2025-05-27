import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf 
from importlib import import_module
from pages.homePage import homePage

# import homePage


def welcome():
    #Image 
    image = Image.open("D:\\Kuliah SMT 3\\AI\\Deepfake Detector\\assets\\welcome.png")
    st.markdown(
    """
    <style>
    .centered-image {
    display: flex;
    justify-content: center;
    align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

    # Membungkus gambar dalam div yang diatur agar berada di tengah
    st.markdown('<div class="centered-image">', unsafe_allow_html=True)
    st.image(image)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    @font-face {
    font-family: 'Poppins';
    src: url('D:\\Kuliah SMT 3\\AI\\Deepfake Detector\\assets\\fonts\\Poppins-Regular.ttf') format('truetype');
    }
    .custom-text {
    font-family: 'Poppins', sans-serif;
    font-size: 24px;
    color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="Poppins" style="font-size:50px; text-align: center;">Welcome to the Deepfake Detector</p>', unsafe_allow_html=True)

    #Deskripsi
    st.markdown("""
    <p class="Poppins" 
    style="
    font-size: 20px;
    color: black;"
    >In an era where technology advances at lightning speed, deepfakes have emerged as one of the most provocative challenges of our time. These sophisticated digital alterations can create hyper-realistic images and videos, making it increasingly difficult to distinguish between reality and deception.</p>"""
    , unsafe_allow_html=True)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    .stButton > button {
    font-family: "Poppins", sans-serif; /* Font Poppins */
    font-weight: 600; /* Ketebalan font */
    background-color: #263A6E; /* Warna tombol */
    color: white; /* Warna teks */
    font-size: 32px; /* Ukuran font */
    padding: 10px 24px; /* Padding tombol */
    cursor: pointer; /* Efek pointer */
    border: none; /* Menghilangkan border */
    border-radius: 8px; /* Sudut melengkung */
    }

    .stButton > button:hover {
    background-color: #39559F 
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("Continue"):
        homePage()
