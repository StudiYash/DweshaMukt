import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import mediainfo
import io
import tempfile
import os
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np

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

def audio_classification_function(audio_file):
    
    # Function to convert audio to WAV format
    def convert_audio_to_wav(audio_file):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name

        audio_info = mediainfo(temp_file_path)
        audio_format = audio_info.get('format_name', None)

        if audio_format and audio_format.lower() != 'wav':
            audio = AudioSegment.from_file(temp_file_path)
            audio = audio[:120000]  # Take the first 1 minute of audio
            converted_file_path = temp_file_path + ".wav"
            audio.export(converted_file_path, format='wav')
            return converted_file_path
        else:
            return temp_file_path

    # Function to recognize speech from audio file
    def recognize_speech(audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return 'Sorry, the speech could not be understood.'
            except sr.RequestError as e:
                return f"Could not request results from Google Speech Recognition service; {e}"

    # Convert and recognize speech
    converted_file = convert_audio_to_wav(audio_file)
    text = recognize_speech(converted_file)

    # Delete the temporary file
    os.remove(converted_file)

    # Predict hate speech based on the transcription
    if text:
        prediction = load_model_and_predict(text)
        return text, prediction
    else:
        return None, None

def main():
    st.title("Speech to Text and Hate Speech Detection")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        text, prediction = audio_classification_function(uploaded_file)

        if text is not None:
            st.write('Transcription:')
            st.write(text)

            # Display the audio file
            st.audio(uploaded_file, format='audio/wav')
            

            # Display prediction with red border for "Yes" and green border for "No"
            if prediction == "Yes":
                st.markdown(
                    f'<div style="border: 2px solid red; border-radius: 5px; padding: 10px;">'
                    f'<h3 style="color: red;">Prediction: {prediction}</h3>'
                    f'</div>',
                    unsafe_allow_html=True
                )
            elif prediction == "No":
                st.markdown(
                    f'<div style="border: 2px solid green; border-radius: 5px; padding: 10px;">'
                    f'<h3 style="color: green;">Prediction: {prediction}</h3>'
                    f'</div>',
                    unsafe_allow_html=True
                )
        else:
            st.write('Sorry, the speech could not be understood.')

if __name__ == "__main__":
    main()
