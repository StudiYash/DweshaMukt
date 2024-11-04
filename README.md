# Hate Speech Detection Project

## 1. Basic Idea Explanation

### Project Idea Introduction
Hate speech poses a significant threat to societal harmony and safety, often inciting violence and discrimination. Recent real-time incidents, such as communal unrest in various parts of the world triggered by inflammatory online content, highlight the need for effective hate speech detection mechanisms. This project introduces a comprehensive hate speech detection model that leverages the **Bidirectional Encoder Representations from Transformers (BERT)** algorithm, along with advanced **Deep Learning** and **Natural Language Processing (NLP)** techniques.

Our model specifically addresses the challenges of detecting hate speech within the **Hinglish** language, a code-mixed variant combining Hindi and English. Utilizing a pre-trained BERT model, we tailored it for real-time scenarios, providing robust and in-depth analysis capabilities. The system adopts a **multilingual and multimodal approach**, enabling the detection of hate speech across various content formats, including text, audio, video, images, GIFs, and YouTube video comments.

Experimental results show an accuracy of 0.88, underscoring the model's efficacy in hate speech detection and its potential for application in diverse real-world contexts.

**Index Terms**: Hate Speech Detection, BERT, Deep Learning, Natural Language Processing, Multilingual, Multimodal, Hinglish, Real-Time Analysis

### Project Timeline
- **Start Date**: 15th February 2023
- **End Date**: 20th October 2024
- **Total Time Required**: 1 Year, 8 Months, and 5 Days

