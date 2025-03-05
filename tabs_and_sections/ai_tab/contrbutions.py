# importing dependencies
import streamlit as st
from functions import *

def contribution_section():
    st.header("My Contributions",anchor="AI-Contributions")
    st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Professional font */
            font-size: 16px;  /* Readable text size */
        }
    </style>

    <div class="custom-text">
        <p>➤ <b>Collaborated with a colleague from the European Space Agency (ESA)</b> on a project to automate lunar rovers using AI and LiDAR. Focused on optimizing navigation, obstacle avoidance, and autonomous decision-making for extraterrestrial exploration.</p>
        <p>➤ <b>Contributed AI models to Hugging Face</b>, enhancing the open-source NLP and deep learning ecosystem.</p>
        <p>➤ <b>Built and contributed ML-powered applications to Streamlit</b>, improving the accessibility of interactive AI-driven web apps.</p>
        <p>➤ <b>Developed and contributed to FireNET on GitHub</b>, an open-source framework for scalable AI deployments and model inference.</p>
    </div>
    """, unsafe_allow_html=True)