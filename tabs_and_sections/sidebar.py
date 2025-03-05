# importing dependencies
import streamlit as st
from streamlit_scroll_navigation import scroll_navbar
from PIL import Image
from functions import *

#sidebar-------------------------------------
def entire_sidebar():
    with st.sidebar:
        # mobile scrollability
        st.markdown("""
            <style>
                @media screen and (max-width: 768px) {
                    [data-testid="stSidebarContent"] {
                        height: 75vh !important;
                        max-height: 75vh !important;
                        overflow-y: scroll !important;
                    }
                }
            </style>
        """, unsafe_allow_html=True)
        #My round face
        round_image = Image.open("./assets/pictures/me2.png")
        col1, col2, col3 = st.columns([0.8, 2, 1])
        with col2: 
            st.image(round_image, width=150)
        
        # My name
        t1,t2,t3 = st.columns([0.95,3.5,0.15])
        with t2:
            st.text("Rajdeep Roshan Sahu")
        
        # My social media links
        icon_buttons3(icon_path1="assets/icons/linkedin_icon.svg",icon_path2="assets/icons/github_icon.svg",icon_path3="assets/icons/youtube_icon.svg")
        vertical_space(2)
        
        st.subheader("Navigate")
        scroll_navbar(anchor_ids=["Home-Page"],anchor_icons=["house"],anchor_labels=["Home-Page"],key='Landing Page')

        with st.expander("1.\u00A0  Artificial Intelligence"):
            scroll_navbar(anchor_ids=["AI-About Me","AI-Skills","AI-Experience","AI-Projects","AI-Education","AI-Recommendations","AI-Contributions"],
                        anchor_icons=["info-circle","tools","briefcase","journals","book","hand-thumbs-up","trophy"],
                        anchor_labels=["About Me","Skills","Experience","Projects","Education","Recommendations","Contributions"],
                        key= "AI navigation" )
        
        with st.expander("2.\u00A0  Visual FX & Filmmaking"):
            scroll_navbar(anchor_ids=["to be continued"],
                        anchor_icons=["camera-reels"],
                        anchor_labels=["<To be continued>"],
                        key= "VFX navigation" )
            
        scroll_navbar(anchor_ids=["Contact Me"],anchor_icons=["person-lines-fill"],anchor_labels=["Contact"],key="Contact navigation")
        st.markdown("""
        <style>
            @media screen and (max-width: 768px) {
                [data-testid="stSidebarContent"] {
                    height: 75vh !important;
                    max-height: 75vh !important;
                    overflow-y: scroll !important;
                }
            }
        </style>