### Team Members
- **Yash Suhas Shukla** — [GitHub](#) | [LinkedIn](#)
- **Tanmay Dnyaneshwar Nigade** — [GitHub](#) | [LinkedIn](#)
- **Suyash Vikas Khodade** — [GitHub](#) | [LinkedIn](#)
- **Prathamesh Dilip Pimpalkar** — [GitHub](#) | [LinkedIn](#)

### Project Guide
- **Prof. Rajkumar Panchal** — [GitHub](#) | [LinkedIn](#)

## 2. Backend Preparation

### 15 Mark Models Index

#### Initial Notes
1. The entire project's backend has 3 Base Models with varying accuracies. **Base Model 3** is the latest and currently in use.
2. **Mark 13, Mark 14,** and **Mark 15** are untested codes developed to explore new base models.
3. This document was last updated on 04/11/2024.

#### Tested Mark Models Index
- **Mark 1**: Works for English; uses BERT (bert-base-uncased) and PyTorch. Dataset: HASOC_English_Dataset_2019.
- **Mark 2**: Similar to Mark 1, using BERT (bert-large-uncased). Dataset: HASOC_English_Dataset_2019.
- **Mark 3**: First Hinglish model, using BERT (bert-base-multilingual-uncased). Datasets: hasoc_hinglish_train_2021 + hasoc_hinglish_train_2022.
- **Mark 4**: Hinglish support, processes text. Dataset: GitHub_Dataset 1_Hinglish_Tanmay_Version 1.
- **Mark 5**: Hinglish support, processes YouTube comments. Dataset: GitHub_Dataset 1_Hinglish_Tanmay_Version 1.
- **Mark 6**: Hinglish support, processes audio. Dataset: GitHub_Dataset 1_Hinglish_Tanmay_Version 1.
- **Mark 7**: Hinglish support, processes images. Dataset: GitHub_Dataset 1_Hinglish_Tanmay_Version 1.
- **Mark 8**: Hinglish support, processes GIFs and videos. Dataset: GitHub_Dataset 1_Hinglish_Tanmay_Version 1.
- **Mark 9**: Combines Mark 4, 5, 6, 7, 8 for processing text, audio, images, GIFs, videos, and YouTube comments.
- **Mark 10**: Uses Base Model 3 with a binary classifier in TensorFlow for text processing.
- **Mark 11**: Combines Mark 10, 5, 6, 7, 8 using TensorFlow and binary classification.
- **Mark 12**: Extends Mark 11 with video-to-audio conversion and emoticon-based classification.

> **Note**: Mark 12 Saved Model 3 achieved the highest accuracy and was used in the IEEE research paper.

#### Untested Mark Models Index
- **Mark 13**: Experimented configurations in PyTorch and TensorFlow; language detection and mixed precision training.
- **Mark 14**: Diversified approach with traditional ML models and transformers (e.g., Roberta, DistilBERT, XLNet).
- **Mark 15**: Hyperparameter tuning with Ray Tune on novel configurations using BERT + CRF models.

## 3. Finalised Backend Explanation

The Hate Speech Detection project is designed to classify input—whether text, audio, image, video, or live YouTube comments—into Hate or Non-Hate categories. This section covers six distinct scenarios, each targeting a specific input type.

### Scenarios
1. **Text Input**: Text entered by the user is classified directly.
2. **Audio Input**: Audio is converted to text via Google STT and then classified.
3. **Image Input**: Text from images is extracted using Google Cloud Vision API and classified.
4. **GIF Input**: Text from GIFs is extracted with Google Video Intelligence API and classified.
5. **Video Input**: Video is processed in two sub-scenarios:
   - Conversion to audio for classification.
   - Direct text extraction similar to GIFs.
6. **Live YouTube Video**: Live comments are fetched using the pytchat library and classified.

Each scenario ultimately converts the input to text before classification, with **Scenario 1** serving as the base code.

The combined code integrates all six scenarios, with emoticon-based classification as an added feature.

## 4. Project Dataset

### Mark 12 Saved Model 3 Dataset Details
- **Datasets Used**: CONSTRAINT 2021 and Hindi Hate Speech Detection (HHSD)
- **Total Comments**: 22,977
  - **Hate**: 9,705 comments
  - **Non-Hate**: 13,272 comments

![Dataset Graph](file-eW4UvNsA1gqdROWBbw6SdvlA)  
[Dataset Requesting Google Form](#)

## 5. Finalised Frontend Explanation

The frontend for this project is implemented as a **Streamlit** application, allowing classification across multiple input formats such as text, audio, video, images, GIFs, and YouTube comments. Key functionalities include model loading, task selection, emoji detection, and interactive user interface.

...

(Each frontend task breakdown goes here, with features for text, audio, video, image, GIF, and YouTube comments)

## 6. Telegram Bots Explanation

This project is integrated with Telegram via multiple bots for each input type:
- **Haspe Text**: Processes text input.
- **Haspe Audio**: Processes audio input.
- **Haspe Image**: Processes image input.
- **Haspe GIF**: Processes GIF input.
- **Haspe Video**: Processes video input.
- **Haspe Youtube**: Processes YouTube live comments.

Each bot interacts with the Google Colab backend to classify the input and return results.

## 7. Project Representation

This project was represented at the **Nexus 1.0 State Level Project Competition** held at Army Institute of Technology, Pune, on **15th April 2024**. Organized by the Department of IT and Computer Engineering under the AIT ACM Student Chapter.

Participation Certificates: [Photo1](#) | [Photo2](#) | [Photo3](#) | [Photo4](#)

## 8. Project Conference

- **Research Paper**: Submitted to IEEE, accessible at [official_link](#).
- **Conference Attendance**: Yash Shukla and Prof. Rajkumar Panchal.
- **Conference Report**: Documenting participation at **CVMI-2024**, IEEE conference at IIIT Allahabad on 19th and 20th October 2024.

Conference Certificates: [Photo1](#) | [Photo2](#)

## 9. Project Copyright

- **Publication Date**: 25th October 2024
- **Document Text**: See full project title, objectives, methodology, uniqueness, applications, and future scope.

Certificate: [Photo1](#)

## 10. Project Funding

Funded by **VPKBIET College**.

- **Funding Requirement**: [Photo1](#)
- **Funding Unofficial Certificate**: [Photo1](#)

## 11. Project Blackbook

The sharable draft of the project blackbook can be accessed [here](official_link).
