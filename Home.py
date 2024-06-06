import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json
import base64

def app():
    # CSS for styling
    st.markdown(
        """
        <style>
        .stApp {
            background-size: cover;
            background-position: center;
        }
        .welcome-text {
            font-size: 3.0rem;
            font-weight: bold;
            margin-bottom: 30px;
            text-align: center;
        }
        .text {
            font-size: 1.6rem;
            margin-bottom: 30px;
            text-align: center;
        }
        .lottie-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Heading
    st.markdown('<div class="welcome-text">Welcome to Deep Derma</div>', unsafe_allow_html=True)

    # Text
    st.markdown('<div class="text">An AI-based Smart Skin Pathology Diagnosis!</div>', unsafe_allow_html=True)

    # Load the Lottie animation file from local file system
    animation_path = r"C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\ANIMATIONS\virus.json"  
    with open(animation_path, "r") as f:
        animation_data = json.load(f)

    # Display Lottie animation if data is successfully loaded
    if animation_data is not None:
        st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
        st_lottie(
            animation_data,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            height=400, # Adjust the height as needed
            width=None,
            key=None,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Text
    st.markdown('<div class="text">Lets Begin A New Journey!</div>', unsafe_allow_html=True)
    
    
 
# Run the app function
app()
