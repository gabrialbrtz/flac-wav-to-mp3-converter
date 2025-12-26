from tkinter import messagebox
from pathlib import Path
import subprocess
import yaml
import os
from concurrent.futures import ProcessPoolExecutor

SUPPORTED_EXT = (".flac", ".wav")

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

BITRATE = str(config.get("bitrate", 320))
SAMPLE_RATE = str(config.get("sample_rate", 44100))
CHANNELS = str(config.get("channels", 2))
NORMALIZE = config.get("normalize", True)
PRESERVE_STRUCTURE = config.get("preserve_structure", True)


def convert_file(args):
    input_path, input_root, output_root = args

    rel = input_path.relative_to(input_root) if PRESERVE_STRUCTURE else input_path.name
    output_path = (output_root / rel).with_suffix(".mp3")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path)
    ]

    if NORMALIZE:
        cmd += ["-af", "loudnorm"]

    cmd += [
        "-vn",
        "-ac", CHANNELS,
        "-ar", SAMPLE_RATE,
        "-c:a", "libmp3lame",
        "-b:a", f"{BITRATE}k",
        "-map_metadata", "0",
        str(output_path)
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def start_conversion(input_dir, output_dir, progress_bar, status_label, root):
    files = [
        Path(dir_path) / f
        for dir_path, _, filenames in os.walk(input_dir)
        for f in filenames
        if f.lower().endswith(SUPPORTED_EXT)
    ]

    total = len(files)
    if total == 0:
        messagebox.showwarning("No files", "No FLAC or WAV files found")
        return

    progress_bar["maximum"] = total

    with ProcessPoolExecutor() as executor:
        futures = []
        for f in files:
            futures.append(executor.submit(convert_file, (f, input_dir, output_dir)))

        for i, future in enumerate(futures, start=1):
            try:
                future.result()
                progress_bar["value"] = i
                status_label.config(text=f"Processing {i}/{total}")
                root.update()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert file: {str(e)}")
                return

    status_label.config(text="Conversion completed")
    progress_bar["value"] = total
    root.update()
    messagebox.showinfo("Complete", f"Successfully converted {total} files to MP3")