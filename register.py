import streamlit as st

def register():
    st.header("Register")
    with st.form("register_form"):
        first_name = st.text_input("First Name").strip()
        last_name = st.text_input("Last Name").strip()
        email = st.text_input("Email").strip()
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        mobile = st.text_input("Mobile")
        submit = st.form_submit_button("Register")
