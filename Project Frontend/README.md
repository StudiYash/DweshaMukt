# Project Frontend 💫

Welcome to the **Project Frontend** folder of the DweshaMukt project! This folder contains the main frontend code for implementing the hate speech detection project as an interactive **Streamlit App**. The app allows users to upload and classify text, audio, images, GIFs, and videos, as well as analyze live YouTube comments.

---

## Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [File and Path Changes](#file-and-path-changes)
- [Important Notes](#important-notes)
- [Watch in Action](#watch-frontend-in-action)

---

## Requirements

Ensure you have the following before proceeding:

1. **VS Code**: Open the entire **Project Frontend** folder in Visual Studio Code.
2. **Tesseract Software**: Download and install Tesseract OCR software.
3. **Google Cloud API Credentials**: JSON files for Speech-to-Text, Vision, and Video Intelligence APIs.
4. **Backend Files**: Download the following from the **Project Backend** folder:
    - Model directory: `hate_speech_model`
    - `tf_model.h5` (TensorFlow model weights)
    - `label_encoder.pkl` (Label encoder file)
5. **Python Environment**: Python 3.10 installed with all required libraries.
6. **Streamlit Configuration**: Add a `config.toml` file in your local Streamlit folder.

---

## Setup Instructions

1. **File Setup and Path Changes**:
    - Open the **Project Frontend** folder in **VS Code**.
    - Update the following paths in the respective files:

        **`Inside All .py Files`**:
      ```python
      model_directory = r'D:\Hate Speech Detection in Hinglish Language\hate_speech_model'
      loaded_model = TFBertForSequenceClassification.from_pretrained(model_directory)
      loaded_tokenizer = BertTokenizer.from_pretrained(model_directory)

      # Load the TensorFlow model
      tf_model_filename = r'D:\Hate Speech Detection in Hinglish Language\tf_model.h5'
      loaded_model.load_weights(tf_model_filename)

      # Load the label encoder
      label_encoder_filename = r'D:\Hate Speech Detection in Hinglish Language\label_encoder.pkl'
      loaded_label_encoder = joblib.load(label_encoder_filename)
      ```

      **`image_classification.py`**:
      ```python
      # Set Tesseract path
      tess.pytesseract.tesseract_cmd = r'C:\Users\UserName\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
      ```

      **`gif_classification.py`**:
      ```python
      # Set Google Cloud credentials environment variable
      os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'D:\Hate Speech Detection in Hinglish Language\noted-casing-413617-bb0c110a54de.json'
      ```

2. **Install Required Libraries**:
    - Install dependencies by running the following command in the terminal:
      ```bash
      pip install -r frontend_requirement.txt
      ```

3. **Add `config.toml` File**:
    - Add a `config.toml` file to your Streamlit folder. The usual path for the Streamlit folder is:
      ```
      C:\Users\<YourUserName>\.streamlit\config.toml
      ```

4. **Run the Streamlit App**:
    - Launch the app using the following command in the terminal:
      ```bash
      streamlit run app.py
      ```

---

## File and Path Changes

Ensure all the files and paths are correctly set according to your folder structure:

- **Model Directory**: Path to the `hate_speech_model` folder.
- **Tesseract OCR Path**: Path to the installed Tesseract executable.
- **Google Cloud Credentials**: Path to your JSON key files for API authentication.
- **Streamlit Config File**: Path to the Streamlit `config.toml` file.

---

## Important Notes

1. **Backend Dependency**: Ensure the backend files are correctly downloaded and paths updated as required.
2. **Streamlit Folder**: The `config.toml` file must be placed in the appropriate Streamlit folder for proper configuration.
3. **Tesseract Installation**: Ensure Tesseract OCR is installed and its path correctly specified.
4. **API Rate Limits**: Be mindful of Google Cloud API quotas while testing multiple inputs.
5. **Testing**: Perform thorough testing of the Streamlit app to verify compatibility with all supported input types.

---

## Watch Frontend in Action

| Bot Name          | Description                              | Watch in Action |
|-------------------|------------------------------------------|-----------------|
| **Text Frontend**    | Processes text input.                    | [![Watch Text Frontend](https://img.shields.io/badge/Watch-Text%20Frontend-white?style=for-the-badge&logo=YouTube)](https://youtu.be/sj4sloqjrp0?si=9-aDAUwBaCw2TtWJ) |
| **Audio Frontend**   | Processes audio input.                   | [![Watch Audio Frontend](https://img.shields.io/badge/Watch-Audio%20Frontend-magenta?style=for-the-badge&logo=YouTube)](https://youtu.be/qLkZnnZxUIs?si=g-chiiKRytZ7oETw) |
| **Image Frontend**   | Processes image input.                   | [![Watch Image Frontend](https://img.shields.io/badge/Watch-Image%20Frontend-indigo?style=for-the-badge&logo=YouTube)](https://youtu.be/8qrNRBQR9eE?si=qirdFIe6XV4F9MfH) |
| **GIF Frontend**     | Processes GIF input.                     | [![Watch GIF Frontend](https://img.shields.io/badge/Watch-GIF%20Frontend-gold?style=for-the-badge&logo=YouTube)](https://youtu.be/c67fxomBWOs?si=e6wvLw9iG28VIxlp) |
| **Video Frontend**   | Processes video input.                   | [![Watch Video Frontend](https://img.shields.io/badge/Watch-Video%20Frontend-blue?style=for-the-badge&logo=YouTube)](https://youtu.be/EBTcEdb98ZA?si=LjbXQMGdY0lD0rdx) |
| **YouTube Frontend** | Processes existing YouTube comments.     | [![Watch YouTube Frontend](https://img.shields.io/badge/Watch-YouTube%20Frontend-crimson?style=for-the-badge&logo=YouTube)](https://youtu.be/9eICn3HgVs8?si=Vd375i5hiZB-fy88) |

**Happy Coding! Enjoy building the frontend for DweshaMukt!**
