# DweshaMukt Local Setup Guide

This guide helps you run DweshaMukt locally after cloning the repository.

No training is required. No private dataset is required. The final model artifacts are already included in `Project Backend/`.

## What You Can Run

DweshaMukt can be used in two main ways:

| Mode | What it runs | Extra services needed |
|---|---|---|
| Frontend Basic Mode | Streamlit text classification | None beyond Python dependencies and local model assets |
| Frontend Full Mode | Text, audio, image, GIF, video, and YouTube workflows | Optional local tools and API credentials |
| Telegram Bots | Telegram-based text and media classification notebooks | Telegram token and optional modality credentials |

The text classifier uses the included backend model assets and returns:

```text
yes = hate speech
no = non-hate speech
```

## 1. Clone the Repository

```bash
git clone https://github.com/StudiYash/DweshaMukt.git
cd DweshaMukt
```

The model files should already be present in:

```text
Project Backend/
```

Required backend assets:

```text
config.json
vocab.txt
tokenizer_config.json
special_tokens_map.json
tf_model.h5
label_encoder.pkl
```

Do not move these files unless you also update the documented project layout.

## 2. Create a Python Environment

Python 3.10 is recommended.

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the frontend dependencies:

```bash
pip install -r "Project Frontend/frontend_requirements.txt"
```

If you plan to run notebooks, also install Jupyter support:

```bash
pip install notebook ipykernel
```

## 3. Run the Streamlit Frontend

Start the app from the frontend folder:

```bash
cd "Project Frontend"
streamlit run app.py
```

Streamlit will print a local browser URL, usually:

```text
http://localhost:8501
```

## 4. Frontend Basic Mode

Basic Mode is the simplest local setup.

Use it for:

```text
Text Classification
```

Basic Mode requires:

- Python environment
- `Project Frontend/frontend_requirements.txt` installed
- Model artifacts already included in `Project Backend/`

Basic Mode does not require:

- Training
- Datasets
- Google Cloud credentials
- YouTube API key
- Telegram bot token
- Tesseract OCR
- ffmpeg

If the app opens and text classification returns `yes` or `no`, Basic Mode is working.

## 5. Frontend Full Mode

Full Mode enables additional workflows:

```text
Audio
Image
GIF
Video
YouTube Comments
```

Depending on which workflow you use, you may need these optional tools or services:

| Feature | Optional setup |
|---|---|
| Audio | `ffmpeg`, internet access for speech recognition |
| Image | Tesseract OCR, optionally `TESSERACT_CMD` |
| GIF | Google Cloud Video Intelligence |
| Video | `ffmpeg`, Google Cloud or speech recognition support depending on workflow |
| YouTube Comments | YouTube Data API and `YOUTUBE_API_KEY` |

Install only the tools and credentials needed for the features you want to use.

## 6. Environment Variables

Create a private `.env` file from the example:

On Windows:

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

Fill in only the values you need:

```text
YOUTUBE_API_KEY=
GOOGLE_APPLICATION_CREDENTIALS=
TESSERACT_CMD=
TELEGRAM_BOT_TOKEN=
TELEGRAM_BOT_USERNAME=
```

What they are for:

| Variable | Used for |
|---|---|
| `YOUTUBE_API_KEY` | YouTube Data API access |
| `GOOGLE_APPLICATION_CREDENTIALS` | Google Cloud service-account JSON path |
| `TESSERACT_CMD` | Tesseract executable path if it is not on PATH |
| `TELEGRAM_BOT_TOKEN` | Telegram BotFather token |
| `TELEGRAM_BOT_USERNAME` | Public username of your Telegram bot |

Keep `.env` private. Do not commit real tokens, API keys, or service-account JSON files.

## 7. Optional External Tools and Services

These are not needed for Basic Mode, but may be needed for full multimodal features:

- `ffmpeg`
- Tesseract OCR
- Google Cloud Video Intelligence
- Google Cloud Vision
- Google Speech-to-Text
- YouTube Data API
- Telegram BotFather token

Install and configure only the tools required by the modality you are testing.

## 8. Telegram Bot Setup

Telegram bot notebooks are located in:

```text
Project Telegram Bots/Codes/
```

Each bot folder contains a notebook for one input type:

- Haspe Text Bot
- Haspe Audio Bot
- Haspe Image Bot
- Haspe GIF Bot
- Haspe Video Bot
- Haspe YouTube Bot

General setup:

1. Create a Telegram bot with BotFather.
2. Save the bot token in `.env` as `TELEGRAM_BOT_TOKEN`.
3. Save the bot username in `.env` as `TELEGRAM_BOT_USERNAME` if the notebook uses it.
4. Configure modality-specific credentials if needed.
5. Start Jupyter from the repository root.

```bash
jupyter notebook
```

Open the notebook for the bot you want to run.

The notebooks locate `Project Backend/` dynamically, so you should not need to edit local model paths after cloning the repository.

## 9. Troubleshooting

### Model Assets Not Found

Confirm these files exist in `Project Backend/`:

```text
config.json
vocab.txt
tokenizer_config.json
special_tokens_map.json
tf_model.h5
label_encoder.pkl
```

Run commands from the cloned repository layout and avoid moving model files into personal folders.

### Streamlit Command Not Found

Activate your virtual environment, then install frontend dependencies:

```bash
pip install -r "Project Frontend/frontend_requirements.txt"
```

### Tesseract OCR Not Found

Install Tesseract OCR and either add it to PATH or set:

```text
TESSERACT_CMD=
```

### ffmpeg Errors

Install `ffmpeg` and confirm this command works:

```bash
ffmpeg -version
```

### Google Cloud Credential Errors

Enable the required Google Cloud APIs for the workflow you are using, then set:

```text
GOOGLE_APPLICATION_CREDENTIALS=
```

This should point to your private service-account JSON file.

### YouTube API Errors

Enable the YouTube Data API and set:

```text
YOUTUBE_API_KEY=
```

### Telegram Bot Does Not Respond

Check that:

- The bot token came from BotFather.
- `TELEGRAM_BOT_TOKEN` is set in `.env`.
- Only one local copy of the bot is polling at a time.
- Optional media credentials are configured for the bot type you are running.

## 10. Important Notes

- Do not retrain the model for local setup.
- Do not download private datasets for local setup.
- Do not commit `.env` files or credentials.
- Basic frontend text classification can run with the included local model assets.
- Full mode and Telegram media bots may require optional tools, internet access, and external service credentials.
