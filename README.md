# ![DweshaMukt](https://github.com/StudiYash/DweshaMukt/blob/main/DweshaMukt%20Logo.png)

## 1. Project Introduction 🛡️

### Abstract 📄
In today’s digital landscape, hate speech is an escalating concern, often fueling division and unrest across communities. DweshaMukt is an **Advanced Multilingual and Multimodal Hate Speech Detection System** designed to counteract this issue by harnessing the power of **Bidirectional Encoder Representations from Transformers (BERT)** alongside cutting-edge **Deep Learning** and **Natural Language Processing (NLP)** techniques.

Our system tackles a unique challenge: detecting hate speech within **Hinglish**—a dynamic blend of Hindi and English—while also supporting **Hindi** and **English** languages individually. DweshaMukt leverages a pre-trained BERT model, specially optimized for real-time scenarios, offering robust analysis across a range of media. Its **multilingual and multimodal architecture** enables hate speech detection across diverse content types: **text**, **audio**, **video**, **images**, **GIFs**, and **YouTube comments**.

With an accuracy of **88%**, DweshaMukt stands as a promising solution for real-world hate speech detection applications, bridging language and media barriers to ensure safer, more inclusive online spaces.

**Index Terms:** Hate Speech Detection, BERT, Deep Learning, Natural Language Processing, Multilingual, Multimodal, Hinglish, Real-Time Analysis

---

### Project Timeline 📅

- **Start Date**: 15th February 2023
- **End Date**: 20th October 2024
- **Total Time Required**: 1 Year, 8 Months, and 5 Days

---

### Team Members 👥

| Team Members                   | GitHub Profile | LinkedIn Profile |
|--------------------------------|----------------|------------------|
| **Yash Suhas Shukla**          | [GitHub](https://github.com/StudiYash) | [LinkedIn](https://www.linkedin.com/in/yash-shukla-2024aiguy/) |
| **Tanmay Dnyaneshwar Nigade**   | [GitHub](#) | [LinkedIn](https://www.linkedin.com/in/tanmay-nigade-0ba002230/) |
| **Suyash Vikas Khodade**        | [GitHub](#) | [LinkedIn](https://www.linkedin.com/in/suyash-khodade/) |
| **Prathamesh Dilip Pimpalkar**  | [GitHub](#) | [LinkedIn](https://www.linkedin.com/in/prathamesh-pimpalkar-5a9545204/) |

### Project Guide 🎓

| Guide                           | GitHub Profile | LinkedIn Profile |
|---------------------------------|----------------|------------------|
| **Prof. Rajkumar Panchal**       | [GitHub](#) | [LinkedIn](#) |

---

## 2. Backend Preparation 🔧

### Mark Models Index

The backend development was an intricate journey, involving months of rigorous research, experimentation, and iterative coding. Each phase contributed to refining the system’s ability to detect hate speech across various input types and languages. 

Our **Mark Model Index Document** provides a comprehensive overview of this journey, showcasing each model’s evolution, from early concepts to the final optimized versions. Dive into the document to see how each model was crafted, tested, and fine-tuned to tackle the challenges of multilingual, multimodal hate speech detection.

[![Read the Full Mark Model Index Document](https://img.shields.io/badge/View-Mark%20Model%20Index%20Document-blue?style=for-the-badge&logo=Adobe)](https://github.com/StudiYash/DweshaMukt/blob/main/Mark%20Model%20Index.pdf)

---

## 3. Project Backend 🖥️

The backend architecture of DweshaMukt enables the system to classify various forms of input **text, audio, video, images, GIFs, and live YouTube comments** by first converting each to text before applying the hate speech detection model. Here are the main scenarios handled by the system:

1. **Text Input**: Processes user-entered text directly.
2. **Audio Input**: Converts audio to text using `Google Speech to Text API`, then classifies it.
3. **Image Input**: Extracts text from images via `Google Cloud Vision API`.
4. **GIF Input**: Analyzes GIFs using `Google Video Intelligence API` for text extraction.
5. **Video Input**: Extracts audio from videos, transcribes it, and classifies it.
6. **Live YouTube Video**: Fetches live comments using `pytchat` library, then classifies them.

The combined code integrates all these scenarios into a unified detection system, including added emoticon-based classification for enhanced accuracy.

---

## 4. Project Dataset 📊

### Overview
The **DweshaMukt Dataset** is a curated collection of comments carefully selected to support research on hate speech detection. This dataset includes multilingual data in **Hinglish**, **Hindi**, and **English**, capturing various instances of hate and non-hate speech. It is a valuable resource for researchers and developers working on projects aimed at building safer online communities.

---

### Dataset Composition
- **Datasets Used**: CONSTRAINT 2021 and Hindi Hate Speech Detection (HHSD)
- **Total Comments**: 22,977
  - **Hate Comments**: 9,705
  - **Non-Hate Comments**: 13,272

### Access the Dataset
To ensure responsible and secure usage, access to the DweshaMukt dataset is granted upon request. Please complete the form below to submit your application. We review each request to verify alignment with our project’s objectives.

[![Dataset Requesting Google Form](https://img.shields.io/badge/Request%20Access-Fill%20Out%20Form-purple?style=for-the-badge&logo=google)](https://forms.gle/RHNkoFQx4W94tXN37)

*Note: Approved requests will receive an email with download instructions within 2-3 business days.*

### Dataset Terms of Use
By requesting access to this dataset, you agree to the following:
- The dataset is strictly for **non-commercial, research, or educational purposes**.
- You will **cite the DweshaMukt project** in any publications or presentations that use this dataset.
- Redistribution or sharing of the dataset with unauthorized parties is strictly prohibited.

---

## 5. Project Frontend 🌐

The frontend for the DweshaMukt project is built as a **Streamlit** application, allowing users to interact seamlessly with our hate speech detection models across various input formats. This interface makes it easy to submit and analyze **text, audio, video, images, GIFs, and YouTube comments**.

---

### Key Features
- **Multi-format Detection**: Supports text, audio, video, images, GIFs, and YouTube comments.
- **Real-time Analysis**: Provides immediate feedback on uploaded content.
- **User-friendly Interface**: Simple navigation with clear instructions and dynamic visual feedback.
- **Emoji Detection**: Enhanced detection with emoticon analysis.

### Main Dashboard
![Dashboard Screenshot](https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Frontend%20Dashboard.png)

[![Explore Frontend Repository](https://img.shields.io/badge/View-Frontend%20Repository-blue?style=for-the-badge&logo=github)](https://github.com/tanmay183/Hate_Speech_Detection_Hinglish)

---

