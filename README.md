# FLAC/WAV to MP3 Converter

A Python GUI application for converting FLAC and WAV audio files to MP3 format with high quality (320kbps by default).

## Features

- **Intuitive graphical interface** with tkinter
- **Batch conversion** of multiple files
- **Optional folder structure preservation**
- **Configurable audio normalization**
- **Customizable configuration** via YAML file
- **Parallel processing** for better speed
- **Real-time progress bar**

## Requirements

### System Dependencies
- **Python 3.7+**
- **FFmpeg** (must be in PATH)

### Python Dependencies
- `PyYAML` - For configuration
- `tkinter` - For graphical interface (included with Python)
- `pathlib` - For path handling (included with Python 3.4+)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flac-wav-to-mp3-converter.git
   cd flac-wav-to-mp3-converter
   ```

2. **Install FFmpeg**
   
   **macOS (with Homebrew):**
   ```bash
   brew install ffmpeg
   ```
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **Windows:**
   - Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Add the bin directory to PATH

3. **Install Python dependencies**
   ```bash
   pip install PyYAML
   ```

## Usage

### Running the application
```bash
python main.py
```

### Graphical interface
1. **Select input folder** - Folder containing FLAC/WAV files
2. **Select output folder** - Where MP3 files will be saved
3. **Click "Convert"** to start the process

## Configuration

Edit the `config.yaml` file to customize the conversion:

```yaml
# Audio configuration
bitrate: 320          # Bitrate in kbps (128, 192, 256, 320)
sample_rate: 44100    # Sample rate in Hz
channels: 2           # Number of channels (1=mono, 2=stereo)

# Processing options
normalize: true               # Normalize audio with loudnorm
preserve_structure: true     # Maintain folder structure
```

## Project Structure

```
flac-wav-to-mp3-converter/
├── main.py              # Main entry point
├── config.yaml          # Configuration file
├── README.md            # Documentation
└── src/
    ├── gui.py           # Graphical interface
    ├── converter.py     # Conversion logic
    └── __pycache__/     # Python cache
```

## Technical Features

- **Supported formats:** FLAC, WAV → MP3
- **Codec:** libmp3lame (high quality)
- **Processing:** Multiprocess for better performance
- **Metadata:** Automatic metadata preservation
- **Normalization:** FFmpeg loudnorm for consistent audio

## Troubleshooting

### "yaml not working" error
```bash
pip install PyYAML
```

### "ffmpeg command not found" error
- Make sure FFmpeg is installed and in PATH
- Verify with: `ffmpeg -version`

### Application won't open
- Verify that Python 3.7+ is installed
- Run from the project directory


## Author

Developed with <3 for DJs.
