# ![DweshaMukt](https://github.com/StudiYash/DweshaMukt/blob/main/DweshaMukt%20Logo.png)

## 1. Project Introduction 🛡️

### Abstract 📄
In today’s digital landscape, hate speech is an escalating concern, often fueling division and unrest across communities. DweshaMukt is an **Advanced Multilingual and Multimodal Hate Speech Detection System** designed to counteract this issue by harnessing the power of **Bidirectional Encoder Representations from Transformers (BERT)** alongside cutting-edge **Deep Learning** and **Natural Language Processing (NLP)** techniques.

Our system tackles a unique challenge: detecting hate speech within **Hinglish**—a dynamic blend of Hindi and English—while also supporting **Hindi** and **English** languages individually. DweshaMukt leverages a pre-trained BERT model, specially optimized for real-time scenarios, offering robust analysis across a range of media. Its **multilingual and multimodal architecture** enables hate speech detection across diverse content types: **text**, **audio**, **video**, **images**, **GIFs**, and **YouTube comments**.

With an accuracy of **88%**, DweshaMukt stands as a promising solution for real-world hate speech detection applications, bridging language and media barriers to ensure safer, more inclusive online spaces.

**Index Terms:** Hate Speech Detection, BERT, Deep Learning, Natural Language Processing, Multilingual, Multimodal, Hinglish, Real-Time Analysis

### Project Timeline 📅

- **Start Date**: 15th February 2023
- **End Date**: 20th October 2024
- **Total Time Required**: 1 Year, 8 Months, and 5 Days

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

