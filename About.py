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
    set_background(r'IMAGES/background image deep dermaa.jpg')  # Use raw string


    # Markdown content with a transparent box
    st.markdown("""
    <h1 style='color: White;'>DEEP DERMA: An AI-based Smart Skin Pathology Diagnosis</h1>           
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px;border: 4px solid black; border-radius: 10px;">
        <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
            Empowering individuals with the ability to recognize and address skin diseases early is the cornerstone of DEEP DERMA. Our cutting-edge web-based system harnesses the power of artificial intelligence to provide rapid and accurate diagnoses, paving the way for timely treatment and prevention of severe consequences.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # Load and display the first image
    img1 = Image.open(r'IMAGES/FYP IMG 01.png')
    st.image(img1, use_column_width=True)

    st.markdown("<h2 style='color: White;'>The Challenge</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">        
    <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
    Skin diseases, often underestimated, can lead to serious health risks if left untreated. With millions of cases reported annually, including the deadliest form of skin cancer, early detection is paramount. However, existing solutions lack comprehensive image-based diagnosis capabilities and fail to address the underlying causes of skin conditions.
    </p>
    </div>          
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='color: White;'>Our Solution</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
    DEEP DERMA bridges this gap by offering a smart skin pathology recommender driven by convolutional neural networks. Our system goes beyond mere identification, providing insights into the root causes of skin conditions. With the ability to detect over 10 diseases, including melanoma, eczema, and acne vulgaris, DEEP DERMA ensures comprehensive diagnosis in a single analysis.
    </p>
    </div>          
    """, unsafe_allow_html=True)

    # Load and display the second image
    img2 = Image.open(r'IMAGES/FYP IMG 02.png')
    st.image(img2, use_column_width=True)

    st.markdown("<h2 style='color: White;'>Why Choose DEEP DERMA</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Comprehensive Diagnosis:</strong> Detects over 10 skin diseases, ensuring thorough analysis.</li>
        <li style="font-size: 22px;"><strong>Early Intervention:</strong> Enables timely treatment to prevent severe health consequences.</li>
        <li style="font-size: 22px;"><strong>User-Friendly Interface:</strong> Intuitive design for seamless user experience.</li>
        <li style="font-size: 22px;"><strong>Personalized Recommendations:</strong> Tailored insights based on individual profiles and medical history.</li>
        <li style="font-size: 22px;"><strong>Cutting-Edge Technology:</strong> Harnesses the power of AI for rapid and accurate diagnosis.</li>
    </ul>
    </div>            
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="background-color: #4592DF; padding: 5px; text-align: center; color: white; position: fixed; bottom: 0; width: 100%;">
        <p>&copy; 2024 Deep Derma. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

app()
