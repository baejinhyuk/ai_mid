import streamlit as st
import base64
st.warning('# 야채 15종 CNN')
st.write("""
### 15개의 정해진 야채중 사진을 올려주세요!
""")
filename = st.file_uploader("사진을 올려주세요")
st.markdown("![Alt Text](https://media.giphy.com/media/VJY3zeoK87CLBKnqqm/giphy.gif)")


main_bg = "vae.jpg"
main_bg_ext = "jpg"

side_bg = "sample.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
