import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
def download_video(resolution):
    url = url_entry.get()
    save_path = filedialog.askdirectory(title="Select Download Folder")
    if not save_path:
        messagebox.showerror("Error", "No folder selected!")
        return
    try:
        ydl_opts = {
            'format': 'bestaudio/best' if resolution == 'audio' else resolution,
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"The video/audio has been downloaded successfully!\nSaved to: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
Frame = tk.Tk()
Frame.geometry("800x500")
Frame.title("YouTube Video Downloader")
Frame.configure(bg='#f0f4f8')
header_label = tk.Label(Frame, text="YouTube Video Downloader", font=("Helvetica", 24, "bold"), bg='#1e3c72', fg='white')
header_label.pack(pady=30)
url_frame = tk.Frame(Frame, bg='#f0f4f8')
url_frame.pack(pady=20)
url_label = tk.Label(url_frame, text="Enter The Video URL:", font=("Helvetica", 14), bg='#f0f4f8', fg='#1e3c72')
url_label.grid(row=0, column=0, padx=10)
url_entry = tk.Entry(url_frame, width=40, font=("Helvetica", 14), relief="solid", borderwidth=2)
url_entry.grid(row=0, column=1, padx=10)
buttons_frame = tk.Frame(Frame, bg='#f0f4f8')
buttons_frame.pack(pady=30)
def create_rounded_button(parent, text, command, bg_color, fg_color):
    button = tk.Button(parent, text=text, command=command, font=("Helvetica", 14), fg=fg_color, bg=bg_color,
                       width=25, height=2, relief="flat", bd=0)
    button.grid(pady=10)
    button.config(highlightthickness=0, bd=0, relief="solid", borderwidth=0)
    return button
high_quality_button = create_rounded_button(buttons_frame, "Download High Quality", lambda: download_video("best"),
                                            bg_color='#4CAF50', fg_color='white')

low_quality_button = create_rounded_button(buttons_frame, "Download Low Quality", lambda: download_video("worst"),
                                           bg_color='#FF9800', fg_color='white')

audio_button = create_rounded_button(buttons_frame, "Download Audio Only", lambda: download_video("audio"),
                                     bg_color='#2196F3', fg_color='white')
Frame.mainloop()
