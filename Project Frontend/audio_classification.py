import os
import tempfile

import speech_recognition as sr
import streamlit as st
from pydub import AudioSegment
from pydub.utils import mediainfo

from model_loader import ModelAssetError, is_hate_label, predict_text


def convert_audio_to_wav(audio_file):
    suffix = os.path.splitext(audio_file.name or "")[1] or ".audio"
    original_path = None
    converted_path = None

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(audio_file.read())
        original_path = temp_file.name

    try:
        audio_info = mediainfo(original_path)
        audio_format = audio_info.get("format_name", "")

        if "wav" in audio_format.lower():
            return original_path, [original_path]

        audio = AudioSegment.from_file(original_path)
        audio = audio[:120000]
        converted_path = original_path + ".wav"
        audio.export(converted_path, format="wav")
        return converted_path, [original_path, converted_path]
    except Exception:
        cleanup_paths([original_path, converted_path])
        raise


def cleanup_paths(paths):
    for path in paths:
        if path and os.path.exists(path):
            try:
                os.remove(path)
            except OSError:
                pass


def recognize_speech(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as exc:
        raise RuntimeError(
            "Could not request results from Google Speech Recognition service. "
            "Check your internet connection."
        ) from exc


def audio_classification_function(audio_file):
    converted_file = None
    cleanup_targets = []

    try:
        converted_file, cleanup_targets = convert_audio_to_wav(audio_file)
        text = recognize_speech(converted_file)

        if not text:
            return "", None

        prediction = predict_text(text)
        return text, prediction
    finally:
        cleanup_paths(cleanup_targets)


def render_prediction(prediction):
    border_color = "red" if is_hate_label(prediction) else "green"
    st.markdown(
        f'<div style="border: 2px solid {border_color}; border-radius: 5px; padding: 10px;">'
        f'<h3>Prediction: {prediction}</h3></div>',
        unsafe_allow_html=True,
    )


def main():
    st.title("Speech to Text and Hate Speech Detection")
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        try:
            text, prediction = audio_classification_function(uploaded_file)
        except ModelAssetError as exc:
            st.error(str(exc))
            return
        except Exception as exc:
            st.error(f"Audio classification failed: {exc}")
            return

        if text:
            st.write("Transcription:")
            st.write(text)
            st.audio(uploaded_file, format="audio/wav")
            render_prediction(prediction)
        else:
            st.write("Sorry, the speech could not be understood.")


if __name__ == "__main__":
    main()
