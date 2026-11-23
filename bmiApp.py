import streamlit as st

st.markdown("# :red[🩺ค่านวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ:")

weight = st.number_input("กรอกน้ำหนักของคุณ (kg) : ", min_value=1.0, value=1.0)
heightcm = st.number_input("กรอกส่วนสูงของคุณ (cm): ", min_value=1.0, value=1.0)

if st.button("คำนวณค่า BMI "):
  heightm = heightcm / 100
  bmi = weight / (heightm** 2)
  
  st.divider(width="20")
  st.header(f"💪ค่า BMI ของคุณคือ: **{bmi:.2f}**")

  if bmi < 18.5:
    st.warning(" คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
  elif 18.5 <= bmi < 23
    st.success(" คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สมส่วน)")
  elif 23 <= bmi <25. theta :
    st.info(" คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
  else:
    st.error(" คุณอยู่ในเกณฑ์อ้วน")

st.divider()
st.write("นาย ภูมิรพี คำตรี เลขที่ 20 ม.4/5")
