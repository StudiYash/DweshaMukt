# Haspe Text Bot 🤖

Welcome to the **Haspe Text Bot**, a Telegram bot designed to detect hate speech in text inputs using a BERT model. The bot processes text messages and classifies them as **Hate** or **Non-Hate** speech, with added detection for hateful emojis.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Bot Commands](#bot-commands)
- [Important Notes](#important-notes)

---

## Features
- Classifies text messages as **Hate** or **Non-Hate** speech.
- Detects and flags hateful emojis in text.
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
  - `transformers`
  - `tensorflow`
  - `numpy`
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
pip install python-telegram-bot nest_asyncio transformers tensorflow numpy joblib
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

All files should be located inside the Project Backend directory which can be accessed by pressing the button below :

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
- **/help**: Explains the bot's functionality and expected input format.
- **/text**: Prompts the user to enter a text message for classification.
- **Message Handling**: Automatically processes any text message sent to the bot and classifies it.

---

## Important Notes

- **Hateful Emojis**: The bot includes a predefined list of hateful emojis and flags messages containing them as **Hate** speech.
- **Input Format**: The bot processes only text inputs. If the input is not text, it will prompt the user to provide a valid text input.
- **Device Compatibility**: The bot is optimized to run on a CPU.
- **Polling**: The bot uses polling to check for new messages. Ensure that the polling interval does not exceed the Telegram API limits.
- **Testing Environment**: The bot is designed for deployment in Google Colab or a local Python environment.

---

**Happy testing, and thank you for using Haspe Text Bot! 😊**