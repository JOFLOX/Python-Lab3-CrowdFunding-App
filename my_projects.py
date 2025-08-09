import streamlit as st
from validation import *
import datetime

DATE_FORMAT = "%Y-%m-%d"


def my_projects():
    st.header("My Projects")
    
    my_projects = [p for p in st.session_state.projects if p['owner_email'] == st.session_state.current_user['email']]
    
    if not my_projects:
        st.info("You have no projects.")
        return
    
    for idx, p in enumerate(my_projects):
        with st.expander(f"{p['title']} ({p['start']} - {p['end']})"):
            st.write(f"**Details:** {p['details']}")
            st.write(f"**Target:** {p['target']} EGP")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Edit", key=f"edit_{idx}"):
                    st.session_state.editing_project = idx
            with col2:
                if st.button(f"Delete", key=f"delete_{idx}"):
                    # st.session_state.projects.remove(p) #kida kida unique so this should work tmam even when it just del the first accurance of the project
                    del st.session_state.projects[idx] # this will delete a specific project from the list safly
                    st.success("Project deleted successfully!")
                    st.rerun()

            if st.session_state.editing_project == idx:
                with st.form(f"edit_project_form_{idx}"):
                    new_title = st.text_input("Title", value=p['title'])
                    new_details = st.text_area("Details", value=p['details'])
                    new_target = st.number_input("Target (EGP)", value=p['target'], min_value=0.01, step=0.01)
                    new_start = st.date_input("Start Date", value=p['start'])
                    new_end = st.date_input("End Date", value=p['end'])


                    if st.form_submit_button("Update Project"):
                        if new_end <= new_start:
                            st.error("End date must be after start date.")
                        elif project_exists(new_title) and new_title != p['title']:
                            st.error("Project title already exists.")
                        else:
                            p.update({
                                "title": new_title,
                                "details": new_details,
                                "target": new_target,
                                "start": new_start.strftime(DATE_FORMAT),
                                "end": new_end.strftime(DATE_FORMAT)
                            })
                            st.success("Project updated successfully!")
                            st.session_state.editing_project = None
                            st.rerun()

