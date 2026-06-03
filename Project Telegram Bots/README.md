## Project Telegram Bots 🤖

The **DweshaMukt** project is integrated with **Telegram** through a series of specialized bots, each designed to handle a different type of input. This allows users to classify text, audio, images, GIFs, video, and YouTube comments directly within the Telegram platform.

| Bot Name          | Description                              | Watch in Action |
|-------------------|------------------------------------------|-----------------|
| **Haspe Text**    | Processes text input.                    | [![Watch Haspe Text Bot](https://img.shields.io/badge/Watch-Haspe%20Text%20Bot-white?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/15Fzb9yz3sgqt2pynk1NeRJ7qeXQiYALZ/view?usp=sharing) |
| **Haspe Audio**   | Processes audio input.                   | [![Watch Haspe Audio Bot](https://img.shields.io/badge/Watch-Haspe%20Audio%20Bot-magenta?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/13jM8Uc7FJPy7pjQwF4kUOhFasmbiiHz6/view?usp=sharing) |
| **Haspe Image**   | Processes image input.                   | [![Watch Haspe Image Bot](https://img.shields.io/badge/Watch-Haspe%20Image%20Bot-indigo?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/17uaC-yYRBFHkI1r2cnQ9pwrtmwlGuGlf/view?usp=sharing) |
| **Haspe GIF**     | Processes GIF input.                     | [![Watch Haspe GIF Bot](https://img.shields.io/badge/Watch-Haspe%20GIF%20Bot-gold?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1MrCXGwq3_FH9ek_ouR7_0wNSC_GPU8-e/view?usp=sharing) |
| **Haspe Video**   | Processes video input.                   | [![Watch Haspe Video Bot](https://img.shields.io/badge/Watch-Haspe%20Video%20Bot-blue?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1mMaORjkkJyi7LyE6O1N_Z-xPhSL-BzXy/view?usp=sharing) |
| **Haspe YouTube** | Processes YouTube live comments.         | [![Watch Haspe YouTube Bot](https://img.shields.io/badge/Watch-Haspe%20YouTube%20Bot-crimson?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1g-AKNtMI1AXyuP2FNh_Wwjt7VYSkO-I6/view?usp=sharing) |

Each bot seamlessly interacts with the backend, delivering real-time classification results to users. Whether you're analyzing text, multimedia, or live YouTube comments, these bots ensure a versatile and accessible experience for hate speech detection.

## Portable Setup Notes

Run the notebooks from inside a cloned DweshaMukt repository. The bot notebooks locate model assets from `Project Backend/` automatically.

Configure credentials through environment variables before running a bot:

```text
TELEGRAM_BOT_TOKEN
GOOGLE_APPLICATION_CREDENTIALS
```

`GOOGLE_APPLICATION_CREDENTIALS` is needed only for bots that use Google Cloud APIs, such as audio, image, GIF, and video workflows. Do not commit real bot tokens or service-account JSON files.

To refer the code of these telegram bots, press the button below.

[![Explore Telegram Bots](https://img.shields.io/badge/View-Telegram%20Bots%20Code-teal?style=for-the-badge&logo=github)](https://github.com/StudiYash/DweshaMukt/tree/main/Project%20Telegram%20Bots/Codes)

---
