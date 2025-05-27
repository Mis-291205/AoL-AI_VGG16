import streamlit as st
from pages.welcome import welcome
from pages.homePage import homePage

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Welcome", "Detect Image"])

# Render pages based on selection
if selection == "Welcome":
    welcome()
elif selection == "Detect Image":
    homePage()
