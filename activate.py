import streamlit as st
from validation import *
from email_sender import send_email


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
                st.warning("Account already activated")
                return
            
            st.session_state.email_to_activate = email
            st.session_state.activation_code = generate_code()

            if send_email(email, st.session_state.activation_code):
                st.success("Activation email sent")
                st.write("Please check your email for the activation code")
            
    if "activation_code" in st.session_state:
        with st.form("activation_form"):
            user_code = st.text_input("Activation Code")
            submit_code = st.form_submit_button("Submit Code")
            
            if submit_code:
                if st.session_state.activation_code == user_code:
                    st.success("Account activated")
                    for user in st.session_state.users:
                        if user["email"] == st.session_state.email_to_activate:
                            user["active"] = True
                            break
                    del st.session_state.activation_code  # Clear after use
                else:
                    st.error("Invalid activation code")
                