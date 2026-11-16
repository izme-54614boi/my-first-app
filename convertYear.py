import streamlit as st

st.title("โปรแกรมแปลงปี พ.ศ. เป็น ค.ศ.")

year_be = st.number_input("กรุณากรอกปี พ.ศ. ที่ต้องการแปลง:", min_value=0, step=1, value=2567)

if st.button("คำนวณ"):
    year_ce = year_be - 543
    
    st.success(f"ปี พ.ศ. {year_be} ตรงกับปี ค.ศ. {year_ce}")
