import streamlit as st
import cv2
import numpy as np
import face_recognition
import pandas as pd

st.set_page_config(
    page_title="Attendance System", page_icon="📊", layout="wide"
)
st.title(":selfie: Add New Student")
st.write("---")
filled = True
with st.container():
    c1, c2 = st.columns((1, 2))
    with c1:
        name = st.text_input("Enter Student name")
        if name == "":
            filled = False

    upload_option = st.radio(
        "Choose the method to add the student's photo",
        ('Camera', 'Upload from storage')
    )

    if upload_option == 'Camera':
        img_file_buffer = st.camera_input("Take a picture for new Student", key="camera")
    else:
        img_file_buffer = st.file_uploader("Upload a picture for new Student", type=["jpg", "jpeg", "png"])

    if img_file_buffer is not None:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        st.write("Number of Faces Detected: ", len(faces))
        if len(faces) > 1:
            st.write("There is more than one face in the image, please take another image.")
        elif len(faces) < 1:
            st.write("No face detected")
        else:
            st.write("Image Taken, Please Click Save")

    with c1:
        if st.button("Save Student"):
            if filled:
                path = "images\\" + name + ".jpg"
                height, width = cv2_img.shape[:2]
                cv2_resized_img = cv2.resize(cv2_img, (int(width / 2), int(height / 2)))

                cv2.imwrite(path, cv2_resized_img)
                img = face_recognition.load_image_file(path)
                img_encodings = face_recognition.face_encodings(img)

                if img_encodings:
                    img_encoding = img_encodings[0]
                    df = pd.read_csv("data\\encodings.csv")
                    en = df["Encodings"].tolist()
                    n = df["Persons"].tolist()
                    en.append(img_encoding)
                    n.append(name)
                    df = pd.DataFrame({"Persons": n, "Encodings": en})
                    df.to_csv("data\\encodings.csv", index=False)
                    st.write("Student Added")
                else:
                    st.write("No face encodings found in the image.")
            else:
                st.warning("Please Enter Student Name")
