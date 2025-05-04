# Lean-Startup-Meeting-Assistant-v0.1
lightweight tool that transcribes, cleans and summarizes a audio record of a meeting

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

## 📁 Project Structure

meeting-assistant/
├── audio/ # Raw input files (.m4a, .mp3, etc.)
├── processed/ # Cleaned and resampled .wav files
├── transcripts/ # Whisper-generated transcripts
├── summaries/ # GPT-4o meeting summaries
├── .env # OpenAI API key
└── run_assistant.py # Main script

---

## 🧱 Step-by-Step Implementation

### ✅ 1. Python Project Setup

- Installed dependencies:
pip install openai-whisper openai python-dotenv

- Created folder structure and `.env` with `OPENAI_API_KEY=sk-...`

---

### ✅ 2. Audio Preprocessing with FFmpeg

- Installed ffmpeg:

brew install ffmpeg

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

1. Drop audio file in `/audio/`
2. Run: python3 run_assistant.py


3. Outputs:
- `/processed/cleaned.wav`
- `/transcripts/*.txt`
- `/summaries/*_summary.txt`

---

## 💰 Cost Summary

- Whisper (local): Free
- GPT-4o API: ~$0.01–0.05 per summary

---

## 📈 Next Versions

| Feature                | Notes                        |
|------------------------|------------------------------|
| Push to Notion/Slack   | Auto-send summaries           |
| Recurring topic tracking | Add memory layer            |
| Translation / diarization | More advanced transcription |

---

This is version `v0.1` — first working MVP of your cofounder assistant. 🔥




