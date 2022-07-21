import streamlit as st

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

st.markdown('### 파일분류 및 담아주기')
code2 = '''def img_folder_read(rt_dir, img_label):
    img_files = []
    labels = []
    vfiles = glob(f"{rt_dir}/{img_label}/*")
    vfiles = sorted(vfiles)
    
    for v_img in vfiles:
        try:
            img_files.append(img_read_resize(v_img))
            labels.append(img_label)
        except:
            continue
    
    return img_files, labels

img_sample, labels = img_folder_read("VegetableImages/train", "Tomato")


st.markdown('### 위 함수를 사용하여 이미지와 정답값을 train, test, valid에 리스트 담아줍니다.')

st.markdown('### 이미지 읽고 사이즈 조정')
code3 = '''def imgs_to_array(rt_dir, image_label):
    x_img = []
    y_img = []
    for img_label in tqdm.tqdm(image_label):
        # 위에서 만든 img_folder_read 를 통해 
        # 이미지와 정답값을 가져와서 train, test 리스트에 담아줍니다. 
        x_temp, y_temp = img_folder_read(rt_dir, img_label)
        x_img.extend(x_temp)
        y_img.extend(y_temp)
    return x_img, y_img
x_train,y_train=imgs_to_array("VegetableImages/train", image_label)
x_test,y_test=imgs_to_array("VegetableImages/test", image_label)
x_val,y_val=imgs_to_array("VegetableImages/validation", image_label) '''
st.code(code3, language='python')


