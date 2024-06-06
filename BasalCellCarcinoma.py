import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown("""
    <h1 style='color: Black;'>Basal Cell Carcinoma (BCC)</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
           Basal Cell Carcinoma (BCC) is the most common type of skin cancer, arising from the basal cells in the epidermis. 
            It usually develops in sun-exposed areas and grows slowly, rarely metastasizing but potentially causing significant local damage.
        </p>
          
            
    <h2 style='color: Black;'>Symtoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Open Sores</strong>A persistent, non-healing sore that may bleed, ooze, or crust over.</li>
        <li style="font-size: 22px;"><strong>Red Patches:</strong>Scaly, red patches that may itch or cause discomfort.</li>
        <li style="font-size: 22px;"><strong>Shiny Bumps or Nodules:</strong>Pearly or translucent bumps, often pink, red, or white, but can also be tan, black, or brown, especially in darker skin tones.</li>
        <li style="font-size: 22px;"><strong>Pink Growths:</strong>: A slightly elevated, rolled border with a crusted indentation in the center.</li>
        <li style="font-size: 22px;"><strong>Scar-like Area:</strong>A white, yellow, or waxy area with poorly defined borders that might resemble a scar.</li>
    </ul>
    </div>         
               

    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>UV Exposure:</strong>Prolonged and repeated exposure to ultraviolet (UV) radiation from the sun or tanning beds.</li>
        <li style="font-size: 22px;"><strong>Skin Type:</strong>Light-colored skin, hair, and eyes increase risk.</li>
        <li style="font-size: 22px;"><strong>Age:</strong>More common in older adults, typically over the age of 50.</li>
        <li style="font-size: 22px;"><strong>Genetics:</strong>Family history of skin cancer.</li>
        <li style="font-size: 22px;"><strong>Radiation Therapy:</strong>Previous radiation therapy increases the risk.</li>
    </ul>
    </div>   
            
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Sun Protection:</strong>Regularly use broad-spectrum sunscreen with high SPF, wear protective clothing, and seek shade during peak sun hours.</li>
        <li style="font-size: 22px;"><strong>Avoid Tanning Beds:</strong>: Stay away from artificial tanning devices.</li>
        <li style="font-size: 22px;"><strong>Regular Skin Checks:</strong>: Conduct self-examinations and have routine dermatological check-ups.</li>
        <li style="font-size: 22px;"><strong>Protective Measures:</strong>: Wear wide-brimmed hats, long-sleeved shirts, and UV-blocking sunglasses.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Surgical Excision</strong>Removing the tumor along with a margin of healthy skin.</li>
        <li style="font-size: 22px;"><strong>Mohs Surgery:</strong>A specialized technique where the tumor is removed layer by layer and examined microscopically until no cancer cells remain.</li>
        <li style="font-size: 22px;"><strong>Cryotherapy:</strong>: Freezing the cancer cells with liquid nitrogen.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Using lasers to remove the cancerous tissue.</li>
    </ul>
    </div> 
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'IMAGES/Basal Cell Carcinoma (BCC).png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Basal Cell Carcinoma (BCC)')       
            
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
