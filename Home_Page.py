import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64

st.set_page_config(
    page_title="Face Attendance Management System", page_icon="📊", layout="wide"
)


st.header("Face Attendance Management System")
st.info("Welcome to our project")

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.text("")
    st.text("")

with col2:
    st.text("")
    st.text("")
    st.text("")
    st.image("logo.png", use_column_width=True)
    st.text("")
    # st.text("")
    # st.text("")
    # st.text("")
    # st.text("")
    # st.text("")
    # st.text("")
    st.text("")
    st.text("")
    st.text("")
    want_to_contribute = st.button("Explore our project")
    if want_to_contribute:
        switch_page(r"add_new_student")

with col3:
    st.text("")

hide = """
    <style>

        # footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .css-1cypcdb {display: none;}
        }

    </style>
"""
st.markdown(hide, unsafe_allow_html=True)


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# img = get_img_as_base64("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")

bg_img = """
<style>
.egzxvld5{

background-image: url("https://cdn.shopify.com/s/files/1/0048/1086/6803/articles/PCOS_2048x.jpg?v=1604611044");
background-repeat: no-repeat;
background-size: cover;

}


</style>
"""

st.markdown(bg_img, unsafe_allow_html=True)
