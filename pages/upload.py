import streamlit as st

st.title("사진 올려주세요~!")
st.write("""
# Put your picture and see what is your nearest breed!
""")
filename = st.file_uploader("Choose a file")
