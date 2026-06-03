from google.cloud import videointelligence_v1p3beta1 as videointelligence
from google.cloud.videointelligence_v1p3beta1.types import (
    Feature,
    TextDetectionConfig,
    VideoContext,
)
import streamlit as st

from config import configure_google_credentials
from model_loader import ModelAssetError, is_hate_label, predict_text


def analyze_gif_text_detection(gif_content):
    credentials_error = configure_google_credentials()
    if credentials_error:
        raise RuntimeError(credentials_error)

    client = videointelligence.VideoIntelligenceServiceClient()
    features = [Feature.TEXT_DETECTION]
    config = TextDetectionConfig(language_hints=["en"])
    context = VideoContext(text_detection_config=config)

    request = videointelligence.AnnotateVideoRequest(
        input_content=gif_content,
        features=features,
        video_context=context,
    )

    operation = client.annotate_video(request)
    results = operation.result(timeout=300)

    extracted_text = ""
    for annotation_result in results.annotation_results:
        for text_annotation in annotation_result.text_annotations:
            extracted_text += text_annotation.text + " "

    return extracted_text.strip()


def gif_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">GIF Text Classification Task</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a GIF", type=["gif"])

    if uploaded_file is not None:
        st.subheader("Uploaded GIF")
        st.image(uploaded_file, use_column_width=True)

        try:
            extracted_text = analyze_gif_text_detection(uploaded_file.read())
        except Exception as exc:
            st.error(str(exc))
            return

        st.subheader("Extracted Text from GIF")
        st.markdown(
            f'<div style="border: 2px solid yellow; border-radius: 10px; padding: 10px;">{extracted_text}</div>',
            unsafe_allow_html=True,
        )

        if not extracted_text:
            st.warning("No text was detected in the uploaded GIF.")
            return

        try:
            predicted_label = predict_text(extracted_text)
        except ModelAssetError as exc:
            st.error(str(exc))
            return
        except Exception as exc:
            st.error(f"GIF text classification failed: {exc}")
            return

        border_color = "red" if is_hate_label(predicted_label) else "green"
        st.subheader("Hate Speech Prediction")
        st.markdown(
            f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">'
            f'Hate Speech Prediction: {predicted_label}</div>',
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    gif_classification_function()
