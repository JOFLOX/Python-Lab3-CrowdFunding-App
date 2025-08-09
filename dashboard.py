import streamlit as st

def dashboard():
    st.header(f"Dashboard - Welcome {st.session_state.current_user['first_name']}!")    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Projects", len(st.session_state.projects))
    with col2:
        my_count = len([p for p in st.session_state.projects if p['owner_email'] == st.session_state.current_user['email']])
        st.metric("My Projects", my_count)