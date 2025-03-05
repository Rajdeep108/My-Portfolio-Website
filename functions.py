# importing dependencies
import streamlit as st
import streamlit.components.v1 as components
import json
import random
import base64

# functions
def screenANDtitle():
    return st.set_page_config("Rajdeep-Portfolio",layout="wide")

def hide_default_streamlit():
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}

                /* Dark mode styles */
                body { background-color: #121212; color: #E1E1E1; }
                .stApp { background-color: #121212; color: #E1E1E1; }
                .stButton>button { background-color: #BB86FC; color: white; }
                .stTextInput>div>div>input { background-color: #1E1E1E; color: white; }
                </style>
                """
    return st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def load_svg(svg_path):
    with open(svg_path, "r") as f:
        return f.read()

def load_lottie_json(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
        
def icon_buttons3(icon_path1,icon_path2,icon_path3, width1=28,width2=33,width3=28):
    with open(icon_path1, "r") as f:
        svg_content1 = f.read()
    with open(icon_path2, "r") as f:
        svg_content2 = f.read()
    with open(icon_path3, "r") as f:
        svg_content3 = f.read()
    st.markdown(
        f"""
        <a href="https://www.linkedin.com/in/rajdeep-roshan-sahu" target="_blank" style="text-decoration: none;">
            <span style="display: inline-block; width: {width1}px; margin-left: 55px; margin-right: 30px;">{svg_content1}
        </a>

        <a href="https://www.github.com/Rajdeep108" target="_blank">
            <span style="display: inline-block; width: {width2}px; margin-right: 30px">{svg_content2}
        </a>

        <a href="https://www.youtube.com/@Madhouseproductions" target="_blank" style="text-decoration: none;">
            <span style="display: inline-block; width: {width3}px;">{svg_content3}</span>
        </a>     
        """,
        unsafe_allow_html=True
    )

def vertical_space(space_count=1):
    for i in range(space_count):
        st.write("")

def horizontal_space(space_count=10):
    return "&nbsp;" * space_count 

def hide_expander_bar():
    hide =  """
    <style>
    [data-testid="stExpander"] details {
        border-style: none;
        }
    </style>
    """

    return st.markdown(hide, unsafe_allow_html=True)

def reomve_top_empty():
        st.markdown(
    """
    <style>
        .block-container {
            padding-top: 30px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

def add_text(text,font_size=36,color = "white",weight='bold',align='left',font_family='Arial',bg_color='Light gray',padding =10,border_rad=10):
    return st.markdown(
    f"""
    <style>
        .custom-text {{
            font-size: {font_size}px; 
            color: {color}; /* Red color */
            font-weight: {weight};
            text-align: {align};
            background-color: {bg_color}; /* Light gray background */
            padding: {padding}px;
            border-radius: {border_rad}px;
            box-shadow: 0px 0px 0px rgba(0,0,0,0);
            font-family: {font_family}, sans-serif;
        }}
    </style>
    <p class="custom-text">{text}</span></p>
    """,
    unsafe_allow_html=True,
    )

def typewriter2(word_list: list):
    words_js = json.dumps(word_list)
    html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Typewriter Effect</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

        .container {{
            display: inline-flex;
            align-items: center;  /* Ensures text and cursor are aligned */
            margin-top: -10.5px;  /* Adjust as needed */
            margin-left: -3px;  /* Adjust as needed */
        }}

        .animated-text {{
            font-family: 'Press Start 2P', cursive;
            font-size: 16px;  /* Increased for better readability */
            color: #fa9343;
            text-shadow: 2px 2px 5px rgba(255, 87, 51, 0.9);
            line-height: 2;  /* Increased height */
            letter-spacing: 1px;
            white-space: nowrap;
            overflow: hidden;
            display: inline-block;
            min-height: 40px;  /* Increased for better spacing */
        }}

        .cursor {{
            display: inline-block;
            width: 10px;
            height: 30px;  /* Increased height to match text */
            background-color: #fa9343;
            vertical-align: bottom;  /* Align cursor with text baseline */
            animation: blink 0.51s infinite alternate;
        }}

        @keyframes blink {{
            0% {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <p class="animated-text" id="typewriter"></p>
        <span class="cursor"></span>
    </div>

    <script>
        const words = {words_js};  // Insert dynamic words list;
        const writingDelay = 180;
        const erasingDelay = 180;
        const blinkDelay = 550;
        let wordIndex = 0;
        let charIndex = 0;
        let isErasing = false;

        function typeEffect() {{
                let display = document.getElementById("typewriter");
                let currentWord = words[wordIndex];

                if (!isErasing) {{
                    display.style.visibility = "visible";
                    display.textContent = currentWord.substring(0, charIndex + 1);
                    charIndex++;
                    if (charIndex === currentWord.length) {{
                        isErasing = true;
                        setTimeout(typeEffect, blinkDelay * 6);
                    }} else {{
                        setTimeout(typeEffect, writingDelay);
                    }}
                }} else {{
                    display.textContent = currentWord.substring(0, charIndex - 1);
                    charIndex--;
                    if (charIndex === 0) {{
                        display.style.visibility = "hidden";
                        isErasing = false;
                        wordIndex = (wordIndex + 1) % words.length;
                        setTimeout(typeEffect, writingDelay);
                    }} else {{
                        setTimeout(typeEffect, erasingDelay);
                    }}
                }}
            }}
            
            typeEffect();
        </script>
    </body>
    </html>
"""
    return components.html(html_code, height=250)

def tab_customize():
    return st.markdown("""
    <style>
        /* Center the tabs */
        div[data-testid="stTabs"] div[role="tablist"] {
            justify-content: center;
        }
        /* Remove underline from tabs */
        div[data-testid="stTabs"] div[role="tablist"] button {
            border-bottom: none !important;
        }
        /* Make tab titles larger */
        div[data-testid="stTabs"] div[role="tablist"] button p {
            font-size: 19px !important;  /* Adjust size as needed */
            font-weight: none;
        }
    </style>
""", unsafe_allow_html=True)

# Inject CSS for styling
def progress_bar_style():
    return st.markdown(f"""
    <style>
        @keyframes glow {{
            0% {{ opacity: 0.3; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.3; }}
        }}

        @keyframes progress-glow {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .skill-container {{
            width: 100%;
            margin-bottom: 10px;
        }}
        .skill-header {{
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .progress-bar {{
            height: 20px;
            background-color: #ddd;
            border-radius: 5px;
            position: relative;
            overflow: hidden;
        }}
        .progress {{
            height: 100%;
            border-radius: 5px;
            transition: width 0.5s ease-in-out;
            background: linear-gradient(90deg, #FF8C00, #FF8C00, #FF8C00); 
            background-size: 200% 100%;
            animation: progress-glow 2s infinite linear;
        }}
        .glow {{
            position: absolute;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.3);
            animation: glow 2s infinite;
        }}
    </style>
    """, unsafe_allow_html=True)

# Function to display a skill with a progress bar
def skill_bar(skill:str, percentage:int, style_css=progress_bar_style):
    style_css()
    delay = round(random.uniform(0, 1.5), 2)  # Generate a random delay for each skill
    st.markdown(f"""
        <div class="skill-container">
            <div class="skill-header">
                <span>{skill}</span>
                <span>{percentage}%</span>
            </div>
            <div class="progress-bar">
                <div class="progress" style="width: {percentage}%; animation-delay: {delay}s;"></div>
                <div class="glow" style="animation-delay: {delay}s;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def slide_images(paths):
    # Define your image paths
    image_paths = paths  # Update with your paths

    # Generate base64 strings for images
    base64_images = [get_base64_image(img) for img in image_paths]

    # Automatically calculate animation duration (6s per image)
    num_images = len(base64_images)
    animation_duration = 6 * num_images  # Adjust speed as needed

    # Custom CSS for dynamic slider
    slide_animation = f"""
<style>
.slider-container {{
    width: 100%;
    overflow: hidden;
    position: relative;
    height: auto; /* Dynamically adjusts to image height */
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: black; /* Avoid blank spaces */
}}

.slider {{
    display: flex;
    width: {100 * num_images}%;
    animation: slide {animation_duration}s infinite ease-in-out;
}}

.slider img {{
    width: 100%;
    height: auto; /* Makes sure the full image is visible */
    max-height: 500px; /* Adjust this if needed */
    object-fit: contain; /* Ensures the full image is visible */
    background-color: black; /* Avoid blank areas */
}}
  
@keyframes slide {{
    0% {{ transform: translateX(0%); }}
    {"".join(f"{(i+1)*(100/num_images)}% {{ transform: translateX(-{(i+1)*(100/num_images)+21.5}%);}} " for i in range(num_images))}
    100% {{ transform: translateX(0%); }}
}}
</style>
"""

    # Display in Streamlit
    st.markdown(slide_animation, unsafe_allow_html=True)

    # Generate HTML for image slider with base64 images
    slider_html = f"""
    <div class="slider-container">
        <div class="slider">
            {"".join(f'<img src="data:image/jpeg;base64,{img}" alt="Image">' for img in base64_images)}
        </div>
    </div>
    """

    st.markdown(slider_html, unsafe_allow_html=True)

def custom_anchor(anchor):
        return st.markdown(f'<div id="{anchor}"></div>', unsafe_allow_html=True)
