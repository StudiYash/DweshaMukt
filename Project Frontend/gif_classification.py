import os
from google.cloud import videointelligence_v1p3beta1 as videointelligence
from google.cloud.videointelligence_v1p3beta1.types import Feature, VideoContext, TextDetectionConfig
import streamlit as st
from PIL import Image
import pytesseract as tess
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np

# Set Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\Tanmay Nigade\Downloads\Hate Speech Hinglish Laguage\noted-casing-413617-bb0c110a54de.json'

# Set Tesseract path
tess.pytesseract.tesseract_cmd = r'C:\Users\Tanmay Nigade\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to load the model and make prediction for hate speech
def load_model_and_predict(text):
    model_directory = r'C:\Users\Tanmay Nigade\Downloads\Hate Speech Hinglish Laguage\hate_speech_model'
    loaded_model = TFBertForSequenceClassification.from_pretrained(model_directory)
    loaded_tokenizer = BertTokenizer.from_pretrained(model_directory)

    # Load the TensorFlow model
    tf_model_filename = r'C:\Users\Tanmay Nigade\Downloads\Hate Speech Hinglish Laguage\tf_model.h5'
    loaded_model.load_weights(tf_model_filename)

    # Load the label encoder
    label_encoder_filename = r'C:\Users\Tanmay Nigade\Downloads\Hate Speech Hinglish Laguage\label_encoder.pkl'
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

# Function to analyze GIF for text detection
def analyze_gif_text_detection(gif_content):
    client = videointelligence.VideoIntelligenceServiceClient()

    # Configure the request
    features = [Feature.TEXT_DETECTION]
    config = TextDetectionConfig(language_hints=["en"])
    context = VideoContext(text_detection_config=config)

    request = videointelligence.AnnotateVideoRequest(
        input_content=gif_content,
        features=features,
        video_context=context
    )

    # Execute the request
    operation = client.annotate_video(request)  # Start long-running operation
    print("Started text detection operation. Waiting for results...")
    results = operation.result(timeout=300)  # Wait for results (with timeout)

    # Get and concatenate the extracted text from the GIF frames
    extracted_text = ""
    for annotation_result in results.annotation_results:
        for text_annotation in annotation_result.text_annotations:
            extracted_text += text_annotation.text + " "

    return extracted_text.strip()

# Streamlit app
def gif_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">GIF Text Classification Task</div>', unsafe_allow_html=True)


    # File uploader for GIF
    uploaded_file = st.file_uploader("Upload a GIF", type=["gif"])

    if uploaded_file is not None:
        # Display the uploaded GIF
        st.subheader("Uploaded GIF")
        st.image(uploaded_file, use_column_width=True)

        # Analyze the GIF for text detection
        extracted_text = analyze_gif_text_detection(uploaded_file.read())

        # Apply HTML/CSS styling for the rectangle around the extracted text
        styled_text = f'<div style="border: 2px solid yellow; border-radius: 10px; padding: 10px;">{extracted_text}</div>'
        
        # Display the extracted text with styling
        st.subheader("Extracted Text from GIF")
        st.write(styled_text, unsafe_allow_html=True)

        # Predict if the extracted text contains hate speech
        predicted_label = load_model_and_predict(extracted_text)

        # Determine border color based on predicted label
        border_color = 'red' if predicted_label == 'yes' else 'green'

        # Apply CSS styling for the predicted label rectangle
        styled_label = f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">Hate Speech Prediction: {predicted_label}</div>'
        st.subheader("Hate Speech Prediction")
        st.write(styled_label, unsafe_allow_html=True)

if __name__ == "__main__":
    gif_classification_function()
