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

code5 ='''x_train_img = np.array(x_train)
x_test_img = np.array(x_test)
y_train_img = np.array(y_train)
y_test_img = np.array(y_test)

x_val_img = np.array(x_val)
y_val_img = np.array(y_val)



x_train_img.shape,x_test_img.shape,y_train_img.shape,y_test_img.shape,x_val_img.shape,y_val_img '''

st.code(code5, language='python')

code6 ='''x_train = x_train_img / 255
x_valid = x_val_img / 255
x_test = x_test_img / 255 '''

st.code(code6, language='python')

code7='''x_train.shape,x_valid.shape, x_test.shape '''

st.code(code7, language='python')

code8='''from sklearn.preprocessing import LabelBinarizer

lb= LabelBinarizer()
y_train = lb.fit_transform(y_train_img)
y_valid = lb.transform(y_val_img)

y_train.shape, y_valid.shape '''

st.code(code8, language='python')

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

code10='''model.summary() '''

st.code(code10, language='python')

code11=''' '''

st.code(code11, language='python')


code12='''model.compile(optimizer="adam",
             loss="categorical_crossentropy",
             metrics=["accuracy"])  '''


st.code(code12, language='python')

code13='''from tensorflow.keras.callbacks import EarlyStopping
earlystop = EarlyStopping(monitor="val_accuracy", patience=5, verbose=1) '''

st.code(code13, language='python')

