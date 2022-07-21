import streamlit as st

st.title("GUESS WHAT DOG YOU ARE")

st.write("""
# Put your picture and see what is your nearest breed!
""")
filename = st.file_uploader("Choose a file")
