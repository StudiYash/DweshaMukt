import streamlit as st
from googleapiclient.discovery import build
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np

api_key = 'api_key'

# Function to load the model and tokenizer
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

def youtube_comment_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Youtube Video Comment Classification Task</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    # Input container
    with st.form(key='input_form'):
        st.write("Please enter the YouTube video ID and the number of comments to display:")
        video_id = st.text_input("YouTube Video ID:")
        num_comments = st.number_input("Number of comments to display:", min_value=1, value=10)

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Call function to retrieve comments
        comments = video_comments(video_id, num_comments)

        # Display comments and their predicted labels
        st.write("Comments and Predicted Labels:")
        for comment in comments:
            predicted_label = load_model_and_predict(comment)
            # Determine border color based on predicted label
            border_color = 'red' if predicted_label == 'yes' else 'green'
            # Add rectangle around comment with green border and rounded corners
            st.markdown(f'<div style="border: 2px solid pink; border-radius: 10px; padding: 10px; margin-bottom: 10px;">Comment: {comment}</div>', unsafe_allow_html=True)
            # Add rectangle around predicted label with red border and rounded corners
            st.markdown(f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">Predicted Label: {predicted_label}</div>', unsafe_allow_html=True)
            st.write("---")

# Function to retrieve comments from YouTube video
def video_comments(video_id, num_comments=10):
    comments = []

    # creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=num_comments
    ).execute()

    # iterate video response
    for item in video_response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments

if __name__ == '__main__':
    youtube_comment_classification_function()
