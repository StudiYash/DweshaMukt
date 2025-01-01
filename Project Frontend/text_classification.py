import streamlit as st
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np
import re

# Function to load the model and tokenizer
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

def text_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Text Classification Task</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    user_input = st.text_input("Enter text to classify:")

    if st.button("Predict"):
        if user_input:
            # Check for hateful emoji first
            prediction = has_hateful_emoji(user_input)

            if prediction is None:  # No hateful emoji found, use model prediction
                prediction = load_model_and_predict(user_input)

            # Add rectangle around predicted label
            border_color = 'red' if prediction == 'yes' else 'green'
            st.markdown(f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">Predicted Label: {prediction}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter some text.")

# Define hateful emojis
hateful_emojis = [u'😠', u'😡', u'🤬', u'🥵', u'🤢', u'🤮', u'👿', u'💩', u'👎', u'👎🏻', u'👎🏼', u'👎🏽', u'👎🏾', u'👎🏿', u'🖕', u'🖕🏻', u'🖕🏼', u'🖕🏽', u'🖕🏾', u'🖕🏿', u'👙', u'🩱', u'💦', u'🍌', u'🍑', u'🥊', u'🏴‍☠️']

# Function to check if text contains hateful emojis
def has_hateful_emoji(text):
    for emoji in hateful_emojis:
        if emoji in text:
            return "yes"  # Predict hate if hateful emoji found
    return None  # Return None if no hateful emoji found

if __name__ == '__main__':
    text_classification_function()
