# importing dependencies
import streamlit as st
from functions import *

def skills_section():
    st.header("Skills", anchor="AI-Skills")
    add_text("My technical and professional skills are essential to my problem-solving and efficiency. Below is a summary of my proficiency levels:",16,'white','none','left')

    pro1,pro2 = st.columns([1,1])
    with pro1:
        skill_bar("Python",100)
        skill_bar("Machine Learning & Deep Learning",97)
        skill_bar("Natural Language Processing",99)
        skill_bar("Docker",89)
        skill_bar("Snowflake",70)
        skill_bar("CI/CD Pipeline",85)
        skill_bar("Streamlit",98)
    with pro2:
        skill_bar("SQL Server",77)
        skill_bar("Generative Artificial Intelligence",99)
        skill_bar("Computer Vision",80)
        skill_bar("Azure Cloud Service",85)
        skill_bar("FastAPI",100)
        skill_bar("Kubernetes",75)
        skill_bar("Solara",67)