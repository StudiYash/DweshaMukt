# Backend Execution 🚀

Welcome to the **Backend Execution** folder of the DweshaMukt project! This folder contains the main backend code, implemented in a Jupyter notebook (`Project Backend.ipynb`), for performing hate speech detection on various input types (text, audio, image, GIF, video, and YouTube comments). The code integrates multiple Google APIs and deep learning models to classify inputs as hate or non-hate speech.

## Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Code](#running-the-code)
- [Supported Input Types](#supported-input-types)
- [Important Notes](#important-notes)

---

## Requirements

Before running the notebook, ensure you have the following:
- **Google Colab** environment or a local machine with Python 3.10.
- **Google Cloud API Keys** for:
  - **Speech-to-Text** (for audio transcription)
  - **Vision API** (for image text extraction)
  - **Video Intelligence API** (for video and GIF text extraction)
- **Google Colab Drive Access** to mount the project folder in Colab.
- **Internet Connection** to install dependencies and access APIs.

## Setup Instructions

1. **Install Dependencies**  
   The notebook installs several libraries required for the project. Run the following commands in a Colab cell if you're working locally, or they will automatically execute in the notebook:

   ```python
   !pip install pandas numpy scikit-learn tensorflow transformers google-cloud-speech google-cloud-videointelligence google-cloud-vision moviepy pytchat joblib

   !apt install python3.10-venv

   !pip install --upgrade ffmpeg
   ```

2. **Google Cloud Authentication :**
- You need to authenticate for each API used in the project (Speech-to-Text, Vision, and Video Intelligence).
- Place your Google Cloud JSON key files in the project directory and specify the paths in the code for each API.
- Update these lines in the code to match the paths to your credential files:

    ```python
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/path/to/your/credentials1.json"  # For Speech-to-Text
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/path/to/your/credentials2.json"  # For Vision API
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/path/to/your/credentials3.json"  # For Video Intelligence API
    ```

3. **Mount Google Drive (for Colab users) :**
- If running in Google Colab, you can mount your Google Drive to access the files:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. **Load Model and Assets :**
- Ensure that the following files are placed in the project directory:
    - tf_model.h5: The trained TensorFlow model file.
    - label_encoder.pkl: The label encoder for mapping predictions.
    - vocab.txt, config.json, tokenizer_config.json, special_tokens_map.json: Configuration files for the tokenizer.

## Running the Code

To run the code:

1. **Open the Notebook :**
- Launch `Project Backend.ipynb` in Google Colab or Jupyter Notebook.

2. **Follow the Prompts:**
- The code includes a prompt-based system. After running the cell, you will be prompted to select one of the six input types:
    - **Text:** Enter a text sentence to classify.
    - **Audio:** Upload an audio file in MP3 format for transcription and classification.
    - **Image:** Upload an image file (JPEG/PNG) to extract text and classify.
    - **GIF:** Upload a GIF file to extract text from frames and classify.
    - **Video:** Upload a video file to analyze both audio and text content.
    - **YouTube:** Enter a YouTube live stream video ID to classify live comments.

3. **Scenario Selection and Input :**
- Based on the scenario, the system will guide you through the input process.
- The system then processes the input, applies the hate speech detection model, and returns the classification result.

## Supported Input Types

This backend execution supports six input types for hate speech detection:
- **Text:** Direct input through a text prompt.
- **Audio:** Uploaded MP3 audio file, converted to text via Google Speech-to-Text API.
- **Image:** Uploaded image file, with text extracted via Google Vision API.
- **GIF:** Uploaded GIF file, with text extracted frame-by-frame using Google Video Intelligence API.
- **Video:** Uploaded video file, analyzed for both audio transcription and text extraction.
- **YouTube Comments:** Real-time analysis of live YouTube comments, using the video’s live stream ID.

## Important Notes

- **Device Compatibility:** The model predictions are executed on the CPU to ensure compatibility across different systems.
- **API Rate Limits:** Be aware of the Google Cloud API rate limits, especially when testing multiple inputs.
- **Timeouts:** For live YouTube comments, the system has a timeout of 3 seconds to avoid excessive API requests.
- **Emoji Handling:** The model has an inbuilt mechanism to detect certain hateful emojis. If a hateful emoji is found in the text, the content is directly classified as hate speech.

> *This backend setup is optimized for testing in Google Colab. Running it on a local system may require additional configuration for API authentication and environment setup.*

---

**Happy testing, and thank you for using DweshaMukt!**