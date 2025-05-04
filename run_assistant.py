import os
import subprocess
from openai import OpenAI
import whisper
from dotenv import load_dotenv

# Load your OpenAI API key from .env
load_dotenv()
client = OpenAI()

# Paths
AUDIO_DIR = "audio/"
PROCESSED_DIR = "processed/"
TRANSCRIPT_DIR = "transcripts/"
SUMMARY_DIR = "summaries/"

# Step 1: Clean the raw audio using ffmpeg
def clean_audio(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    command = [
        "ffmpeg", "-y",           # -y to overwrite without asking
        "-i", input_path,
        "-ac", "1",               # mono
        "-ar", "16000",           # 16 kHz sample rate
        output_path
    ]

    print(f"Cleaning audio: {input_path} → {output_path}")
    subprocess.run(command, check=True)

# Step 2: Transcribe with Whisper (medium model)
def transcribe_audio(filename):
    base_name = os.path.splitext(filename)[0]
    input_audio = os.path.join(AUDIO_DIR, filename)
    processed_audio = os.path.join(PROCESSED_DIR, f"{base_name}.wav")

    # Clean the audio
    clean_audio(input_audio, processed_audio)

    print(f"Transcribing {processed_audio}...")
    model = whisper.load_model("medium")
    result = model.transcribe(processed_audio, language="en", fp16=False)

    transcript_path = os.path.join(TRANSCRIPT_DIR, f"{base_name}.txt")
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)

    with open(transcript_path, "w") as f:
        f.write(result["text"])

    return result["text"]

# Step 3: Summarize with GPT-4o
def summarize_text(transcript_text):
    print("Summarizing with GPT-4o...")
    prompt = f"""
You are an AI assistant summarizing a Lean Startup cofounder work session.

Here is the transcript:
\"\"\"
{transcript_text}
\"\"\"

Please generate the following:
1. 🧠 3–5 key ideas discussed
2. ✅ Action items with responsible person (if mentioned)
3. 📅 Proposed agenda for the next meeting
4. ❓ Open questions or unresolved points

Output in bullet points and clear structure.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

# Step 4: Save summary to file
def save_summary(filename, summary_text):
    base_name = os.path.splitext(filename)[0]
    summary_path = os.path.join(SUMMARY_DIR, f"{base_name}_summary.txt")
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)

    with open(summary_path, "w") as f:
        f.write(summary_text)

    print(f"✅ Summary saved to {summary_path}")

# Main function
def run():
    files = [f for f in os.listdir(AUDIO_DIR) if f.endswith((".mp3", ".m4a", ".wav"))]

    if not files:
        print("No audio files found in 'audio/' folder.")
        return

    for f in files:
        transcript = transcribe_audio(f)
        summary = summarize_text(transcript)
        save_summary(f, summary)

if __name__ == "__main__":
    run()
