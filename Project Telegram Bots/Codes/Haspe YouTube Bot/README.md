# Haspe YouTube Bot 📹

Welcome to the **Haspe YouTube Bot**, a Telegram bot designed to detect hate speech in live comments from YouTube live streams. The bot uses a BERT model to process live comments and classify them as **Hate** or **Non-Hate** speech.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Bot Commands](#bot-commands)
- [Important Notes](#important-notes)

---

## Features
- Fetches live comments from YouTube live stream videos.
- Classifies live comments as **Hate** or **Non-Hate** speech.
- Provides real-time responses to user inputs.
- Simple setup and easy-to-use Telegram interface.

---

## Requirements
Before setting up the bot, ensure you have the following:
- Python 3.10 or later.
- A **Telegram Bot API Token** (from [BotFather](https://core.telegram.org/bots#botfather)).
- Necessary Python libraries:
  - `python-telegram-bot`
  - `nest_asyncio`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `tensorflow`
  - `transformers`
  - `pytchat`
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
pip install python-telegram-bot nest_asyncio pandas numpy scikit-learn tensorflow transformers pytchat joblib
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

### Step 3: Update the Code

Replace the placeholder text in the code with your **Telegram Bot API Token**:

```python
TOKEN: Final = 'Your Telegram Bot API Token'
```

### Step 4: Run the Bot

- Execute the script in your environment (e.g., Google Colab, Jupyter Notebook, or local Python environment).
- The bot will start polling and respond to commands and messages on Telegram.

---

## Bot Commands

- **/start**: Greets the user and provides a brief introduction.
- **/help1**: Explains the bot's functionality and expected input format.
- **/help2**: Instructs the user to re-submit the YouTube Video ID if no output is received.
- **/help3**: Informs the user that the fetching process has stopped due to the 4-second timer and advises re-submitting the Video ID to continue.
- **/youtube**: Prompts the user to provide a YouTube Video ID in plain text format for classification.

---

## Important Notes

- **YouTube Video ID Format**: The Video ID should be an 11-character alphanumeric string. Invalid IDs will be flagged with an error message.
- **Input Format**: The bot processes only YouTube Video IDs in plain text format. Non-text inputs will be flagged, and the user will be prompted to provide valid input.
- **Fetching Timer**: The bot processes live comments for a maximum of 4 seconds per request. To fetch additional comments, re-submit the Video ID.
- **Device Compatibility**: The bot is optimized to run on a CPU.
- **Polling**: The bot uses polling to check for new messages. Ensure that the polling interval does not exceed the Telegram API limits.
- **Testing Environment**: The bot is designed for deployment in Google Colab or a local Python environment.

---

**Happy testing, and thank you for using Haspe YouTube Bot! 😊**