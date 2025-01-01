import streamlit as st
import pytesseract as tess
from PIL import Image
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np
import re

# Set Tesseract path
tess.pytesseract.tesseract_cmd = r'C:\Users\Username\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to load the model and make prediction
def load_model_and_predict(text):
    model_directory = r'hate_speech_model'
    loaded_model = TFBertForSequenceClassification.from_pretrained(model_directory)
    loaded_tokenizer = BertTokenizer.from_pretrained(model_directory)

    # Load the TensorFlow model
    tf_model_filename = r'tf_model.h5'
    loaded_model.load_weights(tf_model_filename)

    # Load the label encoder
    label_encoder_filename = r'label_encoder.pkl'
    loaded_label_encoder = joblib.load(label_encoder_filename)

    # Tokenize and preprocess the input text
    encoding = loaded_tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )

    input_ids = encoding['input_ids']
    attention_mask = encoding['attention_mask']

    # Make prediction
    with tf.device('/cpu:0'):  # Ensure predictions are made on CPU
        outputs = loaded_model.predict([input_ids, attention_mask])
        logits = outputs.logits

    # Convert logits to probabilities and get the predicted label
    probabilities = tf.nn.softmax(logits, axis=1).numpy()[0]
    predicted_label_id = np.argmax(probabilities)
    predicted_label = loaded_label_encoder.classes_[predicted_label_id]

    return predicted_label

# Function to apply CSS styling for the rectangle
def get_css_styles():
    css = """
    <style>
    .extracted-text-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
    }
    .predicted-label-box {
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
    }
    </style>
    """
    return css

# Function to perform image classification
def image_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Image Text Classification Task</div>', unsafe_allow_html=True)

    # File uploader for image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image with adjusted size
        img = Image.open(uploaded_image)  # Process image data directly
        img_width = 300  # Specify desired width for the displayed image
        st.image(img, caption='Uploaded Image', use_column_width=True, width=img_width)

        # Perform text extraction
        extracted_text = tess.image_to_string(img)
        
        # Apply CSS styling for the rectangle around extracted text
        css_styles = get_css_styles()
        st.markdown(css_styles, unsafe_allow_html=True)
        
        # Display the extracted text inside a rectangle
        st.markdown(f'<div class="extracted-text-box">{extracted_text}</div>', unsafe_allow_html=True)

        # Perform hate speech classification
        predicted_label = load_model_and_predict(extracted_text)
        
        # Determine border color based on predicted label
        #border_color = "green" if predicted_label == "Yes" else "red"
        border_color = 'red' if predicted_label == 'yes' else 'green'
        # Apply CSS styling for the predicted label
        predicted_label_css = f"""
            <style>
            .predicted-label-box {{
                border: 2px solid {border_color};
            }}
            </style>
            """
        st.markdown(predicted_label_css, unsafe_allow_html=True)
        
        # Display the predicted label inside a rectangle
        st.markdown(f'<div class="predicted-label-box">Predicted Label: {predicted_label}</div>', unsafe_allow_html=True)

# Streamlit app
def main():
    image_classification_function()

if __name__ == "__main__":
    main()
