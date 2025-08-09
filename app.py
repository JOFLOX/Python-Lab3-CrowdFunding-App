import streamlit as st
from init_state import init_session_state

st.set_page_config(page_title="Crowd-Funding App", page_icon="💰", layout="wide")

st.title("💰 Crowd-Funding App")

init_session_state()

main_menu = ["Home", "Register", "Activate Account", "Login", "View Projects", "Search Projects"]

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Page", 
                            main_menu,)

if page == "Home":
    st.write("Welcome to the Crowd-Funding App!")
    st.write("Please register or login to get started.")
