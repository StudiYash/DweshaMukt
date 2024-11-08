# Haspe Image Bot 🖼️

Welcome to the **Haspe Image Bot**, a Telegram bot designed to detect hate speech in images using Google Cloud Vision and a BERT model. The bot processes images, extracts text, and classifies it as **Hate** or **Non-Hate** speech.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Bot Commands](#bot-commands)
- [Important Notes](#important-notes)

---

## Features
- Extracts text from images using Google Cloud Vision API.
- Classifies the extracted text as **Hate** or **Non-Hate** speech.
- Provides real-time responses to user inputs.
- Simple setup and easy-to-use Telegram interface.

---

## Requirements
Before setting up the bot, ensure you have the following:
- Python 3.10 or later.
- A **Telegram Bot API Token** (from [BotFather](https://core.telegram.org/bots#botfather)).
- Google Cloud API Credentials for Vision API.
- Necessary Python libraries:
  - `python-telegram-bot`
  - `nest_asyncio`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `tensorflow`
  - `transformers`
  - `google-cloud-vision`
  - `joblib`
- A trained BERT model and supporting files:
  - `tf_model.h5` (TensorFlow model file)
  - `label_encoder.pkl` (Label encoder file)
  - Model directory files: `config.json`, `vocab.txt`, `tokenizer_config.json`, `special_tokens_map.json`

---

## Setup Instructions

### Step 1: Install Dependencies
Run the following commands to install the required libraries:
```bash
pip install python-telegram-bot nest_asyncio pandas numpy scikit-learn tensorflow transformers google-cloud-vision joblib
```

### Step 2: Prepare the Model and Files

Place the following files in the specified directories:

- **Model directory**:
  - `config.json`
  - `vocab.txt`
  - `tokenizer_config.json`
  - `special_tokens_map.json`

- **TensorFlow model file**:
  - `tf_model.h5`

- **Label encoder file**:
  - `label_encoder.pkl`

All files should be located inside the Project Backend directory, accessible via the button below:

[![Project Backend](https://img.shields.io/badge/View-Project%20Backend-blue?style=for-the-badge&logo=github)](https://github.com/StudiYash/DweshaMukt/tree/main/Project%20Backend)

### Step 3: Update the API Credentials Path in the Code

Update the Google Cloud Vision API credentials path in the code:

```python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Image Detection/credentials.json"
```

### Step 4: Update the Code

Replace the placeholder text in the code with your **Telegram Bot API Token**:

```python
TOKEN: Final = 'Your Telegram Bot API Token'
```

### Step 5: Run the Bot

- Execute the script in your environment (e.g., Google Colab, Jupyter Notebook, or local Python environment).
- The bot will start polling and respond to commands and messages on Telegram.

---

## Bot Commands

- **/start**: Greets the user and provides a brief introduction.
- **/help**: Explains the bot's functionality and expected input format.
- **/image**: Prompts the user to upload an image for classification.
- **Message Handling**:
  - Processes images, extracts text, and classifies the text as **Hate** or **Non-Hate** speech.
  - Handles non-image inputs by prompting the user to provide a valid image.

---

## Important Notes

- **Google Cloud Vision API**: The bot uses Google Vision API to extract text from images before classification. Ensure API credentials are correctly set.
- **Input Format**: The bot processes only image inputs. Non-image inputs are flagged, and the user is prompted to provide valid images.
- **Device Compatibility**: The bot is optimized to run on a CPU.
- **Polling**: The bot uses polling to check for new messages. Ensure that the polling interval does not exceed the Telegram API limits.
- **Testing Environment**: The bot is designed for deployment in Google Colab or a local Python environment.

---

**Happy testing, and thank you for using Haspe Image Bot! 😊**