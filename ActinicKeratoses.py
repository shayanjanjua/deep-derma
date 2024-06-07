import streamlit as st
from PIL import Image

def app():
    st.markdown("""
    <h1 style='color: Black;'>Actinic Keratoses</h1> 
            <p style="font-family: Arial, sans-serif; font-size: 22px; line-height: 1.6; color: #333333;">
           Actinic Keratoses (AK) are rough, scaly patches on the skin caused by excessive exposure to ultraviolet (UV) light. 
            They are considered precancerous because they can develop into skin cancer if untreated.
        </p>
          
            
    <h2 style='color: Black;'>Symptoms</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;">Rough, dry, or scaly patch of skin, typically less than 1 inch in diameter.</li>
        <li style="font-size: 22px;">Flat to slightly raised patch or bump on the top layer of skin.</li>
        <li style="font-size: 22px;">Hard, wart-like surface.</li>
        <li style="font-size: 22px;">Color variations: pink, red, or brown.</li>
        <li style="font-size: 22px;">Itching or burning in the affected area.</li>
    </ul>
    </div>       
               

    <h2 style='color: Black;'>Causes</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>UV Exposure:</strong>Prolonged exposure to ultraviolet (UV) radiation from the sun or tanning beds.</li>
        <li style="font-size: 22px;"><strong>Skin Type:</strong>Fair skin, light-colored hair, and blue, green, or hazel eyes.</li>
        <li style="font-size: 22px;"><strong>Age:</strong>More common in people over 40.</li>
        <li style="font-size: 22px;"><strong>Geography:</strong>Living in sunny climates or at high altitudes.</li>
        <li style="font-size: 22px;"><strong>Immunosuppression:</strong>Weakened immune system, such as from cancer chemotherapy, AIDS, or organ transplantation.</li>
    </ul>
    </div>   
            
    <h2 style='color: Black;'>Prevention</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Sun Protection:</strong>Use sunscreen with a high SPF, wear protective clothing, and avoid the sun during peak hours.</li>
        <li style="font-size: 22px;"><strong>Avoid Tanning Beds:</strong>Refrain from using artificial tanning devices.</li>
        <li style="font-size: 22px;"><strong>Regular Skin Checks:</strong>Conduct self-examinations and see a dermatologist regularly for skin evaluations.</li>
        <li style="font-size: 22px;"><strong>•Protective Clothing:</strong>Wear wide-brimmed hats, long sleeves, and sunglasses.</li>
    </ul>
    </div>   
            

    <h2 style='color: Black;'>Treatment</h2>
    <div style="background-color: rgba(255, 255, 255, 0.7); padding: 10px; border: 4px solid black; border-radius: 10px;">          
    <ul>
        <li style="font-size: 22px;"><strong>Cryotherapy:</strong>Freezing the lesion with liquid nitrogen.</li>
        <li style="font-size: 22px;"><strong>Topical Treatments:</strong>Prescription creams or gels, such as 5-fluorouracil (5-FU), imiquimod, or diclofenac.</li>
        <li style="font-size: 22px;"><strong>Photodynamic Therapy (PDT):</strong>Applying a light-sensitive solution to the skin and then exposing it to a special light.</li>
        <li style="font-size: 22px;"><strong>Laser Therapy:</strong>Using lasers to remove the affected skin.</li>
    </ul>
    </div>       
    """, unsafe_allow_html=True)

    # Add the image after the treatment section
    image_path = r'IMAGES/ACtinic Keratoses .png' # Replace with your image path
    image = Image.open(image_path)
    st.image(image, caption='Example of Actinic Keratoses Treatment')    


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
