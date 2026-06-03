import os
import tempfile
import wave

import moviepy.editor as mp
import speech_recognition as sr
import streamlit as st

from model_loader import ModelAssetError, is_hate_label, predict_text


def cleanup_paths(paths):
    for path in paths:
        if path and os.path.exists(path):
            try:
                os.remove(path)
            except OSError:
                pass


def transcribe_video(video_file):
    temp_video_file_path = None
    temp_wav_file_path = None
    video_clip = None
    audio_clip = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(video_file.read())
            temp_video_file_path = temp_video.name

        temp_wav_file_path = temp_video_file_path + ".wav"
        video_clip = mp.VideoFileClip(temp_video_file_path)

        if video_clip.duration > 240:
            raise RuntimeError("The uploaded video must be less than or equal to 4 minutes in duration.")

        if video_clip.audio is None:
            raise RuntimeError("No audio track was found in the uploaded video.")

        audio_clip = video_clip.audio
        audio_bytes = audio_clip.to_soundarray()
        audio_samples = (audio_bytes * 32767).astype("int16")

        with wave.open(temp_wav_file_path, "wb") as wav_file:
            channels = 1 if len(audio_samples.shape) == 1 else audio_samples.shape[1]
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(2)
            wav_file.setframerate(audio_clip.fps)
            wav_file.writeframes(audio_samples.tobytes())

        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_wav_file_path) as source:
            data = recognizer.record(source)

        return recognizer.recognize_google(data)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as exc:
        raise RuntimeError(
            "Could not request results from Google Speech Recognition service. "
            "Check your internet connection."
        ) from exc
    finally:
        if audio_clip is not None:
            audio_clip.close()
        if video_clip is not None:
            video_clip.close()
        cleanup_paths([temp_video_file_path, temp_wav_file_path])


def video_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Video Transcription Classification Task</div>', unsafe_allow_html=True)

    video_file = st.file_uploader("Upload a video file", type=["mp4"])

    if video_file is not None:
        st.video(video_file)

        st.markdown("<h2 style='border-radius: 10px; border: 2px solid pink; padding: 10px;'>Transcription:</h2>", unsafe_allow_html=True)
        try:
            with st.spinner("Transcribing..."):
                text = transcribe_video(video_file)
        except Exception as exc:
            st.error(f"An error occurred while transcribing the video: {exc}")
            return

        if not text:
            st.error("No text recognized.")
            return

        st.write(text)

        try:
            predicted_label = predict_text(text)
        except ModelAssetError as exc:
            st.error(str(exc))
            return
        except Exception as exc:
            st.error(f"Video classification failed: {exc}")
            return

        border_color = "red" if is_hate_label(predicted_label) else "green"
        st.markdown("<h2 style='border-radius: 10px; padding: 10px;'>Prediction:</h2>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">'
            f'Predicted Label: {predicted_label}</div>',
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    video_classification_function()
