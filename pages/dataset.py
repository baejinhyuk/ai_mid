import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
import tqdm as tqdm
from glob import glob
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models

st.markdown('### 파일가져오기')
code = '''root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label '''
st.code(code, language='python')



st.markdown('### 이미지 읽고 사이즈 조정')
code1 = '''def img_read_resize(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (40, 40))
    return imgl '''
st.code(code1, language='python')
