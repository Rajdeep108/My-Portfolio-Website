# importing dependencies
import streamlit as st
from functions import *

def experience_section():
    st.header("Experience",anchor="AI-Experience")
    vertical_space()
    st.markdown(f""" 
    <style>
    .custom-font {{
        font-family: "Arial", sans-serif;  /* Change font */
        font-size: 16px;  /* Change size */
    }}
    </style>

    <div class="custom-font">

    ##### <u>**Artificial Intelligence Intern**</u>
    *Smallcap.ai | London, UK* {horizontal_space(145)} *Oct 2024 – Feb 2025*  
    <ul>
    <li>Developed <b>ML models</b> for <b>fraud detection</b> & <b>content moderation</b> in a <b>blockchain gaming platform</b>, enhancing security & user trust.</li>
    <li>Deployed <b>AI solutions</b> on <b>Microsoft Azure</b>, enabling <b>scalable real-time analytics</b> for <b>large datasets</b>.</li>
    </ul>

    <br>
                                
    ##### <u>**Machine Learning Intern**</u>  
    *Roche Products | Welwyn Garden City, UK*  {horizontal_space(118)} *Jul 2024 – Sep 2024*  
    <ul>
    <li>Designed an <b>AI-powered patient engagement platform</b> to automate <b>consent form summarization</b> & <b>eCOA questionnaires</b>.</li>
    <li>Built <b>predictive models</b> for <b>patient data analysis</b>, improving <b>drug effectiveness tracking</b> & <b>personalized treatment strategies</b>.</li>
    </ul> 
    </div>
    """, unsafe_allow_html=True)