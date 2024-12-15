
# MP3 to Text Converter



# Introduction

A beginner-friendly application that converts MP3 audio files to text using OpenAI's Whisper model. It includes a simple graphical interface for selecting audio files, tracking progress, and saving the transcription.

# Features
- Converts MP3 audio files to WAV format.
- Transcribes audio to text with support for diverse accents, including Asian English.
- Displays progress updates with a modern user interface.
- Saves transcriptions as `.txt` files.




# How to Use This Application
## Step 1: Install Python
Download and install Python (version 3.8 or higher) from the official Python website:
👉 [Download Python](https://www.python.org/downloads/windows/)

During installation, check the option **"Add Python to PATH".**
This ensures you can run Python and pip from your terminal.
## Step 2: Install Dependencies
After installing Python:

Open your terminal (Command Prompt, PowerShell, or your terminal of choice).

Run the following commands to install required libraries:

```bash
pip install customtkinter pydub whisper ffmpeg-python `
```
Ensure FFmpeg is installed on your system:

**Windows:**

Download FFmpeg from https://ffmpeg.org/ .
Extract the downloaded files and add the bin folder to your system’s environment PATH.

👉 Guide to Add FFmpeg to PATH macOS/Linux: 
Use your package manager (e.g., Homebrew for macOS or apt for Ubuntu):

`brew install ffmpeg`    # For macOS

`sudo apt install ffmpeg `   # For Linux

## Step 3: Run the Script
Clone or download this repository:

To clone you should have Git installed in your windows system. 
If you don't have it just downloaded from  👉 [here](https://git-scm.com/downloads/win) & install it. 

```bash
git clone https://github.com/azwad-riyan/Mp3toText.git
```

```bash
cd Mp3toText`
```
Run the script:

```bash
python main.py`
```
## Step 4: Use the Application
The graphical interface will open.
Click **"Select MP3 File"** to choose an audio file.
Wait for the progress bar to complete transcription.
View the transcription in the text box and save it as a `.txt` file.
## Contributing

Feel free to fork this repository, make your changes, and submit a pull request. Your contributions are welcome!

