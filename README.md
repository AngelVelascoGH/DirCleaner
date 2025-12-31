# DirCleaner

A file organization tool that automatically sorts files into categorized folders based on their extensions and handles duplicates/archives. It can run as a one-time cleanup or continuously monitor a directory for new files.

## Features

- Automatic file organization by type (images, documents, music, videos, executables, archives)
- Optional automatic extraction of compressed files
- Configurable directory names and watched folder
- Can run as a system service with watchdog monitoring
- Handles duplicate files by appending numbers to filenames

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd DirCleaner
```

2. Install dependencies:
```
uv sync
```

3. Install as executable:
```
uv pip install -e .
```

This creates a `dircleaner` command available system-wide.

## Configuration

On first run, DirCleaner creates a configuration file at `~/.config/dircleaner/config.toml`.

Default configuration:
```toml
watch_dir = "Downloads"
auto_extract = false

[directories]
pictures = "Pictures"
documents = "Documents"
music = "Music"
videos = "Videos"
executables = "Executables"
archives = "Archives"
```

### Configuration Options

- `watch_dir`: Directory to monitor (relative to home directory if no argument provided)
- `auto_extract`: Enable automatic extraction of compressed files
- `[directories]`: Map file types to destination folder names. Remove any category you don't want organized.

### Supported File Types

- **Pictures**: jpg, png, gif, bmp, webp, svg, and more
- **Documents**: pdf, docx, txt, xlsx, pptx, and more
- **Music**: mp3, flac, wav, m4a, and more
- **Videos**: mp4, mkv, avi, mov, and more
- **Executables**: exe, deb, dmg, apk, and more
- **Archives**: zip, rar, tar, 7z, and more

## Usage

### Basic Usage

Run with default settings (uses directory from config):
```
dircleaner
```

### Specify Directory

Provide a directory path relative to current working directory:
```
dircleaner path/to/directory
```

The tool will:
1. Read configuration from `~/.config/dircleaner/config.toml`
2. Watch the specified directory (or configured directory if none provided)
3. Organize files into subdirectories based on their extensions
4. Extract archives if `auto_extract` is enabled
5. Handle duplicate filenames by appending numbers

### Examples

Organize Downloads folder (from config):
```
dircleaner
```

Organize a specific directory:
```
dircleaner Documents/messy-folder
```

## Running as a Service

To run DirCleaner as a systemd service that starts on boot:

1. Create service file at `/etc/systemd/system/dircleaner.service`:
```ini
[Unit]
Description=Directory Cleaner Service
After=network.target

[Service]
Type=simple
User=your-username
ExecStart=/path/to/.venv/bin/dircleaner
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. Enable and start the service:
```
sudo systemctl daemon-reload
sudo systemctl enable dircleaner
sudo systemctl start dircleaner
```

3. Check status:
```
sudo systemctl status dircleaner
```

## File Handling

### Duplicate Files

If a file with the same name exists in the destination, DirCleaner appends a number:
```
document.pdf -> document_1.pdf
document.pdf -> document_2.pdf
```

### Archive Extraction

When `auto_extract` is enabled:
- Creates a folder with the archive name
- Extracts contents into that folder
- Moves the archive to the Archives folder

Supported formats: zip, tar, tar.gz, tar.bz2, tar.xz (RAR requires rarfile package)

### Temporary Files

Download-in-progress files are ignored:
- .crdownload (Chrome)
- .part (Firefox)
- .tmp, .temp

## Development

Run without installing:
```
uv run src/main.py
```

Project structure:
```
DirCleaner/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── configs.py
│   ├── extensions.py
│   ├── file.py
│   └── utils.py
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.12 or higher
- watchdog
- rarfile (optional, for RAR extraction) **Unrar** must be installed
