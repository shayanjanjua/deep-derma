import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import Home, About, Faqs, Contact, Account, Demo
import ActinicKeratoses, BasalCellCarcinoma, BenignKeratoses, Dermatofibroma, Melanoma, MelanocyticNevi, VascularMalformations

# Load the main image
img = Image.open(r'IMAGES/DEEP DERMA LOGO.png')

# Function to load and encode an image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load and encode the sidebar background image
sidebar_image_path = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\sidebar image.png'
sidebar_img_base64 = get_base64_of_bin_file(sidebar_image_path)

# Set page config with the loaded image as the icon
st.set_page_config(
    page_title="DEEP DERMA",
    page_icon=img,
)

# Add custom CSS for sidebar background
st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background-image: url('data:image/jpg;base64,{sidebar_img_base64}');
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Add sidebar menu
        with st.sidebar:
            # Option menu in sidebar
            app = option_menu(
                menu_title='Deep Derma',
                options=['HOME', 'ABOUT', 'TRY IT', 'DISEASE PREDICTIONS', 'ACCOUNT', 'CONTACT', 'FAQ'],
                icons=['house-fill', 'book-fill', 'bi bi-play', 'bi-activity', 'bi bi-person-circle', 'bi-phone-fill', 'bi-question-circle-fill'],
                menu_icon='none',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#4592DF'},
                    "icon": {"color": "White", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#CCE2EB"},
                    "nav-link-selected": {"background-color": "#020202"},
                }
            )

        # Run selected app
        for app_data in self.apps:
            if app_data["title"] == app:
                app_data["function"]()

# Create instance of MultiApp class
multi_app = MultiApp()

# Add apps to the main MultiApp instance
multi_app.add_app("HOME", Home.app)
multi_app.add_app("ABOUT", About.app)
multi_app.add_app("TRY IT", Demo.app)
multi_app.add_app("ACCOUNT", Account.app)
multi_app.add_app("CONTACT", Contact.app)
multi_app.add_app("FAQ", Faqs.app)

# Add apps for disease predictions
def show_disease_predictions():
    disease_app = MultiApp()
    disease_app.add_app("ActinicKeratoses", ActinicKeratoses.app)
    disease_app.add_app("BasalCellCarcinoma", BasalCellCarcinoma.app)
    disease_app.add_app("BenignKeratoses", BenignKeratoses.app)
    disease_app.add_app("Dermatofibroma", Dermatofibroma.app)
    disease_app.add_app("Melanoma", Melanoma.app)
    disease_app.add_app("MelanocyticNevi", MelanocyticNevi.app)
    disease_app.add_app("VascularMalformations", VascularMalformations.app)
    
    st.markdown("<h1 style='color: Black;'>Select Disease that is Predicted By Deep Derma</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Actinic Keratoses"):
            st.session_state.selected_app = "ActinicKeratoses"
        if st.button("Basal Cell Carcinoma"):
            st.session_state.selected_app = "BasalCellCarcinoma"
        if st.button("Benign Keratoses"):
            st.session_state.selected_app = "BenignKeratoses"
    
    with col2:
        if st.button("Dermatofibroma"):
            st.session_state.selected_app = "Dermatofibroma"
        if st.button("Melanoma"):
            st.session_state.selected_app = "Melanoma"
        if st.button("Melanocytic Nevi"):
            st.session_state.selected_app = "MelanocyticNevi"
    
    with col3:
        if st.button("Vascular Malformations"):
            st.session_state.selected_app = "VascularMalformations"
    
    if 'selected_app' in st.session_state:
        for app_data in disease_app.apps:
            if app_data["title"] == st.session_state.selected_app:
                app_data["function"]()

multi_app.add_app("DISEASE PREDICTIONS", show_disease_predictions)

# Run the MultiApp
multi_app.run()
