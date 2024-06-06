import streamlit as st
from PIL import Image
import base64


def app():
    st.markdown("""
    <h1 style='color: Black;'>Melanocytic Nevi</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
           Melanocytic Nevi (commonly known as moles) are benign growths on the skin that result from a proliferation of melanocytes, the cells that produce pigment. While typically harmless, some moles can develop into melanoma, a serious form of skin cancer.
        </p>
          
            
    <h2 style='color: Black;'>Symtoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Appearance:Appearance:</strong>Moles can be flat or raised, and they vary in color from pink to light brown to dark brown or black.</li>
        <li style="font-size: 22px;"><strong>Shape:</strong>They are usually round or oval and have a smooth edge.</li>
        <li style="font-size: 22px;"><strong>Size:</strong>Moles are typically less than 6 mm in diameter (about the size of a pencil eraser).</li>
        <li style="font-size: 22px;"><strong>Changes:</strong>Most moles remain consistent in appearance, but changes in size, shape, or color can indicate a need for medical evaluation.</li>
    </ul>
    </div>         
               

    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>UV Exposure:</strong>Sun exposure, especially during childhood, can increase the number of moles.</li>
        <li style="font-size: 22px;"><strong>Genetics:</strong>Family history plays a significant role in the number and type of moles a person has.</li>
        <li style="font-size: 22px;"><strong>Hormonal Changes:</strong>Puberty and pregnancy can cause new moles to develop and existing moles to change.</li>
    </ul>
    </div>   
            
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Sun Protection:</strong>Use broad-spectrum sunscreen with a high SPF, wear protective clothing, and seek shade during peak sun hours.</li>
        <li style="font-size: 22px;"><strong>Avoid Tanning Beds:</strong>Refrain from using artificial tanning devices.</li>
        <li style="font-size: 22px;"><strong>Regular Skin Examinations:</strong>Regular exfoliation can help to remove dead skin cells and reduce bumps.Conduct self-examinations and have regular check-ups with a dermatologist to monitor moles for any changes.</li>
        <li style="font-size: 22px;"><strong>Protective Measures:</strong>Wear wide-brimmed hats, long-sleeved shirts, and UV-blocking sunglasses.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Observation:</strong>Most melanocytic nevi do not require treatment unless they change in appearance or cause discomfort.</li>
        <li style="font-size: 22px;"><strong>Surgical Excision:</strong>: Removal of the mole if it shows signs of potential malignancy or is cosmetically undesirable.</li>
        <li style="font-size: 22px;"><strong>Shave Removal:</strong>Removing the mole by shaving it off at the skin level, often used for raised moles.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Using laser light to remove the mole, though this is less common and typically used for cosmetic purposes.</li>
    </ul>
    </div>       
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\Melanocytic Nevi.png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Benign Melanocytic Nevi')       
            
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