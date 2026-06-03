import streamlit as st
from googleapiclient.discovery import build

from config import get_youtube_api_key
from model_loader import ModelAssetError, is_hate_label, predict_text


def youtube_comment_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Youtube Video Comment Classification Task</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form(key="input_form"):
        st.write("Please enter the YouTube video ID and the number of comments to display:")
        video_id = st.text_input("YouTube Video ID:")
        num_comments = st.number_input("Number of comments to display:", min_value=1, max_value=100, value=10)
        submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not video_id.strip():
            st.warning("Please enter a YouTube video ID.")
            return

        try:
            comments = video_comments(video_id.strip(), int(num_comments))
        except Exception as exc:
            st.error(str(exc))
            return

        st.write("Comments and Predicted Labels:")
        for comment in comments:
            try:
                predicted_label = predict_text(comment)
            except ModelAssetError as exc:
                st.error(str(exc))
                return
            except Exception as exc:
                st.error(f"YouTube comment classification failed: {exc}")
                return

            border_color = "red" if is_hate_label(predicted_label) else "green"
            st.markdown(
                f'<div style="border: 2px solid pink; border-radius: 10px; padding: 10px; margin-bottom: 10px;">'
                f'Comment: {comment}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">'
                f'Predicted Label: {predicted_label}</div>',
                unsafe_allow_html=True,
            )
            st.write("---")


def video_comments(video_id, num_comments=10):
    api_key = get_youtube_api_key()
    if not api_key:
        raise RuntimeError("YouTube API key not configured. Set YOUTUBE_API_KEY in .env.")

    youtube = build("youtube", "v3", developerKey=api_key)
    video_response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=num_comments,
        textFormat="plainText",
    ).execute()

    return [
        item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        for item in video_response.get("items", [])
    ]


if __name__ == "__main__":
    youtube_comment_classification_function()
