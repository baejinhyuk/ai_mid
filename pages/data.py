import streamlit as st

st.markdown('### 파일가져오기')
code ='''root_dir = "VegetableImages/train"
image_label = os.listdir(root_dir)
image_label '''

st.code(code, language='python')

st.markdown('### 이미지파일가져오고 사이즈조정40,40')
code2 ='''def img_read_resize(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (40, 40))
    return img '''

st.code(code2, language='python')


st.markdown('### 전체이미지파일읽어 list담아주는 함수 ')
code3 ='''def img_folder_read(rt_dir, img_label):
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
len(img_sample), len(labels) '''

st.code(code3, language='python')

st.markdown('### 위에 함수를 사용 정답갓을 train,test리스트에 담아줌')
code4 ='''def imgs_to_array(rt_dir, image_label):
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

st.code(code4, language='python')

st.markdown('### np.arrpy형식으로 만들기')
code5 ='''x_train_img = np.array(x_train)
x_test_img = np.array(x_test)
y_train_img = np.array(y_train)
y_test_img = np.array(y_test)

x_val_img = np.array(x_val)
y_val_img = np.array(y_val)



x_train_img.shape,x_test_img.shape,y_train_img.shape,y_test_img.shape,x_val_img.shape,y_val_img '''

st.code(code5, language='python')

st.markdown('### 정규화하면계산하기좋습니다..')
code6 ='''x_train = x_train_img / 255
x_valid = x_val_img / 255
x_test = x_test_img / 255 '''

st.code(code6, language='python')

st.markdown('### 파일확인')
code7='''x_train.shape,x_valid.shape, x_test.shape '''

st.code(code7, language='python')

st.markdown('### LabelBinarizer 사용 분류를 숫자로 변경합니다.')
code8='''from sklearn.preprocessing import LabelBinarizer

lb= LabelBinarizer()
y_train = lb.fit_transform(y_train_img)
y_valid = lb.transform(y_val_img)

y_train.shape, y_valid.shape '''

st.code(code8, language='python')


st.markdown('### 모델층만들어주기')
code9='''import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import EarlyStopping

model = Sequential()
# 입력층
model.add(Conv2D(filters=8, kernel_size=(3,3),padding= "same", activation='relu', input_shape=(40, 40, 3)))
model.add(MaxPool2D(2,2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=16, kernel_size=(3,3),padding= "same", activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Dropout(0.2))

model.add(Conv2D(filters=32, kernel_size=(3,3),padding= "same", activation='relu'))
model.add(MaxPool2D(2,2))
model.add(Dropout(0.2))

# Fully-connected layer
model.add(Flatten())
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=8, activation='relu'))

# 출력층
model.add(Dense(15, activation='softmax'))
model '''

st.code(code9, language='python')

st.markdown('### 확인')
code10='''model.summary() '''

st.code(code10, language='python')

st.markdown('### 모델 컴파일')
code12='''model.compile(optimizer="adam",
             loss="categorical_crossentropy",
             metrics=["accuracy"])  '''


st.code(code12, language='python')


st.markdown('### EarlyStopping 입력')
code13='''from tensorflow.keras.callbacks import EarlyStopping
earlystop = EarlyStopping(monitor="val_accuracy", patience=5, verbose=1) '''

st.code(code13, language='python')

st.markdown('모델핏돌리기')
code14='''history2= model.fit(x_train,y_train, batch_size=32,
                   epochs=100,validation_data=(x_valid,y_valid), callbacks=[earlystop]) '''

st.code(code14, language='python')

st.markdown('모델 결과값 데이터프레임으로 만들기 ')
code15='''pd.DataFrame(history2.history).tail() '''

st.code(code15, language='python')

code16=''' '''

st.code(code16, language='python')
