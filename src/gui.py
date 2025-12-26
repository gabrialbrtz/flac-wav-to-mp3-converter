import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path

from src.converter import start_conversion

root = tk.Tk()
root.title("FLAC/WAV → MP3 320 DJ Converter")
root.geometry("520x280")

input_path = tk.StringVar()
output_path = tk.StringVar()


def browse_input():
    path = filedialog.askdirectory()
    if path:
        input_path.set(path)


def browse_output():
    path = filedialog.askdirectory()
    if path:
        output_path.set(path)


tk.Label(root, text="Input folder:").pack(anchor="w", padx=10, pady=5)
frame_in = tk.Frame(root)
frame_in.pack(fill="x", padx=10)
tk.Entry(frame_in, textvariable=input_path).pack(side="left", fill="x", expand=True)
tk.Button(frame_in, text="Browse", command=browse_input).pack(side="right")

tk.Label(root, text="Output folder:").pack(anchor="w", padx=10, pady=5)
frame_out = tk.Frame(root)
frame_out.pack(fill="x", padx=10)
tk.Entry(frame_out, textvariable=output_path).pack(side="left", fill="x", expand=True)
tk.Button(frame_out, text="Browse", command=browse_output).pack(side="right")
progress = ttk.Progressbar(root, length=400)
progress.pack(pady=20)

status = tk.Label(root, text="Waiting...")
status.pack()


def run():
    if not input_path.get() or not output_path.get():
        messagebox.showerror("Error", "Select input and output folders")
        return
    
    # Reset progress bar
    progress['value'] = 0
    progress['maximum'] = 100
    status.config(text="Starting conversion...")
    root.update()

    start_conversion(
        Path(input_path.get()),
        Path(output_path.get()),
        progress,
        status,
        root
    )


tk.Button(root, text="Convert", height=2, command=run).pack(pady=10)

if __name__ == "__main__":
    root.mainloop()