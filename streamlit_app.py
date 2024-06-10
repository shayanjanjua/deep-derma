import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import Home, About, Faqs, Contact, Account, Demo
import ActinicKeratoses, BasalCellCarcinoma, BenignKeratoses, Dermatofibroma, Melanoma, MelanocyticNevi, VascularMalformations

# Load the main image
image = Image.open(r'IMAGES/DEEP DERMA LOGO.png')

# Function to load and encode an image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load and encode the sidebar background image
sidebar_image_path = r'IMAGES/sidebar image.png'
sidebar_img_base64 = get_base64_of_bin_file(sidebar_image_path)

# Set page config with the loaded image as the icon
st.set_page_config(
    page_title="DEEP DERMA",
    page_icon=image,
)

# Add custom CSS for sidebar background
try:
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
except Exception as e:
    st.error(f"An error occurred: {e}")

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
                options=['HOME', 'ABOUT', 'TRY IT', 'ACCOUNT', 'CONTACT', 'FAQ'],
                icons=['house-fill', 'book-fill', 'bi bi-play', 'bi bi-person-circle', 'bi-phone-fill', 'bi-question-circle-fill'],
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

# Run the MultiApp
multi_app.run()
