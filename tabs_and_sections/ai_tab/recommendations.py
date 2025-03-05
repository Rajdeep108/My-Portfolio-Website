# importing dependencies
import streamlit as st
from functions import *

def recommendation_section():
    st.header("Recommendations",anchor = "AI-Recommendations")
    slide_images([ "assets/recommendations/Review-Recommendation 1.jpg",
                    "assets/recommendations/Review-Recommendation 2.jpg"])
