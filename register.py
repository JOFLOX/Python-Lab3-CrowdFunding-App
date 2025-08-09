import streamlit as st
from validation import *

def register():
    st.header("Register")
    with st.form("register_form"):
        first_name = st.text_input("First Name",).strip()
        last_name = st.text_input("Last Name").strip()
        email = st.text_input("Email").strip()
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        mobile = st.text_input("Mobile")
        submit = st.form_submit_button("Register")

        if submit:
            if not validate_name(first_name):
                st.error("Invalid first name")
                return
            if password != confirm_password:
                st.error("Passwords do not match")
                return
            if not validate_email(email):
                st.error("Invalid email")
                return
            if validate_email_exists(email):
                st.error("Email already exists")
                return
            if not validate_phone(mobile):
                st.error("Invalid phone number (should be Egyptian)")
                return
            if not validate_password(password):
                st.error("Password must be at least 8 characters")
                return
            
            st.session_state.users.append({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "mobile": mobile,
                "active": False
            })
            st.success("Registered successfully")


    # st.write("first name: " + first_name)
    # st.write("last name: " + last_name)
    # st.write("email: " + email)
    # st.write("password: " + password)
    # st.write("confirm password: " + confirm_password)
    # st.write("mobile: " + mobile)

    # st.write(st.session_state.users)