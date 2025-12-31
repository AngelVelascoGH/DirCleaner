import os

from file import File
from pathlib import Path
from extensions import *
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


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
                print(f"A new file was created: {file.get_name()}")
                organize(file)


def watcher(dir):
    current_dir = os.getcwd()
    target = os.path.join(current_dir,dir)
    print(f"Organizing: {target}")

    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler,target,recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()

def organize(file):
    for folder, extensions in DIRECTORIES.items():
        if file.get_extension() in extensions:
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

    print("File extension not defined, not organizing")

def initial_clean(dir):
    p = Path(dir)
    for entry in p.iterdir(): 
        if not entry.is_dir():
            current_dir = Path.cwd()
            file_path = current_dir / entry
            file = File(file_path,entry.suffix)
            organize(file)

