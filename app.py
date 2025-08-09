import streamlit as st
from init_state import init_session_state
from register import register
from activate import activate_account
from login import login
from dashboard import dashboard
from create_project import create_project
from all_projects import all_projects
from my_projects import my_projects


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
        dashboard()
    elif page == "Create Project":
        create_project()
    elif page == "View All Projects":
        all_projects()
    elif page == "My Projects":
        my_projects()
    
            
