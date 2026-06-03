from pathlib import Path

import joblib
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

from config import BACKEND_DIR, REPO_ROOT
from model_loader import load_model_resources, normalize_label


FIXED_TESTS = [
    "I hate you",
    "You are a good person",
    "You are amazing",
    "I will kill you",
    "Have a nice day",
    "This is disgusting",
    "Have a wonderful day",
    "I love this project",
    "Thank you for your help",
    "This is a beautiful place",
    "You are disgusting",
    "Get lost idiot",
    "I want to hurt you",
]


def softmax(logits):
    values = tf.nn.softmax(logits, axis=1).numpy()[0]
    return [float(value) for value in values]


def load_raw_resources():
    tokenizer = BertTokenizer.from_pretrained(str(BACKEND_DIR), local_files_only=True)
    model = TFBertForSequenceClassification.from_pretrained(
        str(BACKEND_DIR),
        local_files_only=True,
    )
    model.load_weights(str(BACKEND_DIR / "tf_model.h5"))
    label_encoder = joblib.load(BACKEND_DIR / "label_encoder.pkl")
    return model, tokenizer, label_encoder


def predict_raw(model, tokenizer, label_encoder, text):
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="tf",
    )
    outputs = model.predict(
        [encoding["input_ids"], encoding["attention_mask"]],
        verbose=0,
    )
    logits_array = outputs.logits.numpy() if hasattr(outputs.logits, "numpy") else np.asarray(outputs.logits)
    logits = logits_array[0]
    probabilities = softmax(logits_array)
    argmax_index = int(np.argmax(probabilities))
    raw_label = str(label_encoder.classes_[argmax_index])

    return {
        "logits": [float(value) for value in logits],
        "probabilities": probabilities,
        "argmax_index": argmax_index,
        "raw_label": raw_label,
        "normalized_label": normalize_label(raw_label),
        "published_mapping_0_yes_1_no": {0: "yes", 1: "no"}.get(argmax_index, "other"),
    }


def predict_with_loaded_frontend_resources(resources, text):
    model, tokenizer, label_encoder = resources
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="tf",
    )
    outputs = model.predict(
        [encoding["input_ids"], encoding["attention_mask"]],
        verbose=0,
    )
    logits_array = outputs.logits.numpy() if hasattr(outputs.logits, "numpy") else np.asarray(outputs.logits)
    probabilities = tf.nn.softmax(logits_array, axis=1).numpy()[0]
    predicted_label_id = int(np.argmax(probabilities))
    predicted_label = label_encoder.classes_[predicted_label_id]
    return normalize_label(predicted_label)


def load_text_input_files():
    text_dir = REPO_ROOT / "Project Test Inputs" / "Text"
    if not text_dir.exists():
        return []

    inputs = []
    for path in sorted(text_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        if text:
            inputs.append((f"file:{path.name}", text))
    return inputs


def print_prediction(name, text, result, frontend_prediction):
    print("=" * 88)
    print(f"INPUT_NAME: {name}")
    print(f"TEXT: {text[:300].replace(chr(10), ' ')}")
    print(f"LOGITS: {result['logits']}")
    print(f"PROBABILITIES: {result['probabilities']}")
    print(f"ARGMAX_INDEX: {result['argmax_index']}")
    print(f"RAW_LABEL_ENCODER_LABEL: {result['raw_label']}")
    print(f"NORMALIZED_LABEL: {result['normalized_label']}")
    print(f"FRONTEND_PREDICT_TEXT: {frontend_prediction}")
    print(f"PUBLISHED_MAPPING_0_YES_1_NO: {result['published_mapping_0_yes_1_no']}")


def main():
    print("BACKEND_DIR:", BACKEND_DIR)
    model, tokenizer, label_encoder = load_raw_resources()
    print("TOKENIZER_TYPE:", type(tokenizer))
    print("MODEL_TYPE:", type(model))
    print("MODEL_NUM_LABELS:", model.config.num_labels)
    print("MODEL_ID2LABEL:", model.config.id2label)
    print("MODEL_LABEL2ID:", model.config.label2id)
    print("MODEL_OUTPUT_SHAPE:", model.classifier.units)
    print("LABEL_ENCODER_TYPE:", type(label_encoder))
    print("LABEL_ENCODER_CLASSES:", list(label_encoder.classes_))
    print("LABEL_ENCODER_DICT:", label_encoder.__dict__)
    frontend_resources = load_model_resources()

    all_inputs = [(f"fixed:{index + 1}", text) for index, text in enumerate(FIXED_TESTS)]
    all_inputs.extend(load_text_input_files())

    counts = {"yes": 0, "no": 0, "other": 0}
    raw_argmax_counts = {}

    for name, text in all_inputs:
        result = predict_raw(model, tokenizer, label_encoder, text)
        frontend_prediction = predict_with_loaded_frontend_resources(frontend_resources, text)
        normalized = result["normalized_label"]
        if normalized in counts:
            counts[normalized] += 1
        else:
            counts["other"] += 1

        raw_argmax_counts[result["argmax_index"]] = raw_argmax_counts.get(result["argmax_index"], 0) + 1
        print_prediction(name, text, result, frontend_prediction)

    print("=" * 88)
    print("SUMMARY_NORMALIZED_COUNTS:", counts)
    print("SUMMARY_RAW_ARGMAX_COUNTS:", raw_argmax_counts)


if __name__ == "__main__":
    main()
