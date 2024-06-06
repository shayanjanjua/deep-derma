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
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def app():
    # Set the background image
    set_background(r'IMAGES deepdermaa.jpg')  # Use raw string

    st.markdown("<h1 style='color: White;'>Frequently Asked Questions</h1>", unsafe_allow_html=True)

    # Include Montserrat font from Google Fonts
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    .montserrat {
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # Markdown content with a transparent box
    st.markdown("<h3 style='color: White;'>Is the diagnosis provided by the AI accurate?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="montserrat" style="background-color: rgba(255, 255, 255, 0.7); padding: 10px;border: 4px solid black; border-radius: 10px;">          
    <p style="font-size: 22px;line-height: 1.6; color: #333333;">
    While the AI system is trained on a large dataset and strives for high accuracy, it is not a substitute for a professional medical diagnosis. We recommend consulting a healthcare provider for a conclusive diagnosis.</p>
    </div>          
    """, unsafe_allow_html=True)

    # Markdown content with a transparent box
    st.markdown("<h3 style='color: White;'>Can the AI detect all types of skin diseases?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="montserrat" style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <p style="font-size: 22px;line-height: 1.6; color: #333333;">
    Our AI model is trained to recognize many common skin diseases. However, it may not identify rare or less common conditions. Continuous updates and training help improve its capabilities.</p>
    </div>          
    """, unsafe_allow_html=True)

    # Markdown content with a transparent box
    st.markdown("<h3 style='color: White;'>Is my uploaded image stored or shared?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="montserrat" style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <p style="font-size: 22px;line-height: 1.6; color: #333333;">
   We respect your privacy. Images uploaded for analysis are not stored or shared. They are processed in real-time and deleted immediately after analysis.</p>
    </div>          
    """, unsafe_allow_html=True)


    # Markdown content with a transparent box
    st.markdown("<h3 style='color: White;'>Is there any cost associated with using this tool?</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="montserrat" style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <p style="font-size: 22px;line-height: 1.6; color: #333333;">
    The basic analysis tool is free to use. However, we may offer premium features or detailed reports for a fee in the future.</div>          
    """, unsafe_allow_html=True)


# Footer
    st.markdown("""
    <div style="background-color: #4592DF; padding: 5px; text-align: center; color: white; position: fixed; bottom: 0; width: 100%;">
        <p>&copy; 2024 Deep Derma. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

app()
