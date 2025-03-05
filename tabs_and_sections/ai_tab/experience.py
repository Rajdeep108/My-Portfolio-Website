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
    
    /* Flex container for alignment */
    .flex-container {{
        display: flex;
        justify-content: space-between;  /* Add space between location and date */
        align-items: center;
    }}
    
    /* Responsive design for small screens (phone view) */
    @media only screen and (max-width: 600px) {{
        .custom-font {{
            font-size: 14px;  /* Adjust font size for smaller screens */
        }}
        .flex-container {{
            flex-direction: column;  /* Stack items vertically on mobile */
            align-items: flex-start;  /* Align items to the left */
        }}
    }}
    </style>

    <div class="custom-font">

    ##### <u>**Artificial Intelligence Intern**</u>
    <div class="flex-container">
        <span><em>Smallcap.ai | London, UK</em></span>
        <span><em>Oct 2024 – Feb 2025</em></span>
    </div>
    <ul>
    <li>Developed <b>ML models</b> for <b>fraud detection</b> & <b>content moderation</b> in a <b>blockchain gaming platform</b>, enhancing security & user trust.</li>
    <li>Deployed <b>AI solutions</b> on <b>Microsoft Azure</b>, enabling <b>scalable real-time analytics</b> for <b>large datasets</b>.</li>
    </ul>

    <br>
                                
    ##### <u>**Machine Learning Intern**</u>  
    <div class="flex-container">
        <span><em>Roche Products | Welwyn Garden City, UK</em></span>
        <span><em>Jul 2024 – Sep 2024</em></span>
    </div>
    <ul>
    <li>Designed an <b>AI-powered patient engagement platform</b> to automate <b>consent form summarization</b> & <b>eCOA questionnaires</b>.</li>
    <li>Built <b>predictive models</b> for <b>patient data analysis</b>, improving <b>drug effectiveness tracking</b> & <b>personalized treatment strategies</b>.</li>
    </ul> 
    </div>
    """, unsafe_allow_html=True)
