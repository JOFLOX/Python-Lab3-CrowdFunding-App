import streamlit as st

def init_session_state():
    defaults = {
        "users": [],
        "projects": [],
        "current_user": None,
        "page": "home"
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
