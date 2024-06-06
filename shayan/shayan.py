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
BASE_DIR = r'C:\Users\Shayan\Desktop\FYP\HAM 10000\shayan'
MODEL_NAME = 'shay.pt'
MODEL_PATH = os.path.join(BASE_DIR, MODEL_NAME)

# Define the labels path and name
LABELS_PATH = r'C:\Users\Shayan\Desktop\FYP\HAM 10000\shayan\cab.txt'

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
    st.title("Object Detection")

    # Set the background image (optional)
    # set_background(r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\IMAGES\Default_Design_an_engaging_and_visually_appealing_background_i_3 (1).jpg')  # Use raw string

    # Load model
    model = load_yolo_model(MODEL_PATH)

    if model is not None:
        st.success("Model loaded successfully!")
    
    # Load labels
    labels = load_labels(LABELS_PATH)

    if labels is not None:
        st.success("Labels loaded successfully!")

    # Upload file option
    st.markdown('<h1 style="color:white;">Upload Image for Object Detection</h1>', unsafe_allow_html=True)
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
