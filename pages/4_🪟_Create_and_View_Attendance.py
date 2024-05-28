import streamlit as st
import pandas as pd
from datetime import datetime
import glob

st.set_page_config(
    page_title="Face Attendance Management System", page_icon="📊", layout="wide"
)

st.title(":clipboard: Create and View Attendance")
st.write("###")

with st.expander("Create New Attendance Sheet"):
    name_of_attendance_sheet = st.text_input("Enter Name of Attendance Sheet")
    if st.button("Create New Attendance Sheet"):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        df = pd.DataFrame(columns=['Date', 'Time', 'Name', 'Status'])
        sheet = name_of_attendance_sheet + " " + str(date)
        df.to_csv("data/" + sheet + ".csv", index=False)
        st.success(f"Attendance sheet '{sheet}' created successfully!")

# datetime object containing current date and time
now = datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M:%S")

path = r"data\\Attendance\\"


d_l = glob.glob(path + "*.csv")
for i in range(len(d_l)):
    d_l[i] = d_l[i].split("\\")[-1].split(".")[0]

if d_l:
    sheet = st.selectbox("Select Date", d_l)
    df = pd.read_csv(path+str(sheet)+".csv")
    st.table(df)
else:
    st.write("No attendance sheets found.")
