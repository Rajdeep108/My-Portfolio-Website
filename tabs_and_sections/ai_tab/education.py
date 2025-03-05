# importing dependencies
import streamlit as st
from functions import *


def education_section(): 
    st.header("Education",anchor="AI-Education")
    st.markdown(f"""
    <style>
            .custom-edu {{
                font-family: "Arial", sans-serif;  /* Change font */
                font-size: 16px;  /* Adjust text size */
            }}
    </style>
    <div class="custom-edu">

    ##### <u>**Master of Science (MSc) in Artificial Intelligence**</u>  
    *Queen Mary University of London, UK* {horizontal_space(124)} *Sep 2023 – Sep 2024*  
    <ul>
    <li>Graduated with <b>Distinction</b>, specializing in <b>AI/ML, NLP, Computer Vision, Robotics, etc..</b>.</li>
    <li>Developed a strong foundation in <b>AI algorithms, Applied Statistics, and advanced Deep Learning techniques</b>.</li>
    <li>Worked on <b>AI model optimization, finetuning and deployment</b>, tackling real-world AI challenges.</li>  
    </ul>
    <br>
                    
    ##### <u>**Bachelor of Technology (B.Tech) in Computer Science**</u> 
    *National Institute of Science and Technology, India* {horizontal_space(105)} *Apr 2019 – Jul 2023*  
    <ul>
    <li>Built expertise in <b>data structures, algorithms, database management, OS, and computer networks</b>.</li>
    <li>Explored <b>cloud computing, distributed systems, and software engineering</b> for AI-driven applications.</li>
    <li>Developed strong <b>computational problem-solving skills</b>, essential for AI research and development.</li>
    </ul>  
    </div>
    """, unsafe_allow_html=True)