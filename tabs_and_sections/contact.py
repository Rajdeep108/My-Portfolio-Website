# importing dependencies
import streamlit as st
import folium
from streamlit_folium import st_folium
from functions import *

def contact_section():
    st.header("Contact Me",anchor="Contact Me")
    con_col1,con_col2 = st.columns([1,1.5])

    # location coordinates 
    latitude = 19.293962  
    longitude = 84.789078 
    with con_col1:
        st.markdown("""
        <style>
            .custom-heading {
                font-family: "Arial", sans-serif;  /* Clean and professional font */
                font-size: 18px;  /* Adjust heading size */
            }
        </style>

        <div class="custom-heading">You will find me currently at:</div>
        """, unsafe_allow_html=True)

        m = folium.Map(
        location=[latitude, longitude], 
        zoom_start=12, 
        tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}", 
        attr="Google",control_scale=True
        )
        folium.Marker([latitude, longitude], tooltip="I am here!", icon=folium.Icon(color="blue")).add_to(m)
        st_folium(m, width=400, height=300)

    with con_col2:
        vertical_space(3)
        st.markdown("""
        <style>
            .contact-info {
                font-family: "Arial", sans-serif;  /* Professional and clean font */
                font-size: 16px;  /* Adjust size for readability */
                font-weight: 500;  /* Slightly bold for emphasis */
            }
            .contact-info a {
                text-decoration: none;  /* Removes underline from the link */
                color:rgb(255, 154, 31);  /* Professional blue color for links */
                font-weight: bold;
            }
            .contact-info a:hover {
                color:rgb(255, 154, 31);  /* Darker shade on hover */
            }
        </style>

        <p class="contact-info">📧 Email: <a href="mailto:rajdeeproshan2001@gmail.com">click to send mail</a></p>
        <p class="contact-info">📱 Phone: +91 7894941940, +44 7393062560</p>
        """, unsafe_allow_html=True)