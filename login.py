import streamlit as st
from validation import *

def login():
    st.header("Login")
    with st.form("login_form"):
        email = st.text_input("Email").strip().lower()
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            if not validate_email(email):
                st.error("Invalid email")
                return
            if not validate_email_exists(email):
                st.error("Email does not exist")
                return
            if not validate_email_activated(email):
                st.error("Account not activated")
                return
            if not validate_password(password):
                st.error("Invalid password")
                return
            if not validate_password_match(password, email):
                st.error("Passwords do not match")
                return
            
            st.session_state.current_user = current_user_info(email)
            st.session_state.page = "dashboard"
            st.rerun()
            