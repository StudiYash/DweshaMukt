import streamlit as st
import moviepy.editor as mp
import speech_recognition as sr
import wave
import os
import time
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np

def delete_temporary_files():
    """Delete the temporary video and audio files."""
    temp_video_files = [f for f in os.listdir() if f.startswith("temp_video_") and f.endswith(".mp4")]
    temp_audio_files = [f for f in os.listdir() if f.startswith("temp_audio_") and f.endswith(".wav")]

    for file in temp_video_files + temp_audio_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

def transcribe_video(video_file):
    """Transcribes the audio from a video file.

    Args:
        video_file (streamlit.UploadedFile): The uploaded video file.

    Returns:
        str: The transcribed text from the video's audio.
    """

    # Create temporary files with unique names using os.path.join
    temp_video_file_path = os.path.join(os.getcwd(), "temp_video_" + str(hash(video_file.name)) + ".mp4")
    temp_wav_file_path = os.path.join(os.getcwd(), "temp_audio_" + str(hash(video_file.name)) + ".wav")

    try:
        # Save the video content to a temporary file
        with open(temp_video_file_path, "wb") as f:
            f.write(video_file.read())

        # Load the video and close it explicitly for proper resource management
        video_clip = mp.VideoFileClip(temp_video_file_path)

        # Check video duration
        if video_clip.duration > 120:  # 2 minutes = 120 seconds
            return st.error("The uploaded video must be less than or equal to 4 minutes in duration.")

        # Extract the audio from the video
        audio_clip = video_clip.audio

        # Convert audio to a format suitable for speech recognition
        audio_bytes = audio_clip.to_soundarray()  # Convert audio to numpy array
        audio_samples = (audio_bytes * 32767).astype("int16")  # Convert numpy array to int16

        # Save audio samples to a temporary WAV file using a context manager
        with wave.open(temp_wav_file_path, "wb") as wav_file:
            wav_file.setnchannels(audio_samples.shape[1])  # Set number of channels
            wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
            wav_file.setframerate(audio_clip.fps)  # Set frame rate
            wav_file.writeframes(audio_samples.tobytes())

        # Initialize recognizer
        r = sr.Recognizer()

        # Transcribe audio
        with sr.AudioFile(temp_wav_file_path) as source:
            data = r.record(source)

        # Convert speech to text
        text = r.recognize_google(data)

        return text

    except Exception as e:
        # Handle potential exceptions during processing
        print(f"Error during transcription: {e}")
        return st.error("An error occurred while transcribing the video. Please try again.")

    finally:
        # Ensure temporary files are deleted even if exceptions occur
        for _ in range(5):  # Try to delete the file multiple times with a delay
            try:
                if os.path.exists(temp_video_file_path):
                    os.unlink(temp_video_file_path)
                break  # Exit the loop if deletion is successful
            except PermissionError:
                time.sleep(1)  # Wait for 1 second before retrying deletion

def video_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Video Transcription Classification Task</div>', unsafe_allow_html=True)

    # Delete previous temporary files
    delete_temporary_files()

    # File uploader
    video_file = st.file_uploader("Upload a video file", type=["mp4"])

    if video_file is not None:
        # Display video
        st.video(video_file)

        # Process video and display transcription
        st.markdown("<h2 style='border-radius: 10px; border: 2px solid pink; padding: 10px;'>Transcription:</h2>", unsafe_allow_html=True)
        with st.spinner("Transcribing..."):
            text = transcribe_video(video_file)
        if text:
            st.write(text)
        else:
            st.error("No text recognized.")

        # Load the hate speech classification model and tokenizer
        model_directory = r'hate_speech_model'
        loaded_model = TFBertForSequenceClassification.from_pretrained(model_directory)
        loaded_tokenizer = BertTokenizer.from_pretrained(model_directory)

        # Tokenize and preprocess the transcribed text
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
        predicted_label = "Yes" if predicted_label_id == 1 else "No"

        # Display prediction result
        st.markdown("<h2 style='border-radius: 10px; padding: 10px;'>Prediction:</h2>", unsafe_allow_html=True)
        if predicted_label_id == 1:
            st.write(predicted_label, bg_color="#FFCCCC", color="red")
        else:
            st.write(predicted_label, bg_color="#CCFFCC", color="green")

if __name__ == "__main__":
    video_classification_function()