[![Read the Full Mark Model Index Document](https://img.shields.io/badge/View-Mark%20Model%20Index%20Document-blue?style=for-the-badge&logo=Adobe)](https://github.com/StudiYash/DweshaMukt/blob/main/Support%20Files/Mark%20Model%20Index.pdf)

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

### Key Features
- **Multi-format Detection**: Supports text, audio, video, images, GIFs, and YouTube comments.
- **Real-time Analysis**: Provides immediate feedback on uploaded content.
- **User-friendly Interface**: Simple navigation with clear instructions and dynamic visual feedback.
- **Emoji Detection**: Enhanced detection with emoticon analysis.

[![Explore Frontend Repository](https://img.shields.io/badge/View-Frontend%20Repository-blue?style=for-the-badge&logo=github)](https://github.com/tanmay183/Hate_Speech_Detection_Hinglish)

### Main Dashboard

<img src="https://github.com/StudiYash/DweshaMukt/blob/main/Support%20Files/Project%20Frontend%20Dashboard.png" style="border: 2px solid white; width: 600px; height: 300px;" alt="Dashboard Screenshot">

---

## 6. Project Telegram Bots 🤖

The DweshaMukt project is integrated with Telegram through a series of specialized bots, each designed to handle a different type of input. This allows users to classify text, audio, images, GIFs, video, and YouTube comments directly within the Telegram platform.

| Bot Name          | Description                              | Watch in Action |
|-------------------|------------------------------------------|-----------------|
| **Haspe Text**    | Processes text input.                    | [![Watch Haspe Text Bot](https://img.shields.io/badge/Watch-Haspe%20Text%20Bot-white?style=for-the-badge&logo=YouTube)](https://youtu.be/GTeI_L9EeBM) |
| **Haspe Audio**   | Processes audio input.                   | [![Watch Haspe Audio Bot](https://img.shields.io/badge/Watch-Haspe%20Audio%20Bot-magenta?style=for-the-badge&logo=YouTube)](https://youtu.be/mvFZ5Yckq28) |
| **Haspe Image**   | Processes image input.                   | [![Watch Haspe Image Bot](https://img.shields.io/badge/Watch-Haspe%20Image%20Bot-indigo?style=for-the-badge&logo=YouTube)](https://youtu.be/56sKWib-QTU) |
| **Haspe GIF**     | Processes GIF input.                     | [![Watch Haspe GIF Bot](https://img.shields.io/badge/Watch-Haspe%20Gif%20Bot-gold?style=for-the-badge&logo=YouTube)](https://youtu.be/p0YH30J_Dgk) |
| **Haspe Video**   | Processes video input.                   | [![Watch Haspe Video Bot](https://img.shields.io/badge/Watch-Haspe%20Video%20Bot-blue?style=for-the-badge&logo=YouTube)](https://youtu.be/4y4jWDYZOoA) |
| **Haspe YouTube** | Processes YouTube live comments.         | [![Watch Haspe YouTube Bot](https://img.shields.io/badge/Watch-Haspe%20YouTube%20Bot-crimson?style=for-the-badge&logo=YouTube)](https://youtu.be/75ToOIsmgdg) |

Each bot seamlessly interacts with the backend, delivering real-time classification results to users. Whether you're analyzing text, multimedia, or live YouTube comments, these bots ensure a versatile and accessible experience for hate speech detection.

To refer the code of these telegram bots, press the button below.

[![Explore Telegram Bots](https://img.shields.io/badge/View-Telegram%20Bots%20Code-teal?style=for-the-badge&logo=github)](#)

---

## 7. Project Representation 🎉

The DweshaMukt project was proudly showcased at the **Nexus 1.0 State Level Project Competition** on **15th April 2024**. Held at the **Army Institute of Technology, Pune**, this prestigious event was organized by the Department of Information Technology and Computer Engineering under the **AIT ACM Student Chapter**.

Representing this project at Nexus 1.0 allowed our team to not only share our research and technical achievements but also to raise awareness about the importance of addressing hate speech in today’s digital world. Competitions like these offer valuable platforms for knowledge exchange, constructive feedback, and networking with other innovators, researchers, and industry experts.

### Participation Certificates 🏆
Below are the participation certificates awarded to our team members for presenting DweshaMukt at Nexus 1.0.

<p align="center">
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Representation/Nexus%201.0%20State%20Level%20Competetion/Yash.png" alt="Certificate 1" width="45%" />
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Representation/Nexus%201.0%20State%20Level%20Competetion/Tanmay.png" alt="Certificate 2" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Representation/Nexus%201.0%20State%20Level%20Competetion/Suyash.png" alt="Certificate 3" width="45%" />
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Representation/Nexus%201.0%20State%20Level%20Competetion/Prathamesh.png" alt="Certificate 4" width="45%" />
</p>

---

## 8. Project Conference 📑

Presenting the **DweshaMukt** project at an international platform has been a milestone achievement for our team. Our research was showcased at the **CVMI-2024 IEEE International Conference on Computer Vision and Machine Intelligence**, hosted by **IIIT Allahabad, Prayagraj** on **19th and 20th October 2024**. The conference offered a valuable opportunity for knowledge exchange with global experts and researchers, fostering discussions on the latest advancements in computer vision and machine learning.

### Key Highlights
- **Research Paper Submission**: Our research paper on DweshaMukt was successfully submitted to IEEE.
- **Conference Attendance**: Represented by **Yash Shukla** and **Prof. Rajkumar Panchal**, the conference participation strengthened our network and insights within the academic community.
- **Conference Report**: The conference report details our experiences and learnings from the event, including keynote sessions and other relevant presentations on emerging research trends.

**To read our Research Paper, press the button below.**

[![Explore Telegram Bots](https://img.shields.io/badge/View-IEEE%20Research%20Paper-coral?style=for-the-badge&logo=IEEE)](#)

### Conference Participation Certificates 🎓

The following certificates were awarded for our participation and representation at CVMI-2024:

<p align="center">
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Conference/Project%20Conference%20Certificate%20Yash.jpg" alt="Certificate 1" width="75%" />
</p>

> *Showcasing our work at a conference of this caliber allowed us to share our vision for hate speech detection with an international audience, gaining invaluable feedback and recognition.*

---

## 9. Project Copyright ©️

Securing copyright for **DweshaMukt** marked an important milestone in safeguarding our innovation and intellectual property. Copyrighting our project not only protects the unique aspects of our hate speech detection system but also reinforces our commitment to responsible AI research. By copyrighting this idea, we ensure that the methods, models, and technological advances developed through this project remain attributed to our team.

### Copyright Publication Date: 25th October 2024

### Certificate of Copyright 🎓
<p align="center">
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Copyright/Copyright%20Certificate.png" alt="Copyright Certificate" width="60%" />
</p>

> *Establishing copyright protection is a proactive step towards fostering innovation, ensuring recognition, and laying a foundation for future advancements in hate speech detection.*

---

## 10. Project Funding 💸

The **DweshaMukt** project was generously funded by **Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering and Technology College**, whose support played a pivotal role in enabling our team to bring this ambitious vision to life. This funding allowed us to access essential resources, collaborate with experts, and ensure high-quality development across every phase of the project. 

### Funding Breakdown 📜

| Sr No | Demand Reason                     | Demand Cost |
|-------|-----------------------------------|-------------|
| 1     | Google Colab Pro                  | 1025        |
| 2     | Online Courses                    | 2684        |
| 3     | Project Presentation Competition  | 500         |
| 4     | Stationary Cost                   | 500         |
| **Total** |                               | **4709**    |

### Funding Certificate ✨
<p align="center">
  <img src="https://github.com/StudiYash/DweshaMukt/blob/main/Project%20Certifications/Project%20Funding/Project%20Funding%20Certificate.png" alt="Funding Certificate" width="45%" />
</p>

> *We extend our heartfelt gratitude to VPKBIET College for their trust and support. Their investment in DweshaMukt has been invaluable in pushing the boundaries of AI-driven hate speech detection.*

---

