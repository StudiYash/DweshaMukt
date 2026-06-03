import streamlit as st
import pytesseract as tess
from PIL import Image

from config import configure_tesseract
from model_loader import ModelAssetError, is_hate_label, predict_text


def get_css_styles():
    return """
    <style>
    .extracted-text-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
    }
    .predicted-label-box {
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
    }
    </style>
    """


def image_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Image Text Classification Task</div>', unsafe_allow_html=True)

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        tesseract_error = configure_tesseract(tess)
        if tesseract_error:
            st.error(tesseract_error)
            return

        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image", use_column_width=True, width=300)

        try:
            extracted_text = tess.image_to_string(img)
        except Exception as exc:
            st.error(f"Tesseract OCR failed: {exc}")
            return

        st.markdown(get_css_styles(), unsafe_allow_html=True)
        st.markdown(f'<div class="extracted-text-box">{extracted_text}</div>', unsafe_allow_html=True)

        if not extracted_text.strip():
            st.warning("No text was detected in the uploaded image.")
            return

        try:
            predicted_label = predict_text(extracted_text)
        except ModelAssetError as exc:
            st.error(str(exc))
            return
        except Exception as exc:
            st.error(f"Image text classification failed: {exc}")
            return

        border_color = "red" if is_hate_label(predicted_label) else "green"
        st.markdown(
            f"""
            <style>
            .predicted-label-box {{
                border: 2px solid {border_color};
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="predicted-label-box">Predicted Label: {predicted_label}</div>',
            unsafe_allow_html=True,
        )


def main():
    image_classification_function()


if __name__ == "__main__":
    main()
