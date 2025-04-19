import streamlit as st

st.set_page_config(page_title="My first Website", page_icon="🌎",layout="centered")
st.title("welcome to my first python website.")

st.sidebar.title("Navigation")
page=st.sidebar.radio("GO to", ["Home","About","Contact"])

if page == "Home":
    st.header("Home page")
    st.write("This is a simple home page built with python and streamlit")
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hello {name}! thank for visiting.")
elif page == "About":
        st.header("About")
        st.write("This website is built entirely using python and streamlit is under 15 minutes.")

elif page == "Contact":
        st.header("Contact us")
        email = st.text_input("your email")
        message = st.text_input("your message.")
        if st.button("submit"):
              st.success("Thanks! We received your message.")
