import shutil
import sys
import tomllib
from pathlib import Path

from extensions import *

CONFIG_DIR = Path.home() / ".config" / "dircleaner"
CONFIG_FILE = CONFIG_DIR / "config.toml"
DEFAULT_FILE = Path.cwd() / "config.toml"
CONFIGS = None
DIRS = {}

def create_default_config():
    CONFIG_DIR.mkdir(parents=True,exist_ok=True)
    try:
        shutil.copy(DEFAULT_FILE, CONFIG_FILE)
        print(f"Default config placed in /.config/dircleaner")
    except FileNotFoundError:
        print(f"Critical error, default config file not found")
        sys.exit(1)
    except Exception as e:
        print(f"An error ocurred {e}")

def read_configs():
    configs = {}
    dirs = {}

    extension_map = {
        "pictures" : IMAGE_EXTENSIONS,
        "music" : AUDIO_EXTENSIONS,
        "videos" : VIDEO_EXTENSIONS,
        "documents" : DOCUMENT_EXTENSIONS,
        "executables" : EXECUTABLE_EXTENSIONS
    }

    with open(CONFIG_FILE, 'rb') as f:
        try:
            configs = tomllib.load(f)
            if "watch_dir" not in configs:
                configs['watch_dir'] = 'Downloads'
            if "auto_extract" not in configs:
                configs["auto_extract"] = False
            dirs = {}
            for key,folder_name in configs.get('directories',{}).items():
                if key in extension_map:
                    dirs[folder_name] = extension_map[key] 

            return configs, dirs
                    
        except tomllib.TOMLDecodeError as e:
            print(f"Config file corrupted: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An error has ocurred when reading config file: {e}")
            sys.exit(1)


