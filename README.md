# 📜 YouTube AI Notes Converter  
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](README.md)

Convert YouTube videos into AI-generated concise and structured notes! 🎥✨  

---------- 
### Demo : [Here▶️](https://youtube-ai-notes.streamlit.app/)
--- 
### Demo Screenshot:
![Screenshot 2025-03-04 152512](https://github.com/user-attachments/assets/e24dc4e7-8edd-4240-8227-860864c3c3c5)
![Screenshot 2025-03-04 152602](https://github.com/user-attachments/assets/005c9c50-3cef-4555-80dc-60a2b3988dc0)
![Screenshot 2025-03-04 152652](https://github.com/user-attachments/assets/f98ae7f2-41bf-4296-9613-11895debdefa)



----
## 🚀 Features  
- 🎙️ **Automatic Transcript Extraction** – Extracts video transcripts seamlessly.  
- 📝 **AI-Generated Notes** – Converts transcripts into well-structured notes.  
- 🎯 **Concise & Readable** – Eliminates unnecessary details for better clarity.  
- 🔗 **Easy YouTube Link Processing** – Works best with copied video links.  

## 🎯 How It Works  
1️⃣ **Copy the YouTube Video Link** (Right-click & select _Copy link__).  
2️⃣ **Paste the link** in the input field.  
3️⃣ **Click "Generate AI Notes"** to extract and summarize the transcript.  
4️⃣ **Enjoy structured notes** without watching the entire video! 🎉  

---
## 🛠️ Installation & Usage  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Prarthana-Singh/YouTube-AI-Notes.git
cd YouTube-AI-Notes-Converter
```

### 2️⃣ Install Dependencies
Create a virtual environment and install required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```
---

## 📄 Dependencies
Ensure these packages are installed:
1. streamlit
2. youtube-transcript-api
3. google-generativeai
4. transformers
5. torch

## 🔑Add API keys to .env
``` GOOGLE_API_KEY = "your-google-api-key" ```

----

### 🤝 Contributing
We welcome contributions from everyone! Here's how you can help:


##### 📌First-Time Contributors
If you're new to open-source, follow these steps:

1. Fork the repository (click the Fork button on GitHub)
2. Clone your fork:
```bash
   git clone https://github.com/Prarthana-Singh/YouTube-AI-Notes-Converter.git
```
3. Create a new branch:
```bash
git checkout -b my-feature-branch
```

#### ➡️Making Changes
* Make your changes (start with small fixes like documentation improvements)
* Test your changes:
```bash
python tests.py
```
* Commit with a clear message:
```bash
git commit -m "fix: correct typo in installation guide"
```

#### ▶️Submitting a Pull Request
* Push your changes:
```bash
git push origin my-feature-branch
```
* On GitHub, click "Compare & pull request"
* Fill out the PR template explaining your changes
---

### Good First Issues
Look for these labels:
* good first issue - Great for beginners!
* documentation - Help improve docs
* bug - Fix reported issues
---

### ❓ Support
* Got stuck? Open an issue with:
* What you tried
* What happened
* Screenshots if applicable
---

### 📜 License
* This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---

### 🙏 Acknowledgments
* Google YouTube API
* Contributors like you!

**💖 Happy Contributing! Remember, every big project starts with small contributions.**
