# importing dependencies
import streamlit as st
from functions import *

def last_section():
    st.markdown(f"""
    <style>
        .footer-text {{
            font-family: "Arial", sans-serif;  /* Clean and modern font */
            font-size: 14px;  /* Adjust text size */
            font-weight: bold;  /* Makes it slightly prominent */
            text-align: center;  /* Centers the text */
            color: #666666;  /* Subtle gray color for a professional look */
            margin-top: 20px;  /* Adds spacing from above elements */
        }}
    </style>

    <p class="footer-text">❤️ Made with love, by Rajdeep !!!!</p>
    """, unsafe_allow_html=True)