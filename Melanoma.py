import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown("""
    <h1 style='color: Black;'>Melanoma</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
          Melanoma is a serious form of skin cancer that arises from melanocytes, the cells that produce pigment in the skin. It can spread to other parts of the body if not detected and treated early.
        </p>
          
            
    <h2 style='color: Black;'>Symtoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>New or Changing Moles:</strong>The most common sign is a new spot on the skin or a spot that's changing in size, shape, or color.</li>
        <li style="font-size: 22px;"><strong>Asymmetry:</strong>One half of the mole doesn't match the other half.</li>
        <li style="font-size: 22px;"><strong>Border:</strong>Varies from tiny spots to larger patches.Irregular, scalloped, or poorly defined edges.</li>
        <li style="font-size: 22px;"><strong>Color:</strong>Varied shades of brown, black, sometimes with patches of red, white, or blue.</li>
        <li style="font-size: 22px;"><strong>Diameter:</strong>Melanomas are usually larger than 6 mm (about the size of a pencil eraser) but can be smaller when first detected.</li>
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
        <li style="font-size: 22px;"><strong>UV Exposure:</strong>Prolonged and intense exposure to ultraviolet (UV) radiation from the sun or tanning beds.</li>
        <li style="font-size: 22px;"><strong>Fair Skin:</strong>Higher risk for people with fair skin, freckles, red or blonde hair, and light-colored eyes.</li>
        <li style="font-size: 22px;"><strong>Genetics:</strong>Family history of melanoma increases the risk.</li>
        <li style="font-size: 22px;"><strong>Moles:</strong>Having many moles or atypical (dysplastic) moles.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Surgical Excision:</strong>Removing the melanoma and a margin of surrounding healthy skin.</li>
        <li style="font-size: 22px;"><strong>Mohs Surgery:</strong>A precise surgical technique used mainly for very small or thin melanomas.</li>
        <li style="font-size: 22px;"><strong>Sentinel Lymph Node Biopsy:</strong>A precise surgical technique used mainly for very small or thin melanomas.</li>
        <li style="font-size: 22px;"><strong>Immunotherapy:</strong>A precise surgical technique used mainly for very small or thin melanomas.</li>
        <li style="font-size: 22px;"><strong>Chemotherapy:</strong>A precise surgical technique used mainly for very small or thin melanomas.</li>
        <li style="font-size: 22px;"><strong>Radiation Therapy:</strong>Using high-energy rays to destroy cancer cells, typically for advanced melanoma.</li>
    </ul>
    </div>       
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'IMAGES/Melanoma.png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Melanoma')       
            
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
