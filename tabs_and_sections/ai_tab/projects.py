# importing dependencies
import streamlit as st
from functions import *

def projects_section():
    st.header("Projects",anchor="AI-Projects")
    with st.expander("🔍 AI-Powered Web Crawler agent for Autonomous Task Execution"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
    <ul>
        <li>Intelligently discovers, updates, and filters URLs in real time, ensuring access to the most relevant and valuable data before downloading.</li>
        <li>Leverages AI-driven decision-making to analyze web content, filtering out irrelevant information and processing only high-quality data.</li>
        <li>Extracts, enhances, and systematically stores information in MongoDB, enabling fast, structured, and efficient data retrieval for seamless analysis.</li>
    </ul>
    </div>

    """, unsafe_allow_html=True)

    with st.expander("🧠 Building a Small Foundational Language Model"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Implements an encoder-decoder architecture to generate concise command-type responses for lightweight systems.</li>
            <li>Processes real-time inputs efficiently, enabling autonomous decision-making in microcontrollers and robotic rovers.</li>
            <li>Designed with a small parameter count, making it feasible to run on low-end laptops without requiring high computational power.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏥 AI-Powered Patient Engagement Platform"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Facilitates clinical trials by automating patient communication and improving engagement.</li>
            <li>Summarizes informed consent forms, localizes them into multiple languages, and generates audio versions for accessibility.</li>
            <li>Integrates a smart notification system to remind patients of key trial activities and ensure compliance.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
            
    with st.expander("🚨 NSFW Content Detection & Regulation"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Utilizes CLIP-based Transformer models from Hugging Face for high-accuracy NSFW content detection.</li>
            <li>Provides a CLI tool for efficient, on-demand content moderation and analysis.</li>
            <li>Supports real-time filtering and automated enforcement for user-generated content platforms.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💰 Financial Fraud Detection in Blockchain Gaming"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Developed anomaly detection algorithms to flag suspicious transactions in blockchain gaming platform.</li>
            <li>Applied graph-based fraud detection to uncover illicit behavior and collusion networks.</li>
            <li>Enhanced security and compliance with AI-driven behavior tracking and dynamic risk scoring.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("💬 Medical Chatbot with Retrieval-Augmented Generation (RAG)"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Implemented FAISS vector search and LangChain for efficient retrieval of medical knowledge.</li>
            <li>Fine-tuned response generation using RAG to enhance accuracy and reliability in medical queries.</li>
            <li>Optimized for real-time deployment in healthcare advisory and decision-support systems.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 Multimodal Data Analysis for Healthcare & Finance"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Achieved a <span>30%</span> improvement in decision-making using AI-powered data insights.</li>
            <li>Automated feature extraction and correlation analysis for enhanced financial and healthcare analytics.</li>
            <li>Integrated Power BI for seamless, data-driven business intelligence and reporting.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🎨 Generative AI for Art Creation"):
        st.markdown("""
    <style>
        .custom-text {
            font-family: "Arial", sans-serif;  /* Change font */
            font-size: 16px;  /* Adjust size */

        }
    </style>

    <div class="custom-text">
            <ul>
            <li>Achieved <span>95%</span> realism while enhancing creativity in AI-generated artwork.</li>
            <li>Utilized latent space manipulation to explore and generate unique artistic styles.</li>
            <li>Optimized model architectures for scalable, high-quality, and efficient rendering.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)