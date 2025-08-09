import streamlit as st
from validation import *


DATE_FORMAT = "%Y-%m-%d"

def search_projects():
    st.header("Search Projects by Date")
    with st.form("search_form"):
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        submit = st.form_submit_button("Search")
        
        if submit:
            if end_date <= start_date:
                st.error("End date must be after start date.")
            else:
                results = [p for p in st.session_state.projects if p['start'] >= start_date.strftime(DATE_FORMAT) and p['end'] <= end_date.strftime(DATE_FORMAT)]
                if not results:

                    st.info("No projects found.")
                else:
                    for idx, p in enumerate(results, start=1):
                        with st.expander(f"Project Number #{idx}:  {p['title']}"):
                            st.write(f"**Details:** {p['details']}")
                            st.write(f"**Target:** {p['target']} EGP")
                            st.write(f"**Duration:** {p['start']} to {p['end']}")
                            st.write(f"**Owner:** {p['owner_email']}")  
    