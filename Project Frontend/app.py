import streamlit as st
from PIL import Image
import joblib
from transformers import TFBertForSequenceClassification, BertTokenizer
import tensorflow as tf
import numpy as np

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

def main():
    with open("styles.css") as f:
         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.title("Hate Speech Detection in Hinglish")

   

    # Sidebar navigation
    st.sidebar.markdown('<h1 style="text-align: center; font-weight: bold;"><b>Hate Nirikshak</b></h1>', unsafe_allow_html=True)

    # Add margin from the top
    
    # Add image to sidebar
    st.sidebar.image("Hate.jpg", width=300)
    page = st.sidebar.radio("", ["🏠Home", "✅Check Model", "🙎‍♂️About Us"])



    if page == "🏠Home":
        st.markdown('<div class="home-container">', unsafe_allow_html=True)
        
        st.write("**Objective:**")
        st.write("The primary objective of hate speech detection in Hinglish is to develop machine learning models that can accurately identify and classify text as hate speech or non-hate speech. By leveraging natural language processing (NLP) techniques and deep learning models, these systems aim to combat online hate speech and promote a safer and more inclusive online environment.")



        st.markdown('<h4 style="color: pink; text-align: center;">Comprehensive Hate Speech Detection: Addressing Multiple Scenarios and Contexts</h4>', unsafe_allow_html=True)
        
        
        gif_path = "models.gif"
        st.image(gif_path, caption='',width=50, use_column_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

      

    elif page == "✅Check Model":

        # Define the options for the dropdown menu
        options = ["Text Classification", "Audio Classification", "Video Classification", "Image Classification", "GIF Classification", "Youtube Comment Classification"]
        selected_option = st.sidebar.selectbox("Select Classification Task:", options)

        # Execute the selected classification task
        if selected_option == "Text Classification":
            from text_classification import text_classification_function
            text_classification_function()

        elif selected_option == "Audio Classification":
            st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Audio Text Classification Task</div>', unsafe_allow_html=True)
            from audio_classification import audio_classification_function
            audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"]) 
            if audio_file is not None:
                prediction = audio_classification_function(audio_file)
                st.write("Prediction:  ", prediction)
                
        elif selected_option == "Video Classification":
            from video_classification import video_classification_function
            video_classification_function()
        elif selected_option == "Image Classification":
            from image_classification import image_classification_function
            image_classification_function()
        elif selected_option == "GIF Classification":
            from gif_classification import gif_classification_function
            gif_classification_function()
        elif selected_option == "Youtube Comment Classification":
            from youtube_comment_classification import youtube_comment_classification_function
            youtube_comment_classification_function()

    elif page == "🙎‍♂️About Us":

        st.markdown('<div class="about-us-container">', unsafe_allow_html=True)

        st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Meet the Project Team</div>', unsafe_allow_html=True)
        st.write(" ")
        gif_path = "about us.gif"
        st.image(gif_path, caption='',width=50, use_column_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("<h3 style='text-align: center;'>Project Guide : Mr. Rajkumar Panchal</h3>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center;'>Assistant Professor at VPKBIET, Baramati</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: center;'>M.Tech. (Computer Engineering) Ph.D. (Pursuing)</h5>", unsafe_allow_html=True)
       
        # You can add more content related to your team or organization here
        st.markdown('</div>', unsafe_allow_html=True)

    


if __name__ == "__main__":
    main()