# 📜 YouTube AI Notes Converter  

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
1️⃣ **Copy the YouTube Video Link** (Right-click & select _Copy link address_).  
2️⃣ **Paste the link** in the input field.  
3️⃣ **Click "Generate AI Notes"** to extract and summarize the transcript.  
4️⃣ **Enjoy structured notes** without watching the entire video! 🎉  

---
## ❗ Why Copy Link Address?  
Pasting the URL directly from the address bar might not work due to:  
🔹 Extra parameters (like playlists/timestamps) breaking the extraction process.  
✅ **Solution:** Always right-click the video & select **"Copy link address"** before pasting.  

---
## 🛠️ Installation & Usage  
### 1️⃣ Clone the Repository  
```bash
git clone https://huggingface.co/spaces/1Prarthana/YouTube-AI-Notes-Converter
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

## 🔑 API Keys
Set up a .streamlit/secrets.toml file for API authentication:
``` GOOGLE_API_KEY = "your-google-api-key" ```

### 📢 Contributing
We welcome contributions! Fork the repo, make your changes, and submit a pull request. 🚀


