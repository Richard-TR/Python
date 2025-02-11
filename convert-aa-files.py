#Install ffmpeg:
#sudo apt install ffmpeg   # Linux
#brew install ffmpeg       # Mac
#choco install ffmpeg      # Windows

#Install Python libraries:
#pip install tkinter filedialog

#This script will allow you to browse to .aa files and convert them to .mp3. This will work for all old style DRM free Audible files. This breaks no terms of service with Audible as you have bought and own the files.
#The script may appear as if it has frozen during converting, if you check the source folder containing the .aa files you will see the .mp3 files being generated.



import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert .aa to .mp3 using ffmpeg
def convert_aa_to_mp3(file_paths):
    successful = []
    failed = []

    for file_path in file_paths:
        folder, filename = os.path.split(file_path)
        base_name, _ = os.path.splitext(filename)
        mp3_file = os.path.join(folder, base_name + ".mp3")

        # FFmpeg command (for DRM-free .aa files)
        cmd = f'ffmpeg -i "{file_path}" -codec:a libmp3lame -qscale:a 2 "{mp3_file}" -y'

        try:
            subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            successful.append(filename)
        except subprocess.CalledProcessError:
            failed.append(filename)

    # Display final summary message
    summary_message = "Conversion Complete!\n\n"
    
    if successful:
        summary_message += "✅ Successfully Converted:\n" + "\n".join(successful) + "\n\n"
    if failed:
        summary_message += "❌ Failed to Convert:\n" + "\n".join(failed) + "\n\n"
    
    if not failed:
        summary_message += "All files converted successfully! 🎉"
    
    messagebox.showinfo("Conversion Summary", summary_message)

# Function to browse and select .aa files
def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Audible files", "*.aa")])
    if file_paths:
        convert_aa_to_mp3(file_paths)

# GUI setup
root = tk.Tk()
root.title("Audible .AA to .MP3 Converter")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Select .AA files to convert:", font=("Arial", 12))
label.pack()

browse_button = tk.Button(frame, text="Browse Files", command=browse_files, font=("Arial", 12), bg="lightblue")
browse_button.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=root.quit, font=("Arial", 12), bg="lightcoral")
exit_button.pack()

root.mainloop()

