import streamlit as st
from init_state import init_session_state
from register import register
from activate import activate_account
from login import login


st.set_page_config(page_title="Crowd-Funding App", page_icon="💰", layout="wide")

st.title("💰 Crowd-Funding App")

init_session_state()

main_menu = ["Home", "Register", "Activate Account", "Login"]
user_menu = ["dashboard", "Create Project", "View Projects", "Logout"]

if st.session_state.current_user is None:

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose Page", 
                                main_menu,)

    if page == "Home":
        st.write("Welcome to the Crowd-Funding App!")
        st.write("Please register or login to get started.")
    elif page == "Register":
        register()
    elif page == "Activate Account":
        activate_account()
    elif page == "Login":
        login()
else:
    # Logged in user menu
    

    
    st.sidebar.title(f"Welcome {st.session_state.current_user['first_name']}")
    
    if st.sidebar.button("Logout"):
        st.session_state.current_user = None
        st.session_state.page = "home"
        st.rerun()
    
    page = st.sidebar.selectbox("Choose Action", 
                                ["Dashboard", "Create Project", "View All Projects", "My Projects", "Search Projects"])
    
    if page == "Dashboard":
        st.header(f"Dashboard - Welcome {st.session_state.current_user['first_name']}!")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Projects", len(st.session_state.projects))
        with col2:
            my_count = len([p for p in st.session_state.projects if p['owner_email'] == st.session_state.current_user['email']])
            st.metric("My Projects", my_count)
            
