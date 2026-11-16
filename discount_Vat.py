import streamlit as st

st.title("🛍️ แอปพลิเคชันคำนวณส่วนลดและ VAT")


price = st.number_input("ราคาเต็มของสินค้า (บาท):", min_value=0.0, value=1000.0)
dis_per = st.number_input("เปอร์เซ็นต์ส่วนลด (%):", min_value=0.0, value=20.0)

if st.button("คำนวณ"):

    dis_price = price * (dis_per / 100)
    vat = (price - dis_price) * 0.07
    net_price = (price - dis_price) + vat

    st.header("🧾 สรุปรายการคำนวณ")
    st.write(f"• ราคาสินค้า: **{price:,.2f}** บาท (ส่วนลด **{dis_per}%**)")
    st.write(f"• ส่วนลดที่คำนวณได้: **{dis_price:,.2f}** บาท")
    st.write(f"• ภาษีมูลค่าเพิ่ม 7%: **{vat:,.2f}** บาท")
    st.subheader(f"💵 ราคาสุทธิที่ต้องจ่าย: {net_price:,.2f} บาท")

st.divider()
st.write("นาย ภูมิรพี คำตรี เลขที่ 20 ม.4/5")
