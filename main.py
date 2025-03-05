# importing dependencies
import streamlit as st
# Custom made functions import
from functions import *
from tabs_and_sections.sidebar import entire_sidebar
from tabs_and_sections.home_page import home_page_section
from tabs_and_sections.ai_tab.about import about_section
from tabs_and_sections.ai_tab.skills import skills_section
from tabs_and_sections.ai_tab.recommendations import recommendation_section
from tabs_and_sections.ai_tab.projects import projects_section
from tabs_and_sections.ai_tab.experience import experience_section
from tabs_and_sections.ai_tab.education import education_section
from tabs_and_sections.ai_tab.contrbutions import contribution_section
from tabs_and_sections.vfx_tab.in_progress import work_in_progress_section
from tabs_and_sections.contact import contact_section
from tabs_and_sections.end_section import last_section
# code----------------------------------

#Basic page formatting
screenANDtitle()
hide_default_streamlit()

st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5, user-scalable=yes">
    """,
    unsafe_allow_html=True,
)

#sidebar-------------------------------------------
entire_sidebar()

# Main page-----------------------------------------------
home_page_section()
#Tabs for AI and VFX
tab_customize()
tab1, tab2 = st.tabs(["Artificial Intelligence", "Filmmaking & VFX"])
with tab1:#AI tab-------------------------------------------------
    #About section
    about_section()
    st.write("-----")

    #Skills section
    skills_section()
    st.write("-----")

    # Experience Section
    experience_section()
    st.write("---")
    
    #Projects section
    projects_section()
    st.markdown("---")

    #Education Section
    education_section()
    st.write("---")

    #Recommendations Section
    recommendation_section()
    st.write("---")

    # Contributions
    contribution_section()
    st.write("---")

with tab2: #VFX tab----------------------------------------
    work_in_progress_section()
    vertical_space(5)
    st.write("---")

#Contact Section--------------------------------
contact_section()
st.write("---")

#Last Section-------------------------
last_section()
