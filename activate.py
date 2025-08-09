import streamlit as st
from validation import *

def activate_account():
    st.header("Activate Account")
    
    with st.form("activate_form"):
        email = st.text_input("Email").strip().lower()

        submit = st.form_submit_button("Activate")
        if submit:
            if not validate_email(email):
                st.error("Invalid email")
                return
            if not validate_email_exists(email):
                st.error("Email does not exist")
                return
            if validate_email_activated(email):
                return
            
            st.success("Activation email sent")
