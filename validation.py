import re
import streamlit as st

def validate_name(name: str) -> bool:
    return bool(re.match(r"^[a-zA-Z\s]+$", name))

def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)) # the re.match could return none so we wrap it with bool to return true or false

def validate_email_exists(email: str) -> bool:
    for user in st.session_state.users:
        if user["email"] == email:
            return True
    return False

def validate_email_activated(email: str) -> bool:
    for user in st.session_state.users:
        if user["email"] == email:
            if user["active"] == True:
                st.warning("Account already activated")
                return True
            return False
    return False

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^(01[0125]\d{8})$", phone))

def validate_password(password: str) -> bool:
    return len(password) >= 8