# Project Frontend

This folder contains the DweshaMukt Streamlit frontend for Hinglish hate speech detection.

The app supports two setup levels:

- **Basic Mode:** run the app and use text classification from the repository's local model files.
- **Full Mode:** enable audio, image, GIF, video, and YouTube workflows by installing local tools and configuring optional API credentials.

Prediction labels are standardized as:

```text
yes = hate speech
no = non-hate speech
```

## Basic Mode

Basic Mode does not require Google Cloud credentials, a YouTube API key, Tesseract path edits, or source-code changes.

Requirements:

- Python 3.10 recommended; Python 3.13 is also supported by the version-marked dependency file
- pip
- Repository model assets in `Project Backend/`

From the repository root:

```bash
cd "Project Frontend"
python -m venv .venv
.venv\Scripts\activate
pip install -r frontend_requirements.txt
streamlit run app.py
```

On macOS/Linux, activate the environment with:

```bash
source .venv/bin/activate
```

Expected Basic Mode functionality:

```text
Text Classification
```

The app loads model/tokenizer assets from:

```text
../Project Backend/
```

Required files:

```text
config.json
vocab.txt
tokenizer_config.json
special_tokens_map.json
tf_model.h5
label_encoder.pkl
```

## Full Mode

Full Mode supports:

```text
Text
Audio
Image
GIF
Video
YouTube Comments
```

Additional requirements:

- ffmpeg for audio/video conversion
- Tesseract OCR for image text extraction
- Google Cloud Video Intelligence credentials for GIF text extraction
- YouTube Data API key for YouTube comment classification
- Internet access for audio/video speech recognition and cloud/API workflows

### Environment Configuration

Copy the example file from the repository root:

```bash
copy ..\.env.example ..\.env
```

On macOS/Linux:

```bash
cp ../.env.example ../.env
```

Fill only the values you need:

```text
YOUTUBE_API_KEY=
GOOGLE_APPLICATION_CREDENTIALS=
TESSERACT_CMD=
```

`GOOGLE_APPLICATION_CREDENTIALS` may be a path relative to the repository root, or a machine-specific absolute path kept only in your private `.env`.

`TESSERACT_CMD` is only needed if the `tesseract` executable is not available on PATH.

Do not commit `.env` or real credential files.

## Modality Setup

| Modality | Basic/Full | Extra setup |
|---|---|---|
| Text | Basic | None beyond Python dependencies and local model files |
| Audio | Full | ffmpeg, internet access for `SpeechRecognition.recognize_google` |
| Image | Full | Tesseract OCR installed or `TESSERACT_CMD` configured |
| GIF | Full | Google Cloud Video Intelligence enabled and `GOOGLE_APPLICATION_CREDENTIALS` configured |
| Video | Full | ffmpeg, MoviePy, internet access for `SpeechRecognition.recognize_google` |
| YouTube Comments | Full | YouTube Data API key configured as `YOUTUBE_API_KEY` |

## Smoke Test Instructions

Use files from:

```text
../Project Test Inputs/
```

Suggested checks:

1. Text: open `Project Test Inputs/Text/Text Input 1.txt`, paste its content into Text Classification, and confirm a `yes` or `no` label appears.
2. Audio: upload `Project Test Inputs/Audios/Audio Input 1.mp3` after ffmpeg is installed.
3. Image: upload `Project Test Inputs/Images/Image Input 1.jpg` after Tesseract is installed.
4. GIF: upload `Project Test Inputs/GIFs/GIF Input 1.gif` after Google Cloud credentials are configured.
5. Video: upload `Project Test Inputs/Videos/Video Input 1.mp4` after ffmpeg is installed.
6. YouTube: enter a valid YouTube video ID after setting `YOUTUBE_API_KEY`.

## Troubleshooting

### Model assets not found

Error:

```text
Model assets not found in Project Backend.
```

Fix:

- Confirm the repository contains the required files in `Project Backend/`.
- Run Streamlit from `Project Frontend/` or the repository using the documented command.
- Do not move `tf_model.h5` or `label_encoder.pkl` into random local folders.

### Tesseract OCR not found

Error:

```text
Tesseract OCR not found.
```

Fix:

- Install Tesseract OCR.
- Add it to PATH, or set `TESSERACT_CMD` in `.env`.

Example:

```text
TESSERACT_CMD=tools/tesseract/tesseract
```

### Google Cloud credentials not configured

Error:

```text
Google Cloud credentials not configured.
```

Fix:

- Create a Google Cloud service-account JSON key.
- Enable Video Intelligence API.
- Set `GOOGLE_APPLICATION_CREDENTIALS` in `.env`.

### YouTube API key not configured

Error:

```text
YouTube API key not configured.
```

Fix:

- Create a YouTube Data API v3 key.
- Set `YOUTUBE_API_KEY` in `.env`.

### ffmpeg missing

Symptoms:

- Audio conversion fails.
- Video processing fails.
- MoviePy or pydub errors mention codecs or ffmpeg.

Fix:

- Install ffmpeg.
- Confirm `ffmpeg -version` works in your terminal.

## Notes

- Audio and video transcription use the `SpeechRecognition` package's `recognize_google` method, which requires internet access.
- GIF text detection uses Google Cloud Video Intelligence and may incur cloud usage costs.
- Uploaded content may be sent to external services for Full Mode workflows.
