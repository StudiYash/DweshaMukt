import streamlit as st

from model_loader import ModelAssetError, is_hate_label, predict_text


def text_classification_function():
    st.markdown('<div style="border: 3px solid pink; border-radius: 10px; padding: 10px;text-align: center;">Text Classification Task</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    user_input = st.text_input("Enter text to classify:")

    if st.button("Predict"):
        if not user_input:
            st.warning("Please enter some text.")
            return

        prediction = has_hateful_emoji(user_input)
        if prediction is None:
            try:
                prediction = predict_text(user_input)
            except ModelAssetError as exc:
                st.error(str(exc))
                return
            except Exception as exc:
                st.error(f"Unable to run text classification: {exc}")
                return

        border_color = "red" if is_hate_label(prediction) else "green"
        st.markdown(
            f'<div style="border: 2px solid {border_color}; border-radius: 10px; padding: 10px;">'
            f'Predicted Label: {prediction}</div>',
            unsafe_allow_html=True,
        )


hateful_emojis = [
    u'😠', u'😡', u'🤬', u'🥵', u'🤢', u'🤮', u'👿', u'💩', u'👎',
    u'👎🏻', u'👎🏼', u'👎🏽', u'👎🏾', u'👎🏿', u'🖕', u'🖕🏻',
    u'🖕🏼', u'🖕🏽', u'🖕🏾', u'🖕🏿', u'👙', u'🩱', u'💦',
    u'🍌', u'🍑', u'🥊', u'🏴‍☠️',
]


def has_hateful_emoji(text):
    for emoji in hateful_emojis:
        if emoji in text:
            return "yes"
    return None


if __name__ == "__main__":
    text_classification_function()
