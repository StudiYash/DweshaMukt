import joblib
import numpy as np
import streamlit as st
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

from config import BACKEND_DIR


MODEL_REQUIRED_FILES = (
    "config.json",
    "vocab.txt",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "tf_model.h5",
    "label_encoder.pkl",
)

HATE_LABELS = {"0", "yes", "hate", "hateful"}
NON_HATE_LABELS = {"1", "no", "non-hate", "not hate", "non_hate"}


class ModelAssetError(RuntimeError):
    pass


def validate_model_assets():
    missing_files = [
        filename for filename in MODEL_REQUIRED_FILES
        if not (BACKEND_DIR / filename).exists()
    ]
    if missing_files:
        missing_list = ", ".join(missing_files)
        raise ModelAssetError(
            "Model assets not found in Project Backend. "
            f"Missing: {missing_list}."
        )


@st.cache_resource(show_spinner="Loading hate speech model...")
def load_model_resources():
    validate_model_assets()

    tokenizer = BertTokenizer.from_pretrained(
        str(BACKEND_DIR),
        local_files_only=True,
    )
    model = TFBertForSequenceClassification.from_pretrained(
        str(BACKEND_DIR),
        local_files_only=True,
    )
    model.load_weights(str(BACKEND_DIR / "tf_model.h5"))
    label_encoder = joblib.load(BACKEND_DIR / "label_encoder.pkl")

    return model, tokenizer, label_encoder


def normalize_label(label):
    normalized = str(label).strip().lower()
    if normalized in HATE_LABELS:
        return "yes"
    if normalized in NON_HATE_LABELS:
        return "no"
    return normalized


def is_hate_label(label):
    return normalize_label(label) == "yes"


def predict_text(text):
    if not text or not str(text).strip():
        return "no"

    model, tokenizer, label_encoder = load_model_resources()
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="tf",
    )

    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]

    with tf.device("/cpu:0"):
        outputs = model.predict([input_ids, attention_mask], verbose=0)
        logits = outputs.logits

    probabilities = tf.nn.softmax(logits, axis=1).numpy()[0]
    predicted_label_id = int(np.argmax(probabilities))
    predicted_label = label_encoder.classes_[predicted_label_id]

    return normalize_label(predicted_label)
