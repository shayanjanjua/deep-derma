import torch
import pickle

# Load the model from the pickle file
def load_model_from_pickle(pickle_file):
    try:
        with open(pickle_file, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print(f"An error occurred while loading the model from pickle: {str(e)}")
        return None

# Convert the model to PyTorch format and save it
def convert_and_save_model(pickle_file, output_file):
    # Load the model from pickle
    model = load_model_from_pickle(pickle_file)
    if model is not None:
        try:
            # Save the model as PyTorch format
            torch.save(model, output_file)
            print(f"Model converted and saved successfully as '{output_file}'.")
        except Exception as e:
            print(f"An error occurred while saving the model: {str(e)}")
    else:
        print("Model could not be loaded from pickle. Conversion aborted.")

# Specify the paths for the pickle file and the output PyTorch file
pickle_file = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\yolo_model.pkl'  # Replace with the path to your pickle file
output_file = r'C:\Users\Shayan\Desktop\FYP\DEEP DERMA APP\yolo_model.pt'  # Replace with the desired output file path

# Convert and save the model
convert_and_save_model(pickle_file, output_file)
