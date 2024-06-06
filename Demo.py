import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os
import torch
from torchvision import transforms
import base64
from ultralytics import YOLO

# Define the base directory where your models are stored
BASE_DIR = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\shayan'
MODEL_NAME = 'shay.pt'
MODEL_PATH = os.path.join(BASE_DIR, MODEL_NAME)

# Define the labels path and name
LABELS_PATH = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\labelsname.txt'

# Function to load the YOLO model
def load_yolo_model(model_path):
    try:
        # Load the YOLOv8 model
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"An error occurred while loading the model: {str(e)}")
        return None

# Function to load labels
def load_labels(labels_path):
    try:
        with open(labels_path, 'r') as file:
            labels = file.read().splitlines()
        return labels
    except Exception as e:
        st.error(f"An error occurred while loading the labels: {str(e)}")
        return None

# Function to preprocess the image
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((640, 640)),
        transforms.ToTensor(),
    ])
    return transform(image).unsqueeze(0)

# Function to perform object detection using the YOLO model
def detect_objects_yolo(image, model):
    # Convert the image to OpenCV format (BGR)
    image_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Perform inference
    results = model(image_cv2)
    
    return results

# Function to draw bounding boxes on the image and label them
def draw_bounding_boxes(image, results, labels, confidence_threshold=0.5):
    # Extract the predictions
    predictions = results[0].boxes  # Get the boxes from the first result

    # Loop through each prediction
    for pred in predictions:
        confidence = pred.conf.item()
        if confidence > confidence_threshold:
            x1, y1, x2, y2 = map(int, pred.xyxy[0].tolist())
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            class_id = int(pred.cls)
            label = f"{labels[class_id]}: {confidence:.2f}" if class_id < len(labels) else f"Unknown: {confidence:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return image

# Function to set the background image
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function for the Streamlit app
def app():
    # Set the background image
    set_background(r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\background image deep dermaa.jpg')  # Use raw string

    st.markdown("<h1 style='color: white;'>Try It</h1>", unsafe_allow_html=True)

    # Load model
    model = load_yolo_model(MODEL_PATH)

    # Load labels
    labels = load_labels(LABELS_PATH)

    if labels is not None:
        st.markdown("""          
    <div style="background-color: white; border: 4px solid green; border-radius: 10px; padding: 10px;">
    (Labels loaded successfully!)
    </div>
    """, unsafe_allow_html=True)
        
    if model is not None:
        st.markdown("""          
    <div style="background-color: white; border: 4px solid green; border-radius: 10px; padding: 10px;">
    (Model loaded successfully!)
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("<h1 style='color: white;'>Fill This Form Out</h1>", unsafe_allow_html=True)
    
    with st.form("questionnaire_form"):
        # Wrap the form in a div with specified styling

        # QUESTIONS 
        st.markdown(
            '''
                <h3 style="color:White; margin-bottom: 10px;">1. Do you have any known allergies? (Select all that apply)</h3>
            ''',
            unsafe_allow_html=True
        )

        allergies_options = ["None", "Medications", "Skincare products", "Substances (e.g., latex, nickel)", "Foods", "Other"]
        allergies = st.multiselect("", allergies_options)

        if "Other" in allergies:
            other_allergies = st.text_input("Please specify other allergies:")

        st.markdown(
            '''
                <h3 style="color:White; margin-bottom: 10px;">2. Have you been previously diagnosed with any of the following skin conditions? (Select all that apply)</h3>
            ''',
            unsafe_allow_html=True
        )

        skin_conditions_options = ["None", "Eczema", "Psoriasis", "Rosacea", "Acne", "Melanoma", "Basal Cell Carcinoma", "Other"]
        skin_conditions = st.multiselect("", skin_conditions_options)

        if "Other" in skin_conditions:
            other_skin_conditions = st.text_input("Please specify other skin conditions:")

        st.markdown(
            '''
                <h3 style="color:White; margin-bottom: 10px;">3. Are you currently experiencing any of the following symptoms in the affected area? (Select all that apply)</h3>
            ''',
            unsafe_allow_html=True
        )

        symptoms_options = ["None", "Itching", "Redness", "Swelling", "Pain", "Dryness/Scaling", "Blisters/Pustules", "Other"]
       
        symptoms = st.multiselect("", symptoms_options)

        if "Other" in symptoms:
            other_symptoms = st.text_input("Please specify other symptoms:")

        st.markdown(
            '''
                <h3 style="color:White; margin-bottom: 10px;">4. Have you recently started using any new skincare products, medications, or undergone any medical treatments? (Select all that apply)</h3>
            ''',
            unsafe_allow_html=True
        )

        recent_treatments_options = ["No", "Yes, new skincare products", "Yes, new medications", "Yes, recent medical treatments", "Other"]
        recent_treatments = st.multiselect("", recent_treatments_options)

        if "Other" in recent_treatments:
            other_treatments = st.text_input("Please specify other treatments:")

        st.markdown(
            '''
                <h3 style="color:White; margin-bottom: 10px;">5. Do you have any family history of the following skin diseases? (Select all that apply)</h3>
            ''',
            unsafe_allow_html=True
        )

        family_history_options = ["None", "Eczema", "Psoriasis", "Skin cancer (e.g., melanoma, basal cell carcinoma)", "Other"]
        family_history = st.multiselect("", family_history_options)

        if "Other" in family_history:
            other_family_history = st.text_input("Please specify other family history of skin diseases:")

        st.markdown("</div>", unsafe_allow_html=True)

        # Add custom CSS for the submit button
        st.markdown("""
            <style>
            .stButton button {
                background-color: white; /* White background */
                color: black; /* Black text */
                border: 2px solid #4CAF50; /* Green border */
                padding: 10px 24px; /* Some padding */
                border-radius: 10px; /* Rounded corners */
                cursor: pointer; /* Pointer/hand icon */
                font-size: 16px; /* Increase font size */
            }
            .stButton button:hover {
                background-color: #CCE2EB; /* Green background on hover */
                color: white; /* White text on hover */
            }
            </style>
        """, unsafe_allow_html=True)

        # Add a submit button to the form
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form submitted successfully!")

    # Upload file option
    st.markdown('<h1 style="color:White;">Upload Image for Detection</h1>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Check if the "Predict" button is clicked
        if st.button("Predict"):
            # Perform object detection if model loaded successfully
            if model is not None and labels is not None:
                results = detect_objects_yolo(image, model)
                if results is not None:
                    # Convert image to array format for drawing bounding boxes
                    image_np = np.array(image)
                    # Draw bounding boxes on the image
                    image_with_boxes = draw_bounding_boxes(image_np, results, labels)

                    # Display the image with detected objects
                    st.image(image_with_boxes, caption="Detected Objects", use_column_width=True)
                else:
                    st.error("Object detection could not be performed due to an error.")
            else:
                st.error("Model or labels not loaded. Please check the model file path and labels file path and try again.")

if __name__ == "__main__":
    app()
