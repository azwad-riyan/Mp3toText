import os
import sys
import customtkinter as ctk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import whisper
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to convert MP3 to WAV
def convert_mp3_to_wav(mp3_path, progress_bar, progress_label):
    progress_label.set("Converting MP3 to WAV...")
    progress_bar.set(20)
    wav_path = mp3_path.replace(".mp3", ".wav")
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")
    progress_bar.set(50)
    return wav_path

# Function to transcribe audio using Whisper
def transcribe_audio(wav_path, progress_bar, progress_label):
    progress_label.set("Loading Whisper model...")
    progress_bar.set(60)
    model = whisper.load_model(resource_path("base"))  # Load the Whisper model
    progress_label.set("Transcribing audio...")
    progress_bar.set(80)
    result = model.transcribe(wav_path)
    progress_bar.set(100)
    progress_label.set("Transcription completed.")
    return result['text']

# Function to save the transcription to a text file
def save_transcription(text):
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Success", f"Transcription saved to {save_path}")

# Main function to handle file processing
def process_file(progress_bar, progress_label, text_widget):
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if not file_path:
        return
    
    def process():
        try:
            # Reset progress
            progress_bar.set(0)
            
            # Convert MP3 to WAV
            wav_path = convert_mp3_to_wav(file_path, progress_bar, progress_label)
            
            # Transcribe audio
            transcription = transcribe_audio(wav_path, progress_bar, progress_label)
            
            # Display transcription in the text widget
            text_widget.delete("1.0", ctk.END)
            text_widget.insert(ctk.END, transcription)
            
            # Show completion dialog
            messagebox.showinfo("Congratulations", "Transcription Completed!")
            
            # Ask user to save the transcription
            save_transcription(transcription)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    # Run the process in a separate thread to keep the UI responsive
    threading.Thread(target=process, daemon=True).start()

# Setup GUI
def setup_gui():
    ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
    
    root = ctk.CTk()
    root.title("MP3 to Text Converter")
    root.geometry("500x400")
    
    # Label for progress updates
    progress_label = ctk.StringVar(value="Welcome! Select an MP3 file to begin.")
    label = ctk.CTkLabel(root, textvariable=progress_label, wraplength=450, font=("Arial", 14))
    label.pack(pady=10)
    
    # Progress bar
    progress_bar = ctk.CTkProgressBar(root, width=400)
    progress_bar.pack(pady=10)
    progress_bar.set(0)
    
    # Button to select and process the file
    process_button = ctk.CTkButton(root, text="Select MP3 File", command=lambda: process_file(progress_bar, progress_label, text_widget))
    process_button.pack(pady=20)
    
    # Text widget to display transcription
    text_widget = ctk.CTkTextbox(root, wrap="word", width=450, height=150, font=("Arial", 12))
    text_widget.pack(pady=10, padx=10)
    
    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
