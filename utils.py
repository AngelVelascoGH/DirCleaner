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
                file = File(event.src_path,extension.lower())
                organize(file)


def watcher(dir):
    current_dir = os.getcwd()
    target = os.path.join(current_dir,dir)
    print(f"Cleaning: {target}")

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

    # contents = os.listdir(target)
    #
    # create_dirs_if_missing()
    #
    # for content in contents:
    #     if os.path.isdir(content):

def organize(file):
    for folder, extensions in DIRECTORIES.items():
        if file.extension in extensions:
            print(folder)
