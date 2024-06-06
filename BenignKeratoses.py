import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown("""
    <h1 style='color: Black;'>Benign Keratoses</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
           Benign Keratoses refer to non-cancerous growths on the skin, including seborrheic keratoses and keratosis pilaris. These growths are generally harmless but may cause cosmetic concerns or discomfort.
        </p>
          
            
    <h2 style='color: Black;'>Symtoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Appearance:</strong>Brown, black, or light tan growths with a waxy, stuck-on look.</li>
        <li style="font-size: 22px;"><strong>Texture:</strong>Can be flat or slightly elevated with a rough, wart-like surface.</li>
        <li style="font-size: 22px;"><strong>Size:</strong>Varies from tiny spots to larger patches.</li>
        <li style="font-size: 22px;"><strong>Location:</strong>: Commonly found on the chest, back, shoulders, and face.</li>
        <li style="font-size: 22px;"><strong>No Pain:</strong>Generally painless, though they may itch or become irritated if rubbed by clothing.</li>
    </ul>
    </div>         
               

    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Sun Exposure:</strong>ay be related to cumulative UV exposure.</li>
        <li style="font-size: 22px;"><strong>Skin Type:</strong>Light-colored skin, hair, and eyes increase risk.</li>
        <li style="font-size: 22px;"><strong>Age:</strong>Commonly occurs in middle-aged and older adults.</li>
        <li style="font-size: 22px;"><strong>Genetics:</strong>Tends to run in families.</li>
        <li style="font-size: 22px;"><strong>Skin Type:</strong>More common in people with dry skin or eczema.</li>
    </ul>
    </div>   
            
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Sun Protection:</strong>Use sunscreen and wear protective clothing to reduce UV exposure.</li>
        <li style="font-size: 22px;"><strong>Skin Care:</strong>: Regular moisturizing to maintain skin health.</li>
        <li style="font-size: 22px;"><strong>Gentle Exfoliation:</strong>Regular exfoliation can help to remove dead skin cells and reduce bumps.</li>
        <li style="font-size: 22px;"><strong>Humidifiers:</strong>Use humidifiers to add moisture to the air, especially in dry climates or during winter.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Curettage:</strong>Scraping the growth off the skin.</li>
        <li style="font-size: 22px;"><strong>Gentle Skin Care:</strong>Avoid harsh soaps and prolonged hot showers to prevent further skin drying.</li>
        <li style="font-size: 22px;"><strong>Cryotherapy:</strong>Freezing the growth with liquid nitrogen.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Using laser light to remove the growth.</li>
    </ul>
    </div>               
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\Benign Keratoses.png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Benign Keratoses')       
            
    st.markdown("""
    <h2 style='color: Black;'>Monitoring and Follow-Up</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;">Regular dermatological check-ups are essential to monitor and manage the condition.</li>
       <li style="font-size: 22px;">Stay vigilant for any changes in existing lesions or the appearance of new ones.</li>
    </ul>
    </div>                 

    """, unsafe_allow_html=True)
app()