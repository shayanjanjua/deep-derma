import streamlit as st
from PIL import Image
import ActinicKeratoses, BasalCellCarcinoma, BenignKeratoses, Dermatofibroma, Melanoma, MelanocyticNevi, VascularMalformations
import base64

# Function to load and encode an image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Add navigation buttons
        st.markdown("<h1 style='color: Black;'>Predicted Disease By Deep Derma</h1>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Actinic Keratoses"):
                self.apps[0]["function"]()
            if st.button("Basal Cell Carcinoma"):
                self.apps[1]["function"]()
            if st.button("Benign Keratoses"):
                self.apps[2]["function"]()
        
        with col2:
            if st.button("Dermatofibroma"):
                self.apps[3]["function"]()
            if st.button("Melanoma"):
                self.apps[4]["function"]()
            if st.button("Melanocytic Nevi"):
                self.apps[5]["function"]()
        
        with col3:
            if st.button("Vascular Malformations"):
                self.apps[6]["function"]()

# Create instance of MultiApp class
multi_app = MultiApp()

# Add apps
multi_app.add_app("ActinicKeratoses", ActinicKeratoses.app)
multi_app.add_app("BasalCellCarcinoma", BasalCellCarcinoma.app)
multi_app.add_app("BenignKeratoses", BenignKeratoses.app)
multi_app.add_app("Dermatofibroma", Dermatofibroma.app)
multi_app.add_app("Melanoma", Melanoma.app)
multi_app.add_app("MelanocyticNevi", MelanocyticNevi.app)
multi_app.add_app("VascularMalformations", VascularMalformations.app)

# Run the MultiApp
multi_app.run()
