import streamlit as st
import base64
st.snow()

st.warning('# 야채 15종 CNN')
st.write("""
### 15개의 정해진 야채중 사진을 올려주세요!
""")
filename = st.file_uploader("사진을 올려주세요")
st.markdown("![Alt Text](https://media.giphy.com/media/VJY3zeoK87CLBKnqqm/giphy.gif)")


url = 'https://github.com/baejinhyuk/ai_mid/pages/mnist_mlp_model.h5'
filename = url.split('/')[-1]
trained_model.load_weights(urllib.request.urlretrieve(url, filename))

