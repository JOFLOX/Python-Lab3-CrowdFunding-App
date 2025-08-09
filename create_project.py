import streamlit as st
from validation import *

DATE_FORMAT = "%Y-%m-%d"

def create_project():
    st.header("Create New Project")
    
    with st.form("create_project_form"):
        title = st.text_input("Project Title")
        details = st.text_area("Project Details")
        target = st.number_input("Total Target (EGP)", min_value=0.01, step=0.01)
        start_date = st.date_input("Start Date").strftime(DATE_FORMAT) #THATS RETURN DATATIME.DATE(YYYY,MM,DD) OBJECT so we need to convert it to string
        end_date = st.date_input("End Date").strftime(DATE_FORMAT)
        submit = st.form_submit_button("Create Project")
        
        if submit:
            if end_date <= start_date:
                st.error("End date must be after start date.")
            elif project_exists(title):
                st.error("Project title already exists.")
            else:
                st.session_state.projects.append({
                    "owner_email": st.session_state.current_user['email'],
                    "title": title,
                    "details": details,
                    "target": target,
                    # "start": start_date.strftime(DATE_FORMAT), # convert datetime.date to string "YYYY-MM-DD"
                    # "end": end_date.strftime(DATE_FORMAT)
                    "start": start_date, 
                    "end": end_date 
                })
                st.success("Project created successfully!")
                st.write(st.session_state.projects)