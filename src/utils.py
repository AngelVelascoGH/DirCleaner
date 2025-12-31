from enum import verify
import rarfile
import shutil
import os
import sys

from .configs import read_configs
from .extensions import TEMP_DOWNLOAD, ARCHIVES
from .file import File
from pathlib import Path
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

CONFIGS = {}
DIRS = {}


class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        match event.event_type:
            case "created":
                if event.is_directory:
                    return
                extension = Path(f"{event.src_path}").suffix
                if extension in TEMP_DOWNLOAD:
                    print("Temporary File, ignoring until file is donwloaded")
                    return
                file = File(event.src_path,extension.lower())
                if file.get_extension() in ARCHIVES:
                    print("Auto Extracting file")
                    extract(file)
                    return
                print(f"A new file was created: {file.get_name()}")
                organize(file)


def watcher(dir):
    target = verify_dir(dir)
    print(f"Organizing: {target}")

    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler,target,recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()

def organize(file):
    for folder, extensions in DIRS.items():
        if file.get_extension() in extensions and folder != None:
            print(f"Verifying if /{folder} exists in Home")
            target = os.path.join(Path.home(),folder)

            if not os.path.exists(target):
                print(f"Creating /{target} dir")
                os.mkdir(target)

            source = Path(file.path)
            target = Path(target)


            try:
                if (target / file.get_name()).exists():
                    print("File already exists in target Dir, ")
                    id = 1
                    file.set_name(source.stem + "_" + f"{id}" + file.extension)
                    target = Path(target / (file.get_name()))
                    while (target.exists()):
                        id += 1
                else:
                    target = target / file.get_name()
                    
                source.rename(target)
                print(f"File {file.get_name()} moved to {target}")
                return
            except FileNotFoundError:
                print(f"Error: source file not found at {source}")
            except OSError as e:
                print(f"An OS error occurred {e}")

    print("File extension not defined, or folder not specified in configs, not organizing")

def initial_clean(dir):
    global CONFIGS, DIRS
    CONFIGS, DIRS = read_configs()

    target = verify_dir(dir)
    print("Running initial clean")
    for entry in target.iterdir(): 
        if not entry.is_dir():
            file_path = target / entry
            file = File(file_path,entry.suffix)
            if file.get_extension() in ARCHIVES:
                print("Auto Extracting file")
                extract(file)
            else:
                organize(file)


def extract(file):
    if not CONFIGS.get('auto_extract'):
        print("Auto extract is disabled in configs")
        return
    ext = file.get_extension()
    if ext == '.rar':
        extract_rar(file)
    else:
        extract_archive(file)

def extract_archive(file):
    try:
        target = Path(file.get_path()).with_suffix("")
        print(f"Unpacking to {target}")
        shutil.unpack_archive(file.get_path(),target)
        print(f"Successfully extracted all files from {file.get_name()}")
        Path(file.get_path()).unlink(missing_ok=True)
    except Exception as e:
        print(f"Error during extraction: {e}")

def extract_rar(file):
    try:
        with rarfile.RarFile(file.get_path()) as rar_archive:
            rar_archive.extractall(Path(file.get_path()).stem)
        print(f"Successfully extracted all files from {file.get_name()}")
    except Exception as e:
        print(f"Error during extraction: {e}")

def verify_dir(dir):
    if dir is None:
        final_dir = Path.home() / CONFIGS.get("watch_dir",'Downloads')
    else:
        final_dir = Path.cwd() / dir
    if not final_dir.exists():
            print(f"specified dir to watch does not exist")
            sys.exit(1)
    return final_dir
