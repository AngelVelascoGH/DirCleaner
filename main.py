import shutil
import sys
from configs import create_default_config, CONFIG_FILE
from utils import  watcher, initial_clean

from pathlib import Path


def main():
    if len(sys.argv) > 2:
        print("Args not identified")
        print("Usage: dircleaner [dir]  (if no dir is passed config dir will be used)")
    if len(sys.argv) == 2:
        dir = (sys.argv[1])
    else:
        dir = None
    
    if not CONFIG_FILE.exists():
        create_default_config()
    else:
        print("Config file found")

    initial_clean(dir)
    watcher(dir)




if __name__ == "__main__":
    main()
