import streamlit as st
from PIL import Image
import base64

# Function to set the background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def app():
    # Set the background image
    set_background(r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\background image deep dermaa.jpg')  # Use raw string

    # Markdown content with a transparent box
    st.markdown("""
    <h1 style='color: White;'>Contact Us</h1>           
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 20px; border: 4px solid black; border-radius: 10px;">
        <h3 style="text-align: center;">Connect with us:</h3>
        <div style="display: flex; justify-content: center;">
            <a href="https://www.facebook.com/profile.php?id=61560670403294" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" style="width: 50px; margin-right: 20px;">
            </a>
            <a href="https://www.instagram.com/deep_derma" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1024px-Instagram_icon.png" alt="Instagram" style="width: 50px; margin-right: 20px;">
            </a>
            <a href="mailto:deepderma1@gmail.com" target="_blank">
                <img src="https://img.icons8.com/color/48/000000/gmail-new.png" alt="Gmail" style="width: 50px;">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="background-color: #4592DF; padding: 5px; text-align: center; color: white; position: fixed; bottom: 0; width: 100%;">
        <p>&copy; 2024 Deep Derma. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

app()
