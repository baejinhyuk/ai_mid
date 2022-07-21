import streamlit as st
from text.contents import *
from importlib.resources import path

st.markdown('### file load')
code = '''root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label '''
st.code(code, language='python')
