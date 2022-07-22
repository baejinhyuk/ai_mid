import streamlit as st 
import tensorflow as tf
import base64
import numpy as np
from PIL import Image # Strreamlit works with PIL library very easily for Images
import cv2
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.utils import *
from keras.callbacks import *

from keras.applications.densenet import DenseNet121, preprocess_input
st.snow()

model_path='model/mnist_mlp_model.h5'

st.warning("# 야채 15종 CNN")
upload = st.file_uploader('야채사진을올려주세요')
st.markdown("![Alt Text](https://media.giphy.com/media/VJY3zeoK87CLBKnqqm/giphy.gif)")
if upload is not None:
  file_bytes = np.asarray(bytearray(upload.read()), dtype=np.uint8)
  opencv_image = cv2.imdecode(file_bytes, 1)
  opencv_image = cv2.cvtColor(opencv_image,cv2.COLOR_BGR2RGB) # Color from BGR to RGB
  img = Image.open(upload)
  st.image(img,caption='Uploaded Image',width=300)
  if(st.button('Predict')):
    model = tf.keras.models.load_model(model_path)
    x = cv2.resize(opencv_image,(40,40))
    x = np.expand_dims(x,axis=0)    
    y = model.predict(x)
    ans=np.argmax(y,axis=1)
    if(ans==0):
      st.title('야채네요')
      print(ans)
    elif(ans==1):
      st.title('뭘까요')
      print(ans)
    else:
      st.title('다른야채인거같습니다.')
      print(ans)
