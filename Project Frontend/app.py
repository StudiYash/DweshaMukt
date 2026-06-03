from pathlib import Path

import streamlit as st


FRONTEND_DIR = Path(__file__).resolve().parent


def main():
    styles_path = FRONTEND_DIR / "styles.css"
    if styles_path.exists():
        st.markdown(f"<style>{styles_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

    st.title("Hate Speech Detection in Hinglish")

    st.sidebar.markdown('<h1 style="text-align: center; font-weight: bold;"><b>Hate Nirikshak</b></h1>', unsafe_allow_html=True)

    hate_image = FRONTEND_DIR / "Hate.jpg"
    if hate_image.exists():
        st.sidebar.image(str(hate_image), width=300)

    page = st.sidebar.radio(
        "Navigation",
        ["🏠Home", "✅Check Model", "🙎‍♂️About Us"],
        label_visibility="collapsed",
    )

    if page == "🏠Home":
        st.markdown('<div class="home-container">', unsafe_allow_html=True)
        st.write("**Objective:**")
        st.write("The primary objective of hate speech detection in Hinglish is to develop machine learning models that can accurately identify and classify text as hate speech or non-hate speech. By leveraging natural language processing (NLP) techniques and deep learning models, these systems aim to combat online hate speech and promote a safer and more inclusive online environment.")
        st.markdown('<h4 style="color: pink; text-align: center;">Comprehensive Hate Speech Detection: Addressing Multiple Scenarios and Contexts</h4>', unsafe_allow_html=True)

        models_gif = FRONTEND_DIR / "models.gif"
        if models_gif.exists():
            st.image(str(models_gif), caption="", width=50, use_column_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif page == "✅Check Model":
        options = [
            "Text Classification",
            "Audio Classification",
            "Video Classification",
            "Image Classification",
            "GIF Classification",
            "Youtube Comment Classification",
        ]
        selected_option = st.sidebar.selectbox("Select Classification Task:", options)

        if selected_option == "Text Classification":
            from text_classification import text_classification_function
            text_classification_function()

        elif selected_option == "Audio Classification":
            st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Audio Text Classification Task</div>', unsafe_allow_html=True)
            from audio_classification import audio_classification_function
            audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
            if audio_file is not None:
                try:
                    text, prediction = audio_classification_function(audio_file)
                except Exception as exc:
                    st.error(f"Audio classification failed: {exc}")
                    return

                if text:
                    st.write("Transcription:", text)
                    st.write("Prediction:", prediction)
                else:
                    st.warning("No speech text was recognized.")

        elif selected_option == "Video Classification":
            from video_classification import video_classification_function
            video_classification_function()

        elif selected_option == "Image Classification":
            from image_classification import image_classification_function
            image_classification_function()

        elif selected_option == "GIF Classification":
            from gif_classification import gif_classification_function
            gif_classification_function()

        elif selected_option == "Youtube Comment Classification":
            from youtube_comment_classification import youtube_comment_classification_function
            youtube_comment_classification_function()

    elif page == "🙎‍♂️About Us":
        st.markdown('<div class="about-us-container">', unsafe_allow_html=True)
        st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Meet the Project Team</div>', unsafe_allow_html=True)
        st.write(" ")

        about_gif = FRONTEND_DIR / "about us.gif"
        if about_gif.exists():
            st.image(str(about_gif), caption="", width=50, use_column_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Project Guide : Mr. Rajkumar Panchal</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Assistant Professor at VPKBIET, Baramati</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>M.Tech. (Computer Engineering) Ph.D. (Pursuing)</h5>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
