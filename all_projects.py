import streamlit as st
from validation import *

def all_projects():
    st.header("All Projects")
    
    if not st.session_state.projects:
        st.info("No projects found.")
        return
    
    for idx, p in enumerate(st.session_state.projects, start=1):
        with st.expander(f"Project Number #{idx}:  {p['title']}"):
            st.write(f"**Details:** {p['details']}")
            st.write(f"**Target:** {p['target']} EGP")
            st.write(f"**Duration:** {p['start']} to {p['end']}")
            st.write(f"**Owner:** {p['owner_email']}")

