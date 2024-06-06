import streamlit as st
from PIL import Image

def app():
    st.markdown("""
    <h1 style='color: Black;'>Dermatofibroma</h1> 
    <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #White;">
       Dermatofibroma is a common, benign skin growth that usually appears on the legs, though it can develop on any part of the body. It is composed of fibrous tissue and often arises following minor skin trauma.
    </p>
      
    <h2 style='color: Black;'>Symptoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Appearance:</strong>Small, firm, raised nodule, often less than 1 cm in diameter.</li>
        <li style="font-size: 22px;"><strong>Texture:</strong>Smooth surface but feels firm or hard to the touch.</li>
        <li style="font-size: 22px;"><strong>Color:</strong>Color varies from pink to reddish-brown or dark brown.</li>
        <li style="font-size: 22px;"><strong>Location:</strong>Commonly found on the legs, but can appear on other parts of the body.</li>
        <li style="font-size: 22px;"><strong>No Pain:</strong>Generally painless, but can be tender or itchy.</li>
    </ul>
    </div>         
    
    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Minor Skin Injury:</strong>Often develops after a minor injury, such as an insect bite, shaving cut, or a thorn prick.</li>
        <li style="font-size: 22px;"><strong>Immune Response:</strong>Thought to be an abnormal response to minor skin injuries or infections.</li>
        <li style="font-size: 22px;"><strong>Genetics:</strong>There may be a genetic predisposition, though the exact cause is not fully understood.</li>
    </ul>
    </div>   
    
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Avoid Skin Trauma:</strong>Minimize skin injuries by taking precautions during activities that may cause skin trauma.</li>
        <li style="font-size: 22px;"><strong>Protective Clothing:</strong>Wear long sleeves and pants when in environments where skin injury is more likely.</li>
        <li style="font-size: 22px;"><strong>Skin Care:</strong>Maintain good skin care to reduce the risk of minor skin injuries.</li>
    </ul>
    </div>   
    
    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Observation:</strong>Often no treatment is necessary if the dermatofibroma is not causing symptoms or cosmetic concern.</li>
        <li style="font-size: 22px;"><strong>Surgical Excision:</strong>Removing the growth surgically, usually done if it is symptomatic or for cosmetic reasons.</li>
        <li style="font-size: 22px;"><strong>Cryotherapy:</strong>Freezing the lesion with liquid nitrogen to reduce its size.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Using laser light to remove the growth.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\Dermatofibroma.png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Dermatofibroma Treatment')

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