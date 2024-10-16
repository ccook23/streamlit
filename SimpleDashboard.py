# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17DdJlMq-1DHmOA7JX4T3wOLvbATv_T3o
"""

import streamlit as st

# Title of the dashboard
st.title("Hello, World! Dashboard")

# User input
name = st.text_input("Enter your name:")

# Display a greeting message
if name:
    st.write(f"Hello, {name}! Welcome to the Streamlit dashboard.")
else:
    st.write("Please enter your name to be greeted!")

# Adding a button to show a message
if st.button("Click me"):
    st.write("You clicked the button!")

# Adding a select box for a simple choice
option = st.selectbox(
    "Choose your favorite programming language:",
    ("Python", "JavaScript", "C++", "Java", "Other")
)

# Display the selected option
st.write(f"You selected: {option}")