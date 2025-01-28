import sounddevice as sd
import numpy as np
import wave
import whisper
import warnings
import pyttsx3

# Suppress warnings
warnings.filterwarnings("ignore")

# Step 1: Record Audio
samplerate = 16000
duration = 5  # seconds
filename = "recorded_audio.wav"

print("Recording...")
audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print("Recording complete.")

# Save the audio as a .wav file
with wave.open(filename, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)  # 2 bytes for 'int16' data type
    wf.setframerate(samplerate)
    wf.writeframes(audio.tobytes())

print(f"Audio saved as {filename}")

# Step 2: Load Whisper and Transcribe
model = whisper.load_model("tiny.en")
result = model.transcribe(filename)

print("Transcription: ")
print(result["text"])

# Step 3: Text-to-Speech Conversion
text = result["text"]

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Optionally, adjust properties like rate, volume, and voice
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Speak the transcribed text
engine.say(text)

# Wait until the speech finishes before ending the program
engine.runAndWait()
