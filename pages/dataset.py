import streamlit as st

st.markdown('### 파일가져오기')
code = '''root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label '''
st.code(code, language='python')



st.markdown('### 이미지읽어오고 사이즈 조정')
code1 = '''def img_read_resize(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (40, 40))
    return imgl '''
st.code(code1, language='python')
