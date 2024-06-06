import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from streamlit_lottie import st_lottie
import json

# Use double backslashes or forward slashes in the file path
cred = credentials.Certificate('deep-derma-66a2657a04f6.json')

# Check if Firebase app is already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Load the Lottie animation file from the local file system
animation_path = r"ANIMATIONS/loading.json"
with open(animation_path, "r") as f:
    animation_data = json.load(f)

def home():
    st.title("Home Page")
    st.write("Welcome to Deep Derma!")

def app():
    # Center align the animation
    st.markdown(
        """
        <style>
        .center {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display animation at the top of the page
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st_lottie(animation_data, speed=1, reverse=False, loop=True, quality="low", height=200, width=200, key=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.title("LOGIN/SIGNUP")

    choice = st.selectbox("Login/Signup", ['Login', 'Sign Up'])

    def login():
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            try:
                user = auth.get_user_by_email(email)
                st.write('Login Successful')
                st.experimental_rerun()  # Reload the app
            except Exception as e:
                st.warning('Login Failed: {}'.format(e))

    def signup():
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        username = st.text_input("Enter your unique username")
        if st.button("Create my account"):
            try:
                user = auth.create_user(email=email, password=password, uid=username)
                st.success("Account created successfully!")
                st.markdown("Please login using email or password")
            except Exception as e:
                st.warning('Signup Failed: {}'.format(e))

    if choice == 'Login':
        login()
    else:
        signup()

# Run the app
app()
