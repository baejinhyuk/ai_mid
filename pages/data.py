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
from importlib.resources import path
import streamlit as st
from text.contents import *

code = root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label 
st.code(code, language='python')
