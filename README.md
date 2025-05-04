# 🚀 Lean Startup Meeting Assistant v0.1  
**Technical Documentation & Step-by-Step Summary**

---

## 🎯 Purpose

The Lean Startup Meeting Assistant is a lightweight tool that:
1. Records cofounder ideation sessions (e.g. voice memos, Zoom)
2. Automatically transcribes the session using Whisper (OpenAI’s local speech-to-text)
3. Cleans the audio to improve transcription quality using ffmpeg
4. Summarizes the transcript using GPT-4o into:
   - Key ideas
   - Action items
   - Agenda for next session
   - Open questions
5. Saves both the transcript and summary in structured folders

---

## 🛠️ Stack Used

| Component             | Tool/Service         |
|----------------------|----------------------|
| Speech-to-text       | Whisper (local)      |
| Text summarization   | OpenAI GPT-4o (API)  |
| Audio cleanup        | FFmpeg               |
| Python libraries     | whisper, openai, dotenv, subprocess, os |
| File structure       | Folder-based         |
| OS                   | macOS (compatible with Linux/Windows) |

---

## 📦 Installation

1. Clone the project:

   ```bash
   git clone https://github.com/your-username/lean-startup-meeting-assistant.git
   cd lean-startup-meeting-assistant
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key in a `.env` file:

   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
   ```

5. Create the folder structure:

   ```bash
   mkdir -p audio processed transcripts summaries
   touch audio/.gitkeep processed/.gitkeep transcripts/.gitkeep summaries/.gitkeep
   ```

---

## 📁 Project Structure

```
meeting-assistant/
├── audio/             # Raw input files (.m4a, .mp3, etc.)
├── processed/         # Cleaned and resampled .wav files
├── transcripts/       # Whisper-generated transcripts
├── summaries/         # GPT-4o meeting summaries
├── .env               # OpenAI API key
├── requirements.txt   # Dependency list
└── run_assistant.py   # Main script
```

---

## 🧱 Step-by-Step Implementation

### ✅ 1. Python Project Setup

- Installed dependencies:
  ```
  pip install openai-whisper openai python-dotenv
  ```
- Created folder structure and `.env` with `OPENAI_API_KEY=sk-...`

---

### ✅ 2. Audio Preprocessing with FFmpeg

- Installed ffmpeg:
  ```
  brew install ffmpeg
  ```
- Added a Python function to:
  - Convert `.m4a` → `.wav`
  - Mono channel
  - 16kHz sample rate
  - Save in `/processed/`

---

### ✅ 3. Whisper Transcription

- Used `whisper.load_model("medium")` for better accuracy
- Transcribed processed `.wav` files
- Saved transcripts in `/transcripts/`

---

### ✅ 4. GPT-4o Summarization

- Integrated OpenAI SDK v1.0+
- Prompt includes:
  - Key ideas
  - Action items
  - Next meeting agenda
  - Open questions
- Used `gpt-4o` (confirmed via API access check)
- Saved summaries in `/summaries/`

---

### ✅ 5. Pipeline Automation

- Main script (`run_assistant.py`) does:
  - Scan `/audio/` for new files
  - Clean → `/processed/`
  - Transcribe → `/transcripts/`
  - Summarize → `/summaries/`
- Uses subprocess + os to run commands and handle folders

---

## ✅ How to Use

1. Drop your `.m4a`, `.mp3`, or `.wav` file into the `audio/` folder

2. Run the assistant:

   ```bash
   python3 run_assistant.py
   ```

3. You will get:
   - A cleaned `.wav` in `processed/`
   - A transcript in `transcripts/`
   - A GPT-4o-generated summary in `summaries/`

---

## 🔐 Privacy

This project is designed to work **100% locally**. Your audio files and transcripts are never uploaded or tracked.

- The `audio/`, `processed/`, `transcripts/`, and `summaries/` folders are **excluded from Git** using `.gitignore`
- The `.env` file is also ignored for safety
- You can use this tool to process sensitive cofounder meetings without any cloud risk (except GPT summarization)

---

## 💰 Cost Summary

- Whisper (local): Free
- GPT-4o API: ~$0.01–0.05 per summary

---

## 📈 Next Versions

| Feature                  | Notes                        |
|--------------------------|------------------------------|
| Push to Notion/Slack     | Auto-send summaries           |
| Recurring topic tracking | Add memory layer              |
| Translation / diarization| More advanced transcription   |

---

This is version `v0.1` — first working MVP of your cofounder assistant. 🔥