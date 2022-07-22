pip install streamlit

import streamlit as st
import base64
import cv2

import os

import numpy as np

import pickle

import tensorflow as tf

from tensorflow.keras import layers

from tensorflow.keras import models,utils

import pandas as pd

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing.image import load_img,img_to_array

from tensorflow.python.keras import utils
st.snow()

st.warning('# 야채 15종 CNN')
st.write("""
### 15개의 정해진 야채중 사진을 올려주세요!
""")
filename = st.file_uploader("사진을 올려주세요")
st.markdown("![Alt Text](https://media.giphy.com/media/VJY3zeoK87CLBKnqqm/giphy.gif)")






