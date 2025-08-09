import streamlit as st



st.set_page_config(page_title="Crowd-Funding App", page_icon="💰", layout="wide")

st.title("💰 Crowd-Funding App")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Page", 
                            ["Home", "Register", "Activate Account", "Login", "View Projects", "Search Projects"])
