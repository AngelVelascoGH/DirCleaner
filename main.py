import sys
from utils import  watcher
def main():
    if len(sys.argv) != 2:
        print("Missing arguments.")
        print("Usage: uv run main.py [Dir]")
        print("Dir route is relative to Home Directory")
        sys.exit(1)

    dir = (sys.argv[1])

    watcher(dir)
        

if __name__ == "__main__":
    main()
