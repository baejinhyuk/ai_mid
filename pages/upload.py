import streamlit as st

st.warning('# 야채 15종 CNN')
st.write("""
### 15개의 정해진 야채중 사진을 올려주세요!
""")
filename = st.file_uploader("사진을 올려주세요")
