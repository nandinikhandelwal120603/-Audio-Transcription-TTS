# Audio Transcription and Text-to-Speech (TTS)

## Overview
This Python project enables users to record audio, transcribe the spoken content into text using OpenAI's Whisper model, and then convert the text back to speech using a text-to-speech (TTS) engine. The program combines audio recording, transcription, and speech synthesis into a single workflow.

## Features
- **Audio Recording**: Records audio input from the microphone for a specified duration.
- **Speech-to-Text Transcription**: Transcribes recorded audio to text using the Whisper model.
- **Text-to-Speech Conversion**: Converts the transcribed text into audible speech using the pyttsx3 library.

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.7 or higher
- Pip (Python package manager)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/nandinikhandelwal120603/Audio-Transcription-TTS.git
   cd Audio-Transcription-TTS
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies
The required Python libraries are listed in `requirements.txt`:
- `sounddevice`: For audio recording
- `numpy`: For numerical operations
- `wave`: For saving audio files
- `openai-whisper`: For audio transcription
- `pyttsx3`: For text-to-speech conversion

## Usage
1. Run the script:
   ```bash
   python audio_transcription_tts.py
   ```

2. The program will:
   - Record audio for a specified duration (default: 5 seconds).
   - Save the recorded audio as a `.wav` file.
   - Transcribe the audio to text using Whisper.
   - Convert the transcribed text back to speech using pyttsx3.

3. Listen to the synthesized speech output.

## File Description
- **`audio_transcription_tts.py`**: Main script for recording, transcribing, and converting text to speech.
- **`requirements.txt`**: Contains the list of dependencies for the project.

## Example Output
When you run the script, the terminal will display the transcription of your recorded audio:
```
Recording...
Recording complete.
Audio saved as recorded_audio.wav
Transcription:
Hello, this is a test audio.
```
The transcribed text will also be converted to speech and played back.

## Known Issues
- Whisper requires a significant amount of computational resources. Ensure your system meets the minimum requirements for running the model.
- Accuracy of transcription may vary based on the quality of the audio recording.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or bug fixes.

## Author
Nandini Khandelwal
