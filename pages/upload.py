import streamlit as st

st.error(#"야채 15종 CNN")
st.write("""# 15개 야채중 사진을 올려주세요!""")
filename = st.file_uploader("사진올려주세요")
