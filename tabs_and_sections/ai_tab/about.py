# importing dependencies
import streamlit as st
from PIL import Image
from functions import *

def about_section():
    st.header("About Me",anchor= "AI-About Me")
    vertical_space()

    chalumn1,chalumn2 = st.columns([0.5,1.5])
    about_image = Image.open("assets/pictures/me3.JPG")

    with chalumn1:
        small_image = st.image(about_image)
    with chalumn2:
        st.markdown("""
        <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
        <p>
            I’m a <strong>passionate AI & Machine Learning Engineer</strong> who thrives on transforming complex challenges into elegant, AI-driven solutions. 
            With an <strong>MSc in Artificial Intelligence</strong> from Queen Mary University of London (Russell Group) and a <strong>B.Tech in Computer Science</strong>, my journey has been fueled by an 
            <em>insatiable curiosity</em>, evolving from a code enthusiast into a tech innovator.
        </p>

        <p><strong>Over the years, I’ve engineered cutting-edge AI solutions that push boundaries:</strong></p>
        <ul style="list-style-type: disc; margin-left: 20px;">
            <li><strong>Fraud detection systems</strong> for blockchain gaming, enhancing security and user experience.</li>
            <li><strong>Sophisticated RAG chatbots</strong> designed for high-speed, high-accuracy query handling.</li>
            <li><strong>Predictive healthcare models</strong>, improving patient outcomes through intelligent forecasting.</li>
        </ul>

        <p>
            My toolbox is brimming with the latest technologies in <strong>Generative AI, Reinforcement Learning, NLP, and Computer Vision</strong>. 
            I leverage frameworks like <strong>TensorFlow</strong> and <strong>PyTorch</strong>, along with cloud platforms such as <strong>Azure, Docker, and Kubernetes</strong>, 
            to build scalable, high-impact AI solutions.
        </p>
        
        </div>
        """,
        unsafe_allow_html=True)

    st.markdown(
    """
    <div style="text-align: justify; font-family: Arial, sans-serif; font-size: 16px;">
        <p style="font-size: 18px; color: orange; font-weight: bold; font-family: Courier New Monospace"><em>Innovation is at the heart of everything I do !</em></p>
        <p>I don’t just build AI, I engineer intelligence that scales. Whether it's designing <strong>LLM architectures</strong>, optimizing <strong>ML pipelines</strong>, or deploying models seamlessly in production, my work is driven by <strong>precision, performance, and real-world impact</strong>.</p>
        <p>When I’m not training models, you’ll likely find me <em>optimizing my caffeine intake</em> or pondering whether AI will ever grasp sarcasm as well as I do.</p>
        <p><strong>Let’s build something extraordinary together. 🚀</strong></p>
        <p>Hoping to grow my <em>\"neural\" network. </em>Here’s my <a href="https://www.linkedin.com/in/rajdeep-roshan-sahu" target="_blank" style="font-weight: bold; color:rgb(255, 152, 84); text-decoration: none;">LinkedIn</a>.</p>
    </div>
    """,
    unsafe_allow_html=True,
    )
