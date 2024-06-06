import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown("""
    <h1 style='color: Black;'>Vascular Malformations</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
           Vascular Malformations are congenital anomalies of the blood vessels, including arteries, veins, capillaries, or lymphatics. They are present at birth and can grow or change over time. These malformations are categorized into different types based on the involved vessels: capillary, venous, lymphatic, arterial, or combined.
        </p>
          
            
    <h2 style='color: Black;'>Symtoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Capillary Malformations:</strong>Flat, pink, red, or purple discoloration on the skin.Typically present at birth and can darken or thicken over time.</li>
        <li style="font-size: 22px;"><strong>Venous Malformations:</strong>Soft, compressible blue or purple masses.May swell or cause pain, especially when dependent (e.g., standing).</li>
        <li style="font-size: 22px;"><strong>Lymphatic Malformations:</strong>Soft, cystic masses, often filled with clear fluid.Can cause swelling and infection.</li>
        <li style="font-size: 22px;"><strong>Arteriovenous Malformations (AVMs):</strong>Abnormal connections between arteries and veins.Can cause a pulsatile mass, bleeding, or ulcers.</li>
        <li style="font-size: 22px;"><strong>Combined Malformations:</strong>Features of multiple types of vascular malformations.</li>
    </ul>
    </div>         
               

    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Congenital:</strong>Vascular malformations are present at birth and result from errors in vascular development during embryogenesis.</li>
        <li style="font-size: 22px;"><strong>Genetic Factors:</strong>Some vascular malformations are associated with genetic mutations or inherited conditions (e.g., Hereditary Hemorrhagic Telangiectasia.</li>
    </div>   
            
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Genetic Counseling:</strong>For families with a history of vascular malformations, genetic counseling may help understand risks and implications.</li>
        <li style="font-size: 22px;"><strong>Monitoring:</strong>Regular check-ups and monitoring, especially for individuals with known vascular malformations, can help manage potential complications.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Observation:</strong>Small or asymptomatic vascular malformations may not require immediate treatment and can be monitored.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Effective for treating superficial capillary malformations (e.g., port-wine stains) by reducing discoloration.</li>
        <li style="font-size: 22px;"><strong>Sclerotherapy:</strong>Freezing the growth with liquid nitrogen.: Injecting a sclerosing agent into the malformation to shrink it, commonly used for venous malformations.</li>
        <li style="font-size: 22px;"><strong>Surgical Excision:</strong>Removing the malformation, especially if it causes significant symptoms or complications.</li>
        <li style="font-size: 22px;"><strong>Embolization:</strong>Blocking abnormal blood vessels from within using various materials, often used for AVMs.</li>
        <li style="font-size: 22px;"><strong>Compression Therapy:</strong>Removing the malformation, especially if it causes significant symptoms or complications.Using compression garments to manage symptoms of venous and lymphatic malformations.</li>
    </ul>
    </div>       
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\Vascular Malformations.png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Vascular Malformations')   

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