import streamlit as st

code ='''root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label '''

st.code(code, language='python')


code2 ='''def img_read_resize(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (40, 40))
    return img '''

st.code(code2, language='python')
