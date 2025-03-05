# importing dependencies
import streamlit as st
from functions import *


def education_section(): 
    st.header("Education", anchor="AI-Education")
    st.markdown(f"""
    <style>
            .custom-edu {{
                font-family: "Arial", sans-serif;  /* Change font */
                font-size: 16px;  /* Adjust text size */
            }}
    
            /* Flex container for alignment */
            .flex-container {{
                display: flex;
                justify-content: space-between;  /* Add space between location and date */
                align-items: center;
            }}
    
            /* Responsive design for small screens (phone view) */
            @media only screen and (max-width: 600px) {{
                .custom-edu {{
                    font-size: 14px;  /* Adjust font size for smaller screens */
                }}
                .flex-container {{
                    flex-direction: column;  /* Stack items vertically on mobile */
                    align-items: flex-start;  /* Align items to the left */
                }}
            }}
            /* Adding space below the university name */
            .education-title {{
                margin-bottom: 15px;  /* Adjust the space between title and points */
            }}
            /* Removing space between university name and course name */
            .course-title u {{
                margin-top: 0px;  /* Remove space between course and university name */
            }}
    </style>

    <div class="custom-edu">

    <div class="course-title">
        <u><b>Master of Science (MSc) in Artificial Intelligence</b></u>  
    </div>
    <div class="flex-container education-title">
        <span><em>Queen Mary University of London, UK</em></span>
        <span><em>Sep 2023 – Sep 2024</em></span>
    </div>
    <ul>
    <li>Graduated with <b>Distinction</b>, specializing in <b>AI/ML, NLP, Computer Vision, Robotics, etc..</b>.</li>
    <li>Developed a strong foundation in <b>AI algorithms, Applied Statistics, and advanced Deep Learning techniques</b>.</li>
    <li>Worked on <b>AI model optimization, finetuning and deployment</b>, tackling real-world AI challenges.</li>  
    </ul>
    <br>
                    
    <div class="course-title">
        <u><b>Bachelor of Technology (B.Tech) in Computer Science</b></u> 
    </div>
    <div class="flex-container education-title">
        <span><em>National Institute of Science and Technology, India</em></span>
        <span><em>Apr 2019 – Jul 2023</em></span>
    </div>
    <ul>
    <li>Built expertise in <b>data structures, algorithms, database management, OS, and computer networks</b>.</li>
    <li>Explored <b>cloud computing, distributed systems, and software engineering</b> for AI-driven applications.</li>
    <li>Developed strong <b>computational problem-solving skills</b>, essential for AI research and development.</li>
    </ul>  
    </div>
    """, unsafe_allow_html=True)
