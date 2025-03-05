# importing dependencies
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from functions import *

def home_page_section():
    #Title with animation
    k1,k2,k3 = st.columns([0.5,1,3])
    with k1:
        custom_anchor("Home-Page")
        vertical_space(1)
        st.write("#### Hi there")
    with k2:
        hi_animation = load_lottie_json("assets/animations/Hi_animation.json")
        st_lottie(hi_animation, width=100, height=100, loop=True)

    #Hero image
    column1,column2 = st.columns([1.3, 2])
    square_image  = Image.open("assets/pictures/hero-bg.jpg")
    with column2:
        reomve_top_empty()
        st.image(square_image)

    #My name and overview animation
    with column1:
        vertical_space(4)
        st.write("# Rajdeep Roshan")
        kol1,kol2,kol3 = st.columns([0.2,1.5,0.1])
        with kol1:
            st.markdown("<h4>I'm </h4>", unsafe_allow_html=True)
        with kol2:
            typewriter2(word_list=['a Gen AI Developer','an AI/ML Engineer','a Film-maker','an Innovator',"wid pronouns: AI/ML"])
    
