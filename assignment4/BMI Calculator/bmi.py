import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="🤒",layout="centered")
st.title("BMI Calculator in Python 🤒")
st.markdown("""
## create body mass index(BMI) calculate and enter **weight and height**.""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("weight (kg): ", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("height (m): ", min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2) ## bmi formula
    st.subheader("BMI: ")
    st.markdown(f"{bmi: .2f}", unsafe_allow_html=True)
    
    if bmi < 18.5:
        st.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normail weight")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obsity 🚨")

else:
    st.info("please enter a valid weight and height.")

